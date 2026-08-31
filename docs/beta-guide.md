# Guia da beta CloudOps

## Demonstração local

### Backend (FastAPI + Alembic + SQLite/PostgreSQL)

1. No diretório `backend`, copie `.env.example` para `.env` (opcional; há valores padrão).
2. Crie o ambiente Python e instale: `pip install -e ".[dev]"`.
3. A API aplica as **migrações Alembic** automaticamente no boot (criação das tabelas). Ainda assim, você pode rodar manualmente:
   ```bash
   alembic upgrade head
   ```
4. Inicie a API: `uvicorn app.main:app --reload` (porta `8000` por padrão).

### Frontend (Vite/React)

Em `frontend`:
```bash
npm install
npm run dev
```
Acesse `http://localhost:5173`.

### Carregar dados de demonstração

Use o **seed script** para semear o CSV de exemplo (rodar migrations + importar de forma idempotente):
```bash
python -m scripts.seed_csv ../docs/sample-sales.csv
```
Ou envie um CSV UTF-8 para `POST /api/v1/imports/sales-csv` com as colunas `external_id`, `occurred_at` (ISO-8601), `total` e `currency`.

## Execução em contêiner (PostgreSQL + API)

Com Docker:
```bash
docker compose up --build
```
- `database`: PostgreSQL 16 (healthcheck).
- `api`: backend construído com o `backend/Dockerfile`, que roda `alembic upgrade head` e depois `uvicorn` na porta `8000`, apontando para o PostgreSQL via `DATABASE_URL`.

Aponte o frontend local para `http://localhost:8000` (default) usando CORS já configurado para `http://localhost:5173`.

## CI (GitHub Actions)

O workflow `.github/workflows/ci.yml` roda a cada push/PR:

- **backend**: `ruff check .` + `pytest -q`.
- **frontend**: `tsc -b && vite build`.

## PostgreSQL (ambiente de teste/produção)

Por padrão a aplicação usa SQLite (dev). Para usar PostgreSQL, defina a variável `DATABASE_URL` antes de iniciar, por exemplo:
```
DATABASE_URL=postgresql+psycopg://cloudops:SEGredo@localhost:5432/cloudops
```

## Shopify

Crie uma app personalizada, configure o webhook de pedidos para `POST https://SEU-DOMINIO/api/v1/webhooks/shopify/orders` e coloque o segredo de assinatura em `SHOPIFY_WEBHOOK_SECRET`. A API precisa estar em HTTPS. O webhook valida HMAC e evita duplicidade de pedidos.

Esta beta ainda não possui login, OAuth da Shopify, sincronização histórica nem isolamento por organização. Use uma loja de teste ou um único piloto autorizado; não a exponha como produto multiempresa antes dessas proteções.
