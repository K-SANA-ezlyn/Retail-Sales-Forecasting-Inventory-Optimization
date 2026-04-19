import pandas as pd


def preprocess_data(train_df, features_df, stores_df):
    """
    Merge and clean datasets
    """

    print("\nStarting preprocessing...")

    # Convert Date column
    train_df["Date"] = pd.to_datetime(train_df["Date"])
    features_df["Date"] = pd.to_datetime(features_df["Date"])

    # Merge datasets
    merged_df = pd.merge(
        train_df,
        features_df,
        on=["Store", "Date", "IsHoliday"],
        how="left"
    )

    merged_df = pd.merge(
        merged_df,
        stores_df,
        on="Store",
        how="left"
    )

    # Fill missing values
    merged_df.fillna(0, inplace=True)

    # Remove duplicates
    merged_df.drop_duplicates(inplace=True)

    print("Preprocessing completed.")
    print("Final Shape:", merged_df.shape)

    return merged_df
