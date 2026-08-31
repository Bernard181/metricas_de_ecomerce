"""Casos de uso de ingestão e consulta de vendas."""

from datetime import datetime
from decimal import Decimal

from sqlalchemy import Select, func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.domain.metrics import SalesSummary, SaleValue, calculate_sales_summary
from app.infrastructure.models import SaleEventModel


def save_sale(
    session: Session,
    *,
    source: str,
    external_id: str,
    occurred_at: datetime,
    total: Decimal,
    currency: str,
) -> bool:
    """Persiste uma venda; retorna falso quando a chave idempotente já existe."""
    sale = SaleEventModel(
        source=source,
        external_id=external_id,
        occurred_at=occurred_at,
        total=total,
        currency=currency.upper(),
    )
    session.add(sale)
    try:
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False


def sales_summary(session: Session, start: datetime | None, end: datetime | None) -> SalesSummary:
    """Busca vendas do período e delega o cálculo ao domínio puro."""
    statement: Select[tuple[SaleEventModel]] = select(SaleEventModel)
    if start:
        statement = statement.where(SaleEventModel.occurred_at >= start)
    if end:
        statement = statement.where(SaleEventModel.occurred_at <= end)
    sales = session.scalars(statement).all()
    return calculate_sales_summary(SaleValue(total=sale.total) for sale in sales)


def revenue_series(session: Session) -> list[tuple[str, Decimal]]:
    """Agrupa a receita por dia para visualização de tendência."""
    day = func.date(SaleEventModel.occurred_at)
    rows = session.execute(select(day, func.sum(SaleEventModel.total)).group_by(day).order_by(day)).all()
    return [(str(date), Decimal(total)) for date, total in rows]
