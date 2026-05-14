from src.analise_preditiva import (
    carregar_base,
    dividir_treino_teste,
    separar_xy,
)


def main() -> None:
    """Executa um fluxo rapido de leitura da base e divisao treino/teste."""
    base = carregar_base()
    X, y = separar_xy(base)
    X_train, X_test, y_train, y_test = dividir_treino_teste(X, y)

    print("Projeto de analise preditiva carregado com sucesso.")
    print()
    print(f"Total de linhas da base: {len(base)}")
    print(f"Formato de X: {X.shape}")
    print(f"Formato de y: {y.shape}")
    print()
    print(f"Formato de X_train: {X_train.shape}")
    print(f"Formato de X_test: {X_test.shape}")
    print(f"Formato de y_train: {y_train.shape}")
    print(f"Formato de y_test: {y_test.shape}")


if __name__ == "__main__":
    main()
