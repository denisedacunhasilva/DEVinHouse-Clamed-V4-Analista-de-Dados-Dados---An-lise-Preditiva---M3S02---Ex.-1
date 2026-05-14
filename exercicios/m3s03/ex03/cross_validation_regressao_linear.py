from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.analise_preditiva import (
    CV_FOLDS,
    RANDOM_STATE,
    carregar_base,
    separar_xy,
    validar_regressao_linear_cv,
)


def formatar_scores(scores) -> str:
    return ", ".join(f"{score:.4f}" for score in scores)


def main() -> None:
    base = carregar_base()
    X, y = separar_xy(base)
    resultado = validar_regressao_linear_cv(X, y, cv=CV_FOLDS, random_state=RANDOM_STATE)

    print("Exercicio M3S03 - Ex03")
    print()
    print(
        f"Regressao Linear com validacao cruzada ({CV_FOLDS} folds, "
        f"random_state={RANDOM_STATE})"
    )
    print()
    print(f"R2 por fold: {formatar_scores(resultado['r2_scores'])}")
    print(f"R2 medio: {resultado['r2_mean']:.4f}")
    print(f"Desvio padrao R2: {resultado['r2_std']:.4f}")
    print()
    print(f"MAE por fold: {formatar_scores(resultado['mae_scores'])}")
    print(f"MAE medio: {resultado['mae_mean']:.4f}")
    print(f"Desvio padrao MAE: {resultado['mae_std']:.4f}")
    print()
    print(f"RMSE por fold: {formatar_scores(resultado['rmse_scores'])}")
    print(f"RMSE medio: {resultado['rmse_mean']:.4f}")
    print(f"Desvio padrao RMSE: {resultado['rmse_std']:.4f}")


if __name__ == "__main__":
    main()
