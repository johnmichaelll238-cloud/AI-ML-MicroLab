import pandas as pd

def load_passwords():
    df = pd.read_csv("datasets/passwords.csv")
    return df