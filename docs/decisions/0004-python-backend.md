# Decisão 0004: Python como linguagem do backend

- **Data:** 2026-08-30
- **Status:** Proposta

## Contexto

O backend do CloudOps fará forte processamento de dados e análise (métricas), além de expor uma API. É necessário escolher uma linguagem que maximize a produtividade do time/agente e se beneficie do ecossistema de dados.

## Decisão

Usar **Python 3.12+** no backend, com **FastAPI** (web), **Pydantic** (validação/schemas), **SQLAlchemy + Alembic** (banco/migrações) e **pytest** (testes). Todo código deve ser **comentado e tipado** para melhor legibilidade e manutenção.

## Consequências

- **Positivas:** ecossistema forte de dados/análise (`pandas`, `numpy`), legibilidade, rápida iteração, ótima integração com LLM/agentes (o que favorece a produtividade do agente desenvolvedor).
- **Negativas:** performance de CPU inferior a linguagens compiladas para cargas extremas; custo de atenção com tipagem e performance em hot paths (mitigável com camadas adequadas).

## Alternativas consideradas

- Node.js/TypeScript + NestJS.
- Go.
- Java/Spring Boot.
