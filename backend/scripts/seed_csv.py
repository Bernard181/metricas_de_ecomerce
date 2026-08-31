"""Semeador de dados de demonstração a partir de um CSV de vendas.

Uso:
    python -m scripts.seed_csv docs/sample-sales.csv
"""

import sys
from pathlib import Path

from app.application.sales_csv import parse_and_import_csv
from app.infrastructure.database import SessionLocal
from app.shared.migrations import run_migrations


def main(argv: list[str]) -> int:
    """Carrega o CSV informado (relativo à raiz do repositório) no banco configurado."""
    if len(argv) != 1:
        print("Uso: python -m scripts.seed_csv <caminho-para-importar.csv>", file=sys.stderr)
        return 2

    csv_path = Path(argv[0]).resolve()
    if not csv_path.exists():
        print(f"Arquivo não encontrado: {csv_path}", file=sys.stderr)
        return 2

    run_migrations()

    with csv_path.open("rb") as handle:
        content = handle.read()

    with SessionLocal() as session:
        result = parse_and_import_csv(content, session)

    print(
        f"Importados: {result.imported} | Ignorados: {result.ignored} | "
        f"Inválidos: {result.invalid}"
    )
    for error in result.errors:
        print(error, file=sys.stderr)
    return 1 if result.invalid else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
