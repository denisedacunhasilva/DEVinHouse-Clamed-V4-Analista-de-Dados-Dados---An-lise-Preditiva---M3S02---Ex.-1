from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "dados_AP.csv"
TARGET_COLUMN = "demanda"
PREDICTOR_COLUMNS = ["investimento_marketing", "preco_medicamento", "mes"]


def carregar_base(csv_path: Path = DATA_PATH) -> pd.DataFrame:
    """Carrega a base de dados a partir do arquivo CSV do projeto."""
    return pd.read_csv(csv_path)


def separar_xy(
    df: pd.DataFrame,
    predictor_columns: list[str] = PREDICTOR_COLUMNS,
    target_column: str = TARGET_COLUMN,
) -> tuple[pd.DataFrame, pd.Series]:
    """Separa X (preditoras) e y (variavel resposta)."""
    X = df[predictor_columns].copy()
    y = df[target_column].copy()
    return X, y


if __name__ == "__main__":
    base = carregar_base()
    X, y = separar_xy(base)

    print(f"Arquivo carregado: {DATA_PATH}")
    print()
    print("X (variaveis preditoras):")
    print(X.head())
    print()
    print("y (variavel resposta):")
    print(y.head())
    print()
    print(f"Formato de X: {X.shape}")
    print(f"Formato de y: {y.shape}")
