"""Importação CSV para demonstração e onboarding."""

import csv
import io
from datetime import datetime
from decimal import Decimal, InvalidOperation

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.api.schemas import ImportResultResponse
from app.application.sales import save_sale
from app.infrastructure.database import get_session

router = APIRouter(prefix="/imports", tags=["imports"])
REQUIRED_COLUMNS = {"external_id", "occurred_at", "total", "currency"}


@router.post("/sales-csv", response_model=ImportResultResponse)
async def import_sales_csv(
    file: UploadFile = File(...), session: Session = Depends(get_session)
) -> ImportResultResponse:
    """Importa CSV UTF-8 com vendas sem duplicar pedidos já processados."""
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=422, detail="Envie um arquivo CSV")
    content = await file.read()
    if len(content) > 5_000_000:
        raise HTTPException(status_code=413, detail="Arquivo excede o limite de 5 MB")
    try:
        reader = csv.DictReader(io.StringIO(content.decode("utf-8-sig")))
    except UnicodeDecodeError as error:
        raise HTTPException(status_code=422, detail="CSV deve usar UTF-8") from error
    if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
        raise HTTPException(
            status_code=422, detail=f"Colunas obrigatórias: {sorted(REQUIRED_COLUMNS)}"
        )

    imported = ignored = invalid = 0
    errors: list[str] = []
    for line, row in enumerate(reader, start=2):
        try:
            occurred_at = datetime.fromisoformat(row["occurred_at"].replace("Z", "+00:00"))
            total = Decimal(row["total"])
            if not row["external_id"] or total < 0 or len(row["currency"]) != 3:
                raise ValueError("valores inválidos")
            is_new = save_sale(
                session,
                source="csv",
                external_id=row["external_id"],
                occurred_at=occurred_at,
                total=total,
                currency=row["currency"],
            )
            imported += int(is_new)
            ignored += int(not is_new)
        except (KeyError, ValueError, InvalidOperation) as error:
            invalid += 1
            if len(errors) < 20:
                errors.append(f"Linha {line}: {error}")
    return ImportResultResponse(imported=imported, ignored=ignored, invalid=invalid, errors=errors)
