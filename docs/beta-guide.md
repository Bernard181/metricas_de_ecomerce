# Guia da beta CloudOps

## Demonstração local

1. No diretório `backend`, copie `.env.example` para `.env`.
2. Crie ambiente Python e instale `pip install -e ".[dev]"`.
3. Inicie a API com `uvicorn app.main:app --reload`.
4. Em `frontend`, execute `npm install` e `npm run dev`.

Envie um CSV UTF-8 para `POST /api/v1/imports/sales-csv`, com as colunas `external_id`, `occurred_at` (ISO-8601), `total` e `currency`.

## Shopify

Crie uma app personalizada, configure o webhook de pedidos para `POST https://SEU-DOMINIO/api/v1/webhooks/shopify/orders` e coloque o segredo de assinatura em `SHOPIFY_WEBHOOK_SECRET`. A API precisa estar em HTTPS. O webhook valida HMAC e evita duplicidade de pedidos.

Esta beta ainda não possui login, OAuth da Shopify, sincronização histórica nem isolamento por organização. Use uma loja de teste ou um único piloto autorizado; não a exponha como produto multiempresa antes dessas proteções.
