"""Testes de segurança do webhook Shopify."""

import base64
import hashlib
import hmac

from app.api.routers.shopify import is_valid_shopify_hmac


def test_validates_shopify_hmac() -> None:
    """Aceita somente a assinatura criada com o segredo correto."""
    payload = b'{"id": 1}'
    secret = "test-secret"
    signature = base64.b64encode(
        hmac.new(secret.encode(), payload, hashlib.sha256).digest()
    ).decode()
    assert is_valid_shopify_hmac(payload, signature, secret)
    assert not is_valid_shopify_hmac(payload, signature, "other-secret")
