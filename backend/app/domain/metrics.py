"""Cálculos determinísticos dos KPIs iniciais."""

from collections.abc import Iterable
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class SaleValue:
    """Valor de um pedido elegível para agregação."""

    total: Decimal


@dataclass(frozen=True)
class SalesSummary:
    """Resumo de KPIs de vendas para um período."""

    revenue: Decimal
    orders: int
    average_ticket: Decimal


def calculate_sales_summary(sales: Iterable[SaleValue]) -> SalesSummary:
    """Calcula receita, pedidos e ticket médio sem depender de infraestrutura."""
    values = list(sales)
    revenue = sum((sale.total for sale in values), start=Decimal(0))
    orders = len(values)
    average_ticket = revenue / orders if orders else Decimal(0)
    return SalesSummary(revenue=revenue, orders=orders, average_ticket=average_ticket)
