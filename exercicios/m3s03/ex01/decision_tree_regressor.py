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
)


def main() -> None:
    base = carregar_base()
    X, y = separar_xy(base)
    X_train, X_test, y_train, y_test = dividir_treino_teste(X, y)

    modelo = treinar_arvore_decisao(X_train, y_train)
    y_pred = modelo.predict(X_test)
    metricas = avaliar_modelo_regressao(y_test, y_pred)

    print("Exercício M3S03 - Ex01")
    print()
    print("Modelo treinado: DecisionTreeRegressor")
    print(f"Profundidade da árvore: {modelo.get_depth()}")
    print(f"Número de folhas: {modelo.get_n_leaves()}")
    print()
    print(f"MAE: {metricas['mae']:.4f}")
    print(f"RMSE: {metricas['rmse']:.4f}")
    print(f"R2: {metricas['r2']:.4f}")


if __name__ == "__main__":
    main()
