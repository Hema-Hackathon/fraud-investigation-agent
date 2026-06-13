import pandas as pd


def get_transactions(customer_id: str):

    df = pd.read_csv("data/transactions.csv")

    customer_transactions = df[
        df["customer_id"] == customer_id
    ]

    return customer_transactions.to_dict(
        orient="records"
    )