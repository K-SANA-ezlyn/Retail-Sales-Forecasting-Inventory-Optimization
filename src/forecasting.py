from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
from config import TEST_SIZE, RANDOM_STATE


def train_forecast_model(df):
    """
    Train Random Forest forecasting model
    """

    print("\nTraining forecasting model...")

    features = [
        "Store",
        "Dept",
        "IsHoliday",
        "Temperature",
        "Fuel_Price",
        "CPI",
        "Unemployment",
        "Size",
        "Year",
        "Month",
        "Week",
        "Day",
        "DayOfWeek",
        "IsWeekend"
    ]

    target = "Weekly_Sales"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=RANDOM_STATE
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5

    print(f"Model MAE: {mae:.2f}")
    print(f"Model RMSE: {rmse:.2f}")

    results = pd.DataFrame({
        "Actual": y_test,
        "Predicted": predictions
    })

    return model, results
