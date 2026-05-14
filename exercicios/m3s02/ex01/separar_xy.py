from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.analise_preditiva import carregar_base, separar_xy


def main() -> None:
    base = carregar_base()
    X, y = separar_xy(base)

    print("Exercício M3S02 - Ex01")
    print()
    print("X (variáveis preditoras):")
    print(X.head())
    print()
    print("y (variável resposta):")
    print(y.head())
    print()
    print(f"Formato de X: {X.shape}")
    print(f"Formato de y: {y.shape}")


if __name__ == "__main__":
    main()
