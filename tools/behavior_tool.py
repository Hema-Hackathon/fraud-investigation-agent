import pandas as pd


def get_behavior(customer_id: str):

    df = pd.read_csv("data/behaviors.csv")

    behavior = df[
        df["customer_id"] == customer_id
    ]

    return behavior.to_dict(
        orient="records"
    )