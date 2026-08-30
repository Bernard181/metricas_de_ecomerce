# Decisão 0001: Monólito modular como estratégia inicial

- **Data:** 2026-08-30
- **Status:** Proposta

## Contexto

O CloudOps é uma plataforma nova que consolida múltiplas fontes externas (vendas, anúncios, estoque, financeiro). O escopo e o time são pequenos, e microserviços desde o início trariam complexidade operacional alta (rede, transações distribuídas, versionamento múltiplo) sem benefício claro.

## Decisão

Iniciar como **monólito modular**: um único deploy com fronteiras bem definidas por módulo/camada (API, aplicação, domínio, infraestrutura). Os módulos comunicam-se por interfaces claras, permitindo fatiar em serviços no futuro sem reescrita do domínio.

## Consequências

- **Positivas:** simplicidade de deploy e desenvolvimento; menos infraestrutura; transações mais fáceis; comunicação local.
- **Negativas:** capacidade de escala independente limitada; risco de acoplamento se as fronteiras dos módulos não forem respeitadas.

## Alternativas consideradas

- Microserviços desde o início.
- Serverless (funções).
