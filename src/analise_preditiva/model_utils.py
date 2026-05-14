from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor


def treinar_regressao_linear(X_train, y_train) -> LinearRegression:
    """Treina um modelo de regressao linear."""
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    return modelo


def treinar_arvore_decisao(
    X_train,
    y_train,
    random_state: int = 42,
) -> DecisionTreeRegressor:
    """Treina um modelo DecisionTreeRegressor."""
    modelo = DecisionTreeRegressor(random_state=random_state)
    modelo.fit(X_train, y_train)
    return modelo


def avaliar_modelo_regressao(y_true, y_pred) -> dict[str, float]:
    """Calcula metricas basicas para regressao."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred) ** 0.5
    r2 = r2_score(y_true, y_pred)

    return {
        "mae": mae,
        "rmse": rmse,
        "r2": r2,
    }
