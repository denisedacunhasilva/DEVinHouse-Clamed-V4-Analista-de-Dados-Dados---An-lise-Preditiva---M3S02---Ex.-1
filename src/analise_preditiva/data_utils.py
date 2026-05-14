from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from .config import RANDOM_STATE, TEST_SIZE

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "dados_AP.csv"
TARGET_COLUMN = "demanda"
PREDICTOR_COLUMNS = ["investimento_marketing", "preco_medicamento", "mes"]


def carregar_base(csv_path: Path = DATA_PATH) -> pd.DataFrame:
    """Carrega a base de dados do projeto."""
    return pd.read_csv(csv_path)


def separar_xy(
    df: pd.DataFrame,
    predictor_columns: list[str] = PREDICTOR_COLUMNS,
    target_column: str = TARGET_COLUMN,
) -> tuple[pd.DataFrame, pd.Series]:
    """Separa X (preditoras) e y (variável resposta)."""
    X = df[predictor_columns].copy()
    y = df[target_column].copy()
    return X, y


def dividir_treino_teste(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Divide os dados em 80% para treino e 20% para teste por padrão."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
