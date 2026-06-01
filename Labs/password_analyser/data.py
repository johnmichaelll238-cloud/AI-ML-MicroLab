import pandas as pd

def load_passwords():
    try:
        df = pd.read_csv("datasets/passwords.csv")
        if "password" not in df.columns:
            print("[ERROR] CSV must contain a 'password' column.")
            return None

        if df.empty:
            print("[ERROR] CSV contains no data.")
            return None

        return df
    except FileNotFoundError:
        print("[ERROR] passwords.csv not found.")
        return None

    except pd.errors.EmptyDataError:
        print("[ERROR] passwords.csv is empty.")
        return None