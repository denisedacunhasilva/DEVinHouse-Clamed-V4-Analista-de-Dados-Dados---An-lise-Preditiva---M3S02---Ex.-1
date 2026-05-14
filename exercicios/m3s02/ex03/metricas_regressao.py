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
    treinar_regressao_linear,
)


def main() -> None:
    base = carregar_base()
    X, y = separar_xy(base)
    X_train, X_test, y_train, y_test = dividir_treino_teste(X, y)

    modelo = treinar_regressao_linear(X_train, y_train)
    y_pred = modelo.predict(X_test)
    metricas = avaliar_modelo_regressao(y_test, y_pred)

    print("Exercício M3S02 - Ex03")
    print()
    print(f"MAE: {metricas['mae']:.4f}")
    print(f"RMSE: {metricas['rmse']:.4f}")
    print(f"R2: {metricas['r2']:.4f}")
    print()
    print("Coeficientes do modelo:")
    for nome_coluna, coeficiente in zip(X.columns, modelo.coef_):
        print(f"- {nome_coluna}: {coeficiente:.6f}")
    print(f"Intercepto: {modelo.intercept_:.6f}")


if __name__ == "__main__":
    main()
