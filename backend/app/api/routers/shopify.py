"""Webhook Shopify para pedidos criados/pagos."""

import base64
import hashlib
import hmac
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.application.sales import save_sale
from app.config import settings
from app.infrastructure.database import get_session

router = APIRouter(prefix="/webhooks/shopify", tags=["shopify"])


def is_valid_shopify_hmac(payload: bytes, received_hmac: str, secret: str) -> bool:
    """Confere a assinatura HMAC enviada pela Shopify, sem expor o segredo."""
    if not secret or not received_hmac:
        return False
    digest = base64.b64encode(hmac.new(secret.encode(), payload, hashlib.sha256).digest()).decode()
    return hmac.compare_digest(digest, received_hmac)


@router.post("/orders", status_code=202)
async def receive_shopify_order(
    request: Request, session: Session = Depends(get_session)
) -> dict[str, bool]:
    """Normaliza um pedido Shopify após validar a assinatura do webhook."""
    payload = await request.body()
    received_hmac = request.headers.get("X-Shopify-Hmac-Sha256", "")
    if not is_valid_shopify_hmac(payload, received_hmac, settings.shopify_webhook_secret):
        raise HTTPException(status_code=401, detail="Assinatura Shopify inválida")
    try:
        order: dict[str, Any] = await request.json()
        external_id = str(order["id"])
        occurred_at = datetime.fromisoformat(str(order["created_at"]).replace("Z", "+00:00"))
        total = Decimal(str(order["total_price"]))
        currency = str(order["currency"])
        if total < 0 or len(currency) != 3:
            raise ValueError("campos de pedido inválidos")
    except (KeyError, ValueError, InvalidOperation) as error:
        raise HTTPException(status_code=422, detail="Payload Shopify inválido") from error
    created = save_sale(
        session,
        source="shopify",
        external_id=external_id,
        occurred_at=occurred_at,
        total=total,
        currency=currency,
    )
    return {"accepted": True, "created": created}
