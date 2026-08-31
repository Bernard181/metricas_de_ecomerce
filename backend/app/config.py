"""Configuração segura, obtida exclusivamente do ambiente."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações necessárias para executar a API."""

    database_url: str = "sqlite:///./cloudops.db"
    shopify_webhook_secret: str = ""
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
