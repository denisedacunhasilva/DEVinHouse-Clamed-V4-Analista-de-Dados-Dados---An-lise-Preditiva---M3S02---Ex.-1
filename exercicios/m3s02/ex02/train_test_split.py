from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.analise_preditiva import carregar_base, dividir_treino_teste, separar_xy


def main() -> None:
    base = carregar_base()
    X, y = separar_xy(base)
    X_train, X_test, y_train, y_test = dividir_treino_teste(X, y)

    print("Exercicio M3S02 - Ex02")
    print()
    print(f"Formato de X_train: {X_train.shape}")
    print(f"Formato de X_test: {X_test.shape}")
    print(f"Formato de y_train: {y_train.shape}")
    print(f"Formato de y_test: {y_test.shape}")


if __name__ == "__main__":
    main()
