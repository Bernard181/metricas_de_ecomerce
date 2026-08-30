# Arquitetura

Esta seção documenta a arquitetura do CloudOps — a referência técnica para quem desenvolve o sistema.

## Índice de documentos

| Documento | Descrição |
|-----------|-----------|
| [Visão Geral](overview.md) | Arquitetura estratégica, princípios e fluxo de dados. Leia primeiro. |
| [Backend](backend.md) | Regras técnicas **Python** (FastAPI, camadas, estrutura, comentários). |
| [API e Contratos](api.md) | Design REST, versionamento, erros, autenticação. |
| [Integrações](integrations.md) | Como conectar fontes externas (webhook/polling, resiliência). |
| [Camada de Dados e Métricas](data-layer.md) | Modelo de dados, engine de métricas, insights e alertas. |
| [Frontend](frontend.md) | Arquitetura do dashboard (React SPA). |
| [Infraestrutura](infrastructure.md) | CI/CD, deploy, observabilidade e segurança. |

## Regras transversais

- Backend em **Python**; código **comentado** e tipado (ver `backend.md` §6).
- Camadas: API → Aplicação → Domínio → Infraestrutura.
- Regras de negócio nunca dependem de frameworks.
- Toda alteração arquitetural relevante documentada aqui e/ou como ADR (`../decisions/`).

## Decisões registradas

Ver [ADR em `docs/decisions/`](../decisions/README.md).
