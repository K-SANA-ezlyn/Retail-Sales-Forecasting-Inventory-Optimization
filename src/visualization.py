import matplotlib.pyplot as plt
import os
from config import CHARTS_PATH


def sales_trend_chart(df):
    """
    Generate sales trend chart
    """

    print("\nGenerating charts...")

    sales_trend = df.groupby("Date")["Weekly_Sales"].sum()

    plt.figure(figsize=(12, 6))
    sales_trend.plot()

    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Weekly Sales")

    os.makedirs(CHARTS_PATH, exist_ok=True)

    file_path = os.path.join(CHARTS_PATH, "sales_trend.png")
    plt.savefig(file_path)
    plt.close()

    print("Chart saved:", file_path)
