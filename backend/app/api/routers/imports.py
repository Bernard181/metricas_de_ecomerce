"""Importação CSV para demonstração e onboarding."""

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.api.schemas import ImportResultResponse
from app.application.sales_csv import parse_and_import_csv
from app.infrastructure.database import get_session

router = APIRouter(prefix="/imports", tags=["imports"])


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
        result = parse_and_import_csv(content, session)
    except UnicodeDecodeError as error:
        raise HTTPException(status_code=422, detail="CSV deve usar UTF-8") from error
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error

    return ImportResultResponse(
        imported=result.imported,
        ignored=result.ignored,
        invalid=result.invalid,
        errors=result.errors,
    )
