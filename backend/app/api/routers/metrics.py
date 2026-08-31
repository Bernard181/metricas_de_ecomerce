"""Rotas de consulta de métricas."""

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.schemas import MetricsSummaryResponse, RevenuePointResponse
from app.application.sales import revenue_series, sales_summary
from app.infrastructure.database import get_session

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get("/summary", response_model=MetricsSummaryResponse)
def get_summary(
    start: datetime | None = Query(default=None),
    end: datetime | None = Query(default=None),
    session: Session = Depends(get_session),
) -> MetricsSummaryResponse:
    """Retorna os KPIs de vendas no intervalo informado."""
    if start and end and start > end:
        raise HTTPException(status_code=422, detail="start deve ser anterior a end")
    result = sales_summary(session, start, end)
    return MetricsSummaryResponse(
        revenue=result.revenue,
        orders=result.orders,
        average_ticket=result.average_ticket,
    )


@router.get("/revenue-series", response_model=list[RevenuePointResponse])
def get_revenue_series(session: Session = Depends(get_session)) -> list[RevenuePointResponse]:
    """Retorna receita diária, atualizada após cada ingestão."""
    return [RevenuePointResponse(date=date, revenue=revenue) for date, revenue in revenue_series(session)]
