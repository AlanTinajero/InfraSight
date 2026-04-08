import pandas as pd
import os

FILE = "history.csv"

def save_data(df):
    if os.path.exists(FILE):
        df.to_csv(FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(FILE, index=False)

def load_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    return pd.DataFrame()
