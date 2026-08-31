"""Execução das migrações Alembic de forma reutilizável (API e scripts)."""

from pathlib import Path

from alembic.config import Config

from alembic import command


def run_migrations() -> None:
    """Aplica as migrações Alembic pendentes para o banco configurado."""
    backend_root = Path(__file__).resolve().parent.parent.parent
    config = Config(str(backend_root / "alembic.ini"))
    command.upgrade(config, "head")
