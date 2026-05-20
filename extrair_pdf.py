"""Extrai texto bruto de PDF ignorando cor de fonte."""

import sys

from pdfminer.high_level import extract_text


def extrai(pdf_path: str) -> str:
    return extract_text(pdf_path)


if __name__ == "__main__":
    caminho = sys.argv[1] if len(sys.argv) > 1 else "peticao_envenenada.pdf"
    texto = extrai(caminho)
    print(f"=== texto extraido de {caminho} ({len(texto)} chars) ===")
    print(texto)
