import pandas as pd


def get_customer(customer_id: str):

    df = pd.read_csv("data/customers.csv")

    customer = df[
        df["customer_id"] == customer_id
    ]

    return customer.to_dict(
        orient="records"
    )