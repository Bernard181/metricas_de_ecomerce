"""Contratos Pydantic de entrada e saída."""

from decimal import Decimal

from pydantic import BaseModel, Field


class ImportResultResponse(BaseModel):
    """Resultado da importação de um lote CSV."""

    imported: int
    ignored: int
    invalid: int
    errors: list[str] = Field(default_factory=list)


class MetricsSummaryResponse(BaseModel):
    """KPIs básicos exibidos no dashboard."""

    revenue: Decimal
    orders: int
    average_ticket: Decimal


class RevenuePointResponse(BaseModel):
    """Ponto diário da série de receita."""

    date: str
    revenue: Decimal
