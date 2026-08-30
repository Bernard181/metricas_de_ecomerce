# ESTUDO: Avaliação da stack do backend

> **Status:** Feito — usado para fundamentar o [ADR-0004](../decisions/0004-python-backend.md).
> Data: 2026-08-30.

## Contexto

O backend processa dados heterogêneos e expõe métricas. Critérios: produtividade do time/agente, ecossistema de dados, manutenção, maturidade.

## Comparativo

| Critério | Python + FastAPI | Node/TS + NestJS | Go | Java/Spring |
|----------|------------------|------------------|----|-------------|
| Produtividade/legibilidade | Alta | Alta | Média | Média |
| Ecossistema de dados/análise | **Excelente** (`pandas`, `numpy`) | Médio | Baixo | Médio |
| Curva de aprendizado | Baixa | Média | Média | Alta |
| Performance bruta | Boa p/ uso típico | Boa | Alta | Alta |
| Tipagem estática | Type hints (opcional) | Forte (TS) | Forte | Forte |
| Documentação de API | OpenAPI automático (FastAPI) | Swagger (NestJS) | Manual | OpenAPI (SpringDoc) |

## Decisão

Adotar **Python + FastAPI**: melhor equilíbrio para um produto intensivo em dados/análise com time pequeno, favorecendo velocidade e iteração. Ver ADR-0004.

## Consequências

- Exigir **type hints** e **comentários** (ver [`architecture/backend.md`](../architecture/backend.md) §6) para manter clareza.
- Para cargas analíticas massivas, avaliar separadamente colunar (ex.: ClickHouse/TimescaleDB) no futuro.
