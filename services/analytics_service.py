import pandas as pd

from services.risk_service import calculate_risk


def get_suspicious_customers():

    customers = pd.read_csv(
        "data/customers.csv"
    )

    behaviors = pd.read_csv(
        "data/behaviors.csv"
    )

    suspicious_customers = []

    for _, behavior in behaviors.iterrows():

        risk_score = calculate_risk(
            behavior
        )

        customer = customers[
            customers["customer_id"]
            == behavior["customer_id"]
        ]

        if not customer.empty:

            suspicious_customers.append(
                {
                    "customer_id":
                        behavior["customer_id"],

                    "customer_name":
                        customer.iloc[0]["name"],

                    "risk_score":
                        risk_score
                }
            )

    suspicious_customers.sort(
        key=lambda x: x["risk_score"],
        reverse=True
    )

    return suspicious_customers[:10]


"""
Analytics Service

Purpose:
Provides customer risk analytics
and investigation insights.

Functions:
- get_suspicious_customers()
- get_top_risk_customers()
- get_crypto_customers()
- get_high_value_transaction_customers()

Future:
Will support dashboard analytics
and investigation recommendations.
"""