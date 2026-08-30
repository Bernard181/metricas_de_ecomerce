# Backend — CloudOps

> Backend **Python** da plataforma CloudOps.
> Documentação normativa: [`docs/architecture/backend.md`](../docs/architecture/backend.md).

## Stack

- **Python 3.12+**
- **FastAPI** + **Uvicorn**
- **Pydantic v2**
- **SQLAlchemy 2.x** + **Alembic**
- **PostgreSQL**
- **Redis** (+ fila RQ/ARQ)
- **pytest** / **ruff** / **mypy**

## Estrutura

```
backend/
├── pyproject.toml
├── alembic/                 # migrações
├── app/
│   ├── main.py              # app FastAPI + DI
│   ├── config.py            # settings (pydantic-settings)
│   ├── api/                 # routers, schemas, deps
│   ├── application/         # casos de uso / services
│   ├── domain/              # entidades, regras, ports
│   ├── integrations/        # connectors de fontes externas
│   ├── infrastructure/      # db, repos, fila, cache, http
│   └── shared/              # erros, logging, utils
└── tests/
```

Ver a estrutura completa e regras em [`docs/architecture/backend.md`](../docs/architecture/backend.md).

## Desenvolvimento local

1. Variáveis: copie `.env.example` para `.env` e preencha.
2. Crie o ambiente e instale dependências:

```bash
python -m venv .venv
# ative o venv (Windows: .venv\Scripts\activate; Linux/Mac: source .venv/bin/activate)
pip install -e ".[dev]"
```

3. Suba Postgres/Redis (docker-compose, se disponível).
4. Aplique migrações:

```bash
alembic upgrade head
```

5. Rode a API:

```bash
uvicorn app.main:app --reload
```

Documentação interativa: <http://localhost:8000/docs> (OpenAPI).

## Qualidade

```bash
ruff check .        # lint
ruff format .       # formatação
mypy app            # verificação de tipos
pytest              # testes
```

> **Importante:** todo código deve ser **comentado** (docstrings/intenção) e **tipado** — ver `../AGENTS.md` e `../docs/architecture/backend.md` §6.
