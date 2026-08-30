# Decisão 0003: Configuração e secrets fora do código

- **Data:** 2026-08-30
- **Status:** Proposta

## Contexto

O CloudOps conecta-se a muitas fontes externas, cada uma com credenciais próprias. Secrets versionados no Git são um risco de segurança grave e dificultam rotacionar credenciais.

## Decisão

Toda configuração e credencial vem de **variáveis de ambiente**, tipadas com `pydantic-settings` no backend. Apenas um `.env.example` (sem valores reais) é versionado. Em produção, secrets ficam em **secret manager** do provedor.

## Consequências

- **Positivas:** secrets nunca entram no repositório; rotação sem deploy; portabilidade entre ambientes.
- **Negativas:** exige disciplina ao configurar novos serviços/ambientes.

## Alternativas consideradas

- Secrets em arquivos de config versionados (rejeitado — risco).
- Banco de dados para configuração (complexidade antecipada).
