"""Testes das regras de métricas."""

from decimal import Decimal

from app.domain.metrics import SaleValue, calculate_sales_summary


def test_calculates_sales_summary() -> None:
    """Soma vendas e calcula ticket médio com precisão decimal."""
    result = calculate_sales_summary([SaleValue(Decimal(10)), SaleValue(Decimal(20))])
    assert result.revenue == Decimal(30)
    assert result.orders == 2
    assert result.average_ticket == Decimal(15)


def test_empty_sales_have_zero_ticket() -> None:
    """Evita divisão por zero em uma operação sem pedidos."""
    assert calculate_sales_summary([]).average_ticket == Decimal(0)
