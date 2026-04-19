import pandas as pd


def inventory_optimization(df, forecast_results):
    """
    Calculate safety stock and reorder recommendations
    """

    print("\nRunning inventory optimization...")

    avg_sales = df.groupby("Dept")["Weekly_Sales"].mean().reset_index()
    avg_sales.columns = ["Dept", "Average_Sales"]

    avg_sales["Safety_Stock"] = avg_sales["Average_Sales"] * 0.20
    avg_sales["Reorder_Point"] = (
        avg_sales["Average_Sales"] + avg_sales["Safety_Stock"]
    )

    # Simulated current stock
    avg_sales["Current_Stock"] = avg_sales["Average_Sales"] * 0.80

    avg_sales["Reorder_Required"] = avg_sales.apply(
        lambda row: "YES"
        if row["Current_Stock"] < row["Reorder_Point"]
        else "NO",
        axis=1
    )

    print("Inventory optimization completed.")

    return avg_sales
