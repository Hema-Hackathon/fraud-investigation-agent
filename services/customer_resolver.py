import pandas as pd


def resolve_customer(query: str):

    customers = pd.read_csv(
        "data/customers.csv"
    )

    query = query.lower()

    for _, customer in customers.iterrows():

        customer_id = str(
            customer["customer_id"]
        ).lower()

        customer_name = str(
            customer["name"]
        ).lower()

        if (
            customer_id in query
            or customer_name in query
        ):

            return {
                "customer_id":
                    customer["customer_id"],

                "customer_name":
                    customer["name"]
            }

    return None

    """
Customer Resolver

Purpose:
Identifies the customer mentioned
in a natural language query.

Example:

"Investigate Allison Reese"
            ↓
{
    "customer_id": "C0001",
    "customer_name": "Allison Reese"
}

Future:
Can be replaced by LLM-based
entity extraction.
"""