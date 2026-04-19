def create_features(df):
    """
    Create useful ML features
    """

    print("\nCreating features...")

    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Week"] = df["Date"].dt.isocalendar().week.astype(int)
    df["Day"] = df["Date"].dt.day
    df["DayOfWeek"] = df["Date"].dt.dayofweek

    # Weekend flag
    df["IsWeekend"] = df["DayOfWeek"].apply(
        lambda x: 1 if x >= 5 else 0
    )

    print("Feature engineering completed.")

    return df
