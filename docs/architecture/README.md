# Arquitetura

Esta seção documenta a arquitetura do CloudOps.

## Visão geral

> Nota: esta seção será preenchida conforme a arquitetura da plataforma for definida.

O projeto deverá separar as seguintes camadas (ver `AGENTS.md`):

- API
- domínio
- regras de negócio
- serviços
- persistência
- infraestrutura

## Fluxo principal

```
        FONTES DE DADOS
              │
              ▼
     ┌─────────────────┐
     │    CloudOps     │
     │   Data Layer    │
     └────────┬────────┘
              │
              ▼
        PROCESSAMENTO
              │
              ▼
     ┌─────────────────┐
     │  MÉTRICAS       │
     │  INSIGHTS       │
     │  ALERTAS        │
     └────────┬────────┘
              │
              ▼
         DECISÕES
```

## Documentos

- Documentos de arquitetura detalhados serão adicionados aqui conforme forem criados.
