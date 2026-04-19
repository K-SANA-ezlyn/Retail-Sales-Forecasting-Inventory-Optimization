import pandas as pd
from config import TRAIN_FILE, FEATURES_FILE, STORES_FILE


def load_data():
    """
    Load all required CSV files
    """

    print("Loading datasets...")

    train_df = pd.read_csv(TRAIN_FILE)
    features_df = pd.read_csv(FEATURES_FILE)
    stores_df = pd.read_csv(STORES_FILE)

    print("Datasets loaded successfully.\n")

    print("Train Shape:", train_df.shape)
    print("Features Shape:", features_df.shape)
    print("Stores Shape:", stores_df.shape)

    return train_df, features_df, stores_df
