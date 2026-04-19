from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.forecasting import train_forecast_model
from src.inventory import inventory_optimization
from src.visualization import sales_trend_chart

import os
from config import PREDICTIONS_PATH


def main():
    print("RETAIL SALES FORECASTING PROJECT STARTED\n")

    # Step 1
    train_df, features_df, stores_df = load_data()

    # Step 2
    df = preprocess_data(
        train_df,
        features_df,
        stores_df
    )

    # Step 3
    df = create_features(df)

    # Step 4
    model, forecast_results = train_forecast_model(df)

    # Step 5
    inventory_results = inventory_optimization(
        df,
        forecast_results
    )

    # Step 6
    sales_trend_chart(df)

    # Save outputs
    os.makedirs(PREDICTIONS_PATH, exist_ok=True)

    forecast_results.to_csv(
        os.path.join(
            PREDICTIONS_PATH,
            "forecast_results.csv"
        ),
        index=False
    )

    inventory_results.to_csv(
        os.path.join(
            PREDICTIONS_PATH,
            "inventory_recommendations.csv"
        ),
        index=False
    )

    print("\nProject completed successfully.")
    print("Outputs saved in outputs folder.")


if __name__ == "__main__":
    main()
