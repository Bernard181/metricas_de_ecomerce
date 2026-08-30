# Decisão 0002: API REST versionada como contrato público

- **Data:** 2026-08-30
- **Status:** Proposta

## Contexto

O CloudOps precisa expor métricas e dados para o dashboard e, potencialmente, para clientes externos. É necessário um contrato estável, versionado e consumível.

## Decisão

Usar **API REST** em **JSON**, com prefixo de versão `/api/v{n}`, documentada por **OpenAPI** (gerada automaticamente pelo FastAPI). Adotar erros padronizados, autenticação JWT e paginação por cursor.

## Consequências

- **Positivas:** ampla compatibilidade, contratos explícitos, ferramentas maduras, geração automática de documentação e tipos.
- **Negativas:** necessidade de versionamento disciplinado para evitar quebras; REST não é ideal para notificações em tempo real (usar websockets/filas quando necessário).

## Alternativas consideradas

- GraphQL.
- gRPC.
- Mensageria como interface primária.
