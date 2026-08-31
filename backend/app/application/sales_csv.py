"""Importação de vendas a partir de arquivo CSV (compartilhado por HTTP e seed)."""

import csv
import io
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal, InvalidOperation

from sqlalchemy.orm import Session

from app.application.sales import save_sale

REQUIRED_COLUMNS = {"external_id", "occurred_at", "total", "currency"}


@dataclass
class CsvImportResult:
    """Contagem final após processar um lote CSV."""

    imported: int = 0
    ignored: int = 0
    invalid: int = 0
    errors: list[str] = field(default_factory=list)


def parse_and_import_csv(content: bytes, session: Session) -> CsvImportResult:
    """Decodifica, valida e persiste vendas de um CSV UTF-8 sem duplicar pedidos."""
    text = content.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")

    result = CsvImportResult()
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
            result.imported += int(is_new)
            result.ignored += int(not is_new)
        except (KeyError, ValueError, InvalidOperation) as error:
            result.invalid += 1
            if len(result.errors) < 20:
                result.errors.append(f"Linha {line}: {error}")
    return result
