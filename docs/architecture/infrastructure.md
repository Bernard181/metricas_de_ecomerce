# Infraestrutura, Implantação e Observabilidade

> Define **como o CloudOps é executado em produção**, o pipeline de CI/CD e como o sistema é observado.

## 1. Modelo de implantação

- **Backend Python (FastAPI)** — serviço web (containers Docker).
- **Frontend (SPA)** — build estático servido por CDN/reverse proxy.
- **PostgreSQL** — banco de dados gerenciado.
- **Redis** — fila e cache.
- **Workers** — processos de fila (RQ/ARQ) para ingestão/processamento assíncrono.

```mermaid
flowchart LR
    subgraph Net["Rede"]
        LB[Load Balancer / Reverse Proxy]
    end
    subgraph Web["Serviços web"]
        API[FastAPI app]
        SPA[Frontend estático]
        WK[Workers (fila)]
    end
    subgraph Data["Dados"]
        PG[(PostgreSQL)]
        RD[(Redis)]
    end

    LB --> API
    LB --> SPA
    API --> PG
    API --> RD
    WK --> PG
    WK --> RD
```

## 2. Containerização

- **Dockerfile** por serviço (backend, worker; o frontend vira imagem estática com nginx).
- Images **imutáveis**: a mesma imagem deu build → vai para todos os ambientes.
- `docker-compose.yml` para ambiente local de desenvolvimento (API + Postgres + Redis + worker).
- Multi-arquitetura e versões pinadas têm prioridade.

## 3. CI/CD (GitHub Actions)

Pipeline já esboçado em `.github/workflows/ci.yml`. Expandir conforme o código:

| Etapa | Ação |
|-------|------|
| **Lint e format** | `ruff check` + `ruff format --check` (backend). |
| **Tipos** | `mypy` (se adotado). |
| **Testes** | `pytest` (unit + integration) com serviços de teste (Postgres/Redis). |
| **Build** | Build das imagens Docker. |
| **Deploy** | Push para registry + deploy no ambiente nas branches `main`/`release`. |

Fluxo de PR: toda alteração dispara lint + testes antes do merge.

## 4. Variáveis de ambiente / configuração

- Config via variáveis de ambiente, tipadas com `pydantic-settings` (backend).
- `.env.example` versionado com valores de exemplo; **secrets nunca versionados** (ver [ADR-0003](../decisions/0003-secure-config-and-secrets.md)).
- Em produção: secrets em **secret manager** do provedor (ex.: AWS Secrets Manager / Docker secrets), não no código.

## 5. Observabilidade

Tudo que acontece no sistema deve ser mensurável:

- **Logs estruturados (JSON)** — cada requisição logada com `request_id`.
- **Métricas de aplicação** — instrumentar com **Prometheus**-compatível (`prometheus-client`) ou OpenTelemetry.
- **Tracing distribuído** — OpenTelemetry para rastrear ingestão → processamento.
- **Dashboards e alertas de sistema** — métricas de saúde: latência, taxa de erro, filas atrasadas, uso de banco.

Indicadores de saúde essenciais:

- Latência da API (p95).
- Taxa de erro HTTP (5xx).
- Tamanho/idade da fila (backlog).
- Sucesso de integrações/connectors por fonte.
- Uptime de serviços.

## 6. Segurança em produção

- HTTPS obrigatório em todo o tráfego.
- Secrets fora do código; rotação suportada.
- Mínimo privilégio no acesso ao banco e serviços.
- Backups automáticos do PostgreSQL.
- Rate limiting na API pública (ver [api.md](api.md)).
- Revisão de dependências (SAST/Dependabot) no fluxo CI.

## 7. Ambientes

- **development** — local (docker-compose).
- **staging** — réplica próxima de produção para validar PRs.
- **production** — ambiente real; deploys apenas a partir de `main` aprovado.

## 8. Documentos relacionados

- [Visão Geral](overview.md) — componentes do sistema.
- [Backend](backend.md) — serviço web e worker.
- [API](api.md) — rate limiting e contratos.
- [Segurança](../decisions/0003-secure-config-and-secrets.md) — secrets/config.
