"""Configuração do ambiente Alembic para o CloudOps backend."""

from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
from app.config import settings
from app.infrastructure import models  # noqa: F401  (permite o autogenerate ver as tabelas)
from app.infrastructure.database import Base

# Objeto de configuração do Alembic, com acesso aos valores do arquivo .ini.
config = context.config

# Usa a mesma string de conexão da aplicação (env `DATABASE_URL` ou fallback).
config.set_main_option("sqlalchemy.url", settings.database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadados dos modelos registrados em `app.infrastructure.models`.
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Gera SQL sem exigir um banco conectado."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa migrações conectando ao banco configurado."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
