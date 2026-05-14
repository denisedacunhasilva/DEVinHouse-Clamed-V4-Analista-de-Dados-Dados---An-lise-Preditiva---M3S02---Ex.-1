from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.analise_preditiva import (
    avaliar_modelo_regressao,
    carregar_base,
    dividir_treino_teste,
    separar_xy,
    treinar_arvore_decisao,
    treinar_regressao_linear,
)


def main() -> None:
    base = carregar_base()
    X, y = separar_xy(base)
    X_train, X_test, y_train, y_test = dividir_treino_teste(X, y)

    modelos = {
        "Regressao Linear": treinar_regressao_linear(X_train, y_train),
        "Arvore de Decisao": treinar_arvore_decisao(X_train, y_train),
    }

    print("Exercicio M3S03 - Ex02")
    print()

    for nome, modelo in modelos.items():
        train_pred = modelo.predict(X_train)
        test_pred = modelo.predict(X_test)

        metricas_train = avaliar_modelo_regressao(y_train, train_pred)
        metricas_test = avaliar_modelo_regressao(y_test, test_pred)

        print(nome)
        print(f"  Treino - MAE: {metricas_train['mae']:.4f}")
        print(f"  Treino - RMSE: {metricas_train['rmse']:.4f}")
        print(f"  Treino - R2: {metricas_train['r2']:.4f}")
        print(f"  Teste  - MAE: {metricas_test['mae']:.4f}")
        print(f"  Teste  - RMSE: {metricas_test['rmse']:.4f}")
        print(f"  Teste  - R2: {metricas_test['r2']:.4f}")

        if nome == "Arvore de Decisao":
            print(f"  Profundidade: {modelo.get_depth()}")
            print(f"  Folhas: {modelo.get_n_leaves()}")

        print()


if __name__ == "__main__":
    main()
