# Auditoria do Projeto — CloudOps

> **Data:** 30 de agosto de 2026  
> **Escopo:** auditoria estática do repositório. Nenhum código de produto foi criado ou alterado.

## 1. Executive Summary

O repositório é uma fundação documental bem organizada, não uma aplicação em funcionamento. A visão do produto, a arquitetura-alvo, quatro ADRs e regras de engenharia estão definidos; `backend/`, `frontend/` e `tests/` contêm apenas arquivos de preservação/README. Portanto, não há fluxo executável de entrada de dados, persistência, cálculo de métricas, interface ou alertas.

O menor MVP demonstrável deve validar uma única proposta de valor: importar vendas por CSV, normalizá-las, calcular receita/pedidos/ticket médio para um período e exibi-los em um dashboard. Integrações externas, autenticação completa, Redis, workers, alertas enviados e insights automatizados ficam fora desse primeiro corte.

## 2. Current Architecture

A arquitetura existente é **proposta**, não implementada. Ela define um monólito modular com dependências para dentro:

`API REST (FastAPI) → aplicação → domínio puro → ports/adapters de infraestrutura`.

O estado-alvo prevê PostgreSQL como fonte de verdade, Redis para fila/cache, connectors por fonte, engine de métricas, SPA React e observabilidade. As decisões registradas — monólito modular, REST, secrets fora do código e backend Python — ainda estão com status **Proposta**.

## 3. Repository Structure

| Área | Estado observado | Função |
|---|---|---|
| `README.md` | Documentação | proposta de valor, problema e visão geral. |
| `AGENTS.md` | Documentação normativa | regras de arquitetura, qualidade, segurança e Git. |
| `docs/architecture/` | Documentação | arquitetura-alvo de backend, API, dados, integrações, frontend e infraestrutura. |
| `docs/decisions/` | Documentação | ADRs 0001–0004. |
| `docs/research/` | Documentação | pesquisa de KPIs, stack e contexto original. |
| `backend/` | Vazio além de README e `.gitkeep` | nenhum projeto Python, app, dependência ou migração. |
| `frontend/` | Apenas `.gitkeep` | nenhuma SPA, build ou componentes. |
| `tests/` | Apenas `.gitkeep` | nenhum teste. |
| `.github/` | Parcial | templates de Issue/PR e CI estrutural. |

## 4. Technology Stack

As tecnologias são intenções documentadas: Python 3.12+, FastAPI, Pydantic v2, SQLAlchemy 2, Alembic, PostgreSQL, Redis, pytest e ruff no backend; React, TypeScript, Vite, TanStack Query, Zustand e biblioteca de gráficos no frontend. Não há `pyproject.toml`, `package.json`, Dockerfile, Compose ou lockfile que materialize essa stack.

## 5. Data Flow

**Fluxo real atual:** não existe execução nem dados.

**Fluxo arquitetural previsto:** fonte (webhook, polling ou arquivo) → connector/normalização → deduplicação e fila → persistência de eventos operacionais → regras puras de métricas → API REST → dashboard; alertas e insights consomem as métricas. Para o MVP, a importação CSV síncrona substitui connector externo e fila, reduzindo o caminho crítico.

## 6. Current Features

- Visão, posicionamento e público-alvo potencial documentados para e-commerce e negócios digitais.
- Princípios de arquitetura e desenvolvimento definidos.
- Contrato REST e modelos conceituais de dados/KPIs documentados.
- Templates de Issue/PR e workflow CI que apenas valida a existência de pastas.

Não há funcionalidade de usuário entregue, API acessível, banco de dados, autenticação, cálculo, dashboard ou integração.

## 7. Missing Features

### P0 — necessário para o MVP

| Feature | Problema resolvido | Valor | Dependências | Complexidade | Risco |
|---|---|---|---|---|---|
| Fundação executável do backend | não há serviço executável | viabiliza o produto | decisões existentes | Baixa | Baixo |
| Persistência de vendas e importação CSV | dados de vendas não entram | centraliza uma fonte de dados demonstrável | fundação/backend | Média | Médio |
| KPIs de receita, pedidos e ticket médio | não há leitura operacional | visão imediata do desempenho | vendas persistidas | Baixa | Baixo |
| API de métricas | dashboard não tem contrato executável | consumo estável dos KPIs | engine de métricas | Baixa | Baixo |
| Dashboard de resumo | dados não são apresentados | demonstra valor ao gestor | API de métricas | Média | Baixo |

### P1 — importante para lançamento

- Autenticação e isolamento por organização.
- Integração real com uma fonte escolhida pelo negócio e processamento assíncrono.
- Séries temporais, filtros e estados de importação.
- Regras de alerta exibidas no produto.

### P2 — evolução posterior

- Notificações por e-mail/webhook com deduplicação e cooldown.
- Insights comparativos automatizados.
- Conectores para ads, estoque e financeiro; polling; cache Redis.

### P3 — ideias futuras

- Motor avançado de recomendações e análises preditivas.
- Escala analítica com TimescaleDB/ClickHouse, se o volume justificar.

## 8. Technical Debt

| Severidade | Achado | Evidência/impacto |
|---|---|---|
| **Alto** | Documentação descreve componentes inexistentes como se fossem operacionais. | `backend/README.md` traz comandos que falham porque não há `pyproject.toml`, `app/`, Alembic ou `.env.example`; pode induzir desenvolvimento incorreto. |
| **Alto** | A arquitetura proposta inclui complexidade antes da validação. | Redis, workers, circuit breaker, DLQ, JWT, rate limiting, tracing e múltiplas fontes não são necessários para validar o primeiro fluxo CSV. |
| **Médio** | Decisões fundamentais permanecem como “Proposta”. | ADRs não formalizam aceitação; o primeiro ciclo deve confirmar o corte de MVP sem abrir nova arquitetura. |
| **Médio** | KPIs são pesquisa, sem contrato de negócio fechado. | Fórmulas de receita, pedidos e ticket são indicadas, mas precisam de regras explícitas para dados inválidos, moeda e período. |
| **Baixo** | CI é somente um placeholder. | Valida diretórios, mas não qualidade, testes nem builds. |

Não foi encontrado código implementado para avaliar duplicação, acoplamento, gargalos ou necessidade de refatoração. Logo, não há refatoração justificada neste momento.

## 9. Security Concerns

- **Alto:** não existe mecanismo efetivo de validação, autenticação, autorização, segredo ou isolamento de dados; isto é esperado pela ausência de aplicação, mas impede exposição pública.
- **Médio:** a documentação prevê importações e integrações sem ainda definir limites de arquivo, validação de CSV, retenção de dados, isolamento por organização ou política de PII.
- **Baixo:** não há secrets versionados encontrados nesta auditoria. A decisão de usar ambiente/secret manager é adequada e reutilizável.

Para o MVP local/demonstrável, a API não deve ser publicada sem autenticação. Validação de payload e limites de importação são requisitos do primeiro fluxo.

## 10. Testing Status

Não há testes, framework configurado nem comando executável de teste. O CI atual não testa código. Cada Issue de implementação deve acrescentar os testes da unidade criada; prioridade: cálculos puros, importação e endpoint de métricas.

## 11. Product Analysis

**Proposta percebida:** oferecer a gestores uma visão centralizada de operações que hoje estão dispersas em plataformas de vendas e outras fontes.

**Fluxo MVP proposto:** gestor importa um CSV de vendas → CloudOps valida e persiste os registros → sistema calcula três KPIs para o período → gestor vê o resumo no dashboard.

**Usuários e casos de uso (HIPÓTESE):** gestores de pequenas operações de e-commerce e produtos digitais que consolidam vendas manualmente e precisam acompanhar receita, pedidos e ticket médio. Não há pesquisa de usuários ou definição de fonte concreta no repositório que confirme essa hipótese.

## 12. Recommended Features

O MVP deve restringir-se a uma organização de demonstração, uma fonte CSV e três KPIs. Esse recorte prova a cadeia “fonte → dados normalizados → métricas → dashboard” sem dependência de credenciais externas ou infraestrutura assíncrona. A primeira fonte externa, alertas e autenticação devem ser decididos após a demonstração.

## 13. Priorities

1. Tornar o backend e a persistência executáveis.
2. Importar uma fonte simples e validada (CSV).
3. Calcular e expor os três KPIs de vendas.
4. Exibir o resultado em um dashboard mínimo.
5. Automatizar testes e CI do que foi entregue.

## 14. Roadmap

### Fase 1 — Fundação

Estruturar projeto FastAPI, configuração segura, banco local, migrações, health check, testes e CI de backend.

### Fase 2 — MVP

Modelar vendas, importar CSV idempotentemente, calcular receita/pedidos/ticket médio, expor API e construir dashboard de resumo.

### Fase 3 — Produto utilizável

Adicionar período/filtros, série temporal, autenticação e isolamento por organização, além de uma integração real selecionada.

### Fase 4 — Pré-lançamento

Adicionar observabilidade, backups, limites, revisão de segurança, ambiente de staging e regras de alerta no produto.

### Fase 5 — Pós-lançamento

Evoluir conectores, notificações, insights e escala analítica conforme uso e volume observados.

## 15. Recommended Next Step

Validar o backlog de Issues do MVP e, após aprovação, implementar as Issues em ordem em uma branch `feature/`, sem antecipar Redis, filas, conectores externos, alertas enviados ou autenticação completa.
