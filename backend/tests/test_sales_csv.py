"""Testes da importação compartilhada de vendas via CSV."""

from decimal import Decimal
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.application.sales import sales_summary
from app.application.sales_csv import parse_and_import_csv
from app.infrastructure import models  # noqa: F401  (registra as tabelas no metadata)
from app.infrastructure.database import Base

SAMPLE_CSV = (
    b"external_id,occurred_at,total,currency\n"
    b"demo-1,2026-08-01T10:30:00Z,100.00,BRL\n"
    b"demo-2,2026-08-02T11:00:00Z,50.50,BRL\n"
    b"demo-3,2026-08-02T12:00:00Z,25.25,BRL\n"
)


def _session():
    """Cria sessão isolada sobre um banco SQLite em memória."""
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)(), engine


def test_imports_valid_rows_and_counts() -> None:
    """Conta corretamente pedidos importados e inválidos."""
    session, _ = _session()
    result = parse_and_import_csv(SAMPLE_CSV, session)
    assert result.imported == 3
    assert result.ignored == 0
    assert result.invalid == 0


def test_import_is_idempotent() -> None:
    """Reimportar não duplica pedidos já existentes."""
    session, _ = _session()
    assert parse_and_import_csv(SAMPLE_CSV, session).imported == 3
    again = parse_and_import_csv(SAMPLE_CSV, session)
    assert again.imported == 0
    assert again.ignored == 3


def test_invalid_rows_are_reported_and_skipped() -> None:
    """Linhas malformadas são sinalizadas sem interromper o lote."""
    session, _ = _session()
    payload = SAMPLE_CSV + b"demo-x,notadate,1.00,BRL\n" b"demo-y,2026-08-01T10:00:00Z,-5,BRL\n"
    result = parse_and_import_csv(payload, session)
    assert result.invalid == 2
    assert result.imported == 3


def test_missing_required_column_raises() -> None:
    """Falha rápido quando há colunas obrigatórias ausentes."""
    session, _ = _session()
    payload = b"external_id,occurred_at,total\n" b"demo-1,2026-08-01T10:00:00Z,1.00\n"
    try:
        parse_and_import_csv(payload, session)
    except ValueError as error:
        assert "currency" in str(error)
    else:
        raise AssertionError("deveria levantar ValueError")


def test_seed_csv_path_is_importable() -> None:
    """Garante que o csv de demonstração continua válido para semear dados."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    sample = repo_root / "docs" / "sample-sales.csv"
    assert sample.exists()
    session, _ = _session()
    result = parse_and_import_csv(sample.read_bytes(), session)
    assert result.imported > 0
    summary = sales_summary(session, None, None)
    assert summary.revenue == Decimal("1707.30")
