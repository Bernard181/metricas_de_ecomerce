"""Ponto de entrada da API CloudOps."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import imports, metrics, shopify
from app.config import settings
from app.infrastructure.database import Base, engine


def create_app() -> FastAPI:
    """Monta a aplicação e registra os adaptadores HTTP."""
    app = FastAPI(title="CloudOps API", version="0.1.0")
    origins = [origin.strip() for origin in settings.cors_origins.split(",") if origin.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    def create_local_tables() -> None:
        """Cria tabelas somente para reduzir fricção na demonstração local."""
        Base.metadata.create_all(bind=engine)

    @app.get("/health", tags=["health"])
    def health() -> dict[str, str]:
        """Informa que a API está pronta para receber requisições."""
        return {"status": "ok"}

    app.include_router(imports.router, prefix="/api/v1")
    app.include_router(metrics.router, prefix="/api/v1")
    app.include_router(shopify.router, prefix="/api/v1")
    return app


app = create_app()
