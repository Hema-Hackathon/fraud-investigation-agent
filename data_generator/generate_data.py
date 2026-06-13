from faker import Faker
import pandas as pd
import random

fake = Faker()

customers = []

for i in range(1, 101):

    customers.append({
        "customer_id": f"C{i:04}",
        "name": fake.name(),
        "age": random.randint(18, 75),
        "risk_profile": random.choice(
            ["Low", "Medium", "High"]
        ),
        "country": fake.country()
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "data/customers.csv",
    index=False
)

print("customers.csv generated")

transactions = []

for i in range(1, 1001):

    customer_id = f"C{random.randint(1,100):04}"

    transactions.append({
        "transaction_id": f"T{i:05}",
        "customer_id": customer_id,
        "amount": round(random.uniform(100, 500000), 2),
        "transaction_type": random.choice([
            "TRANSFER",
            "PAYMENT",
            "WITHDRAWAL",
            "CRYPTO"
        ]),
        "timestamp": fake.date_time_this_year()
    })

transactions_df = pd.DataFrame(transactions)

transactions_df.to_csv(
    "data/transactions.csv",
    index=False
)

print("transactions.csv generated")

behaviors = []

for i in range(1, 101):

    behaviors.append({
        "customer_id": f"C{i:04}",
        "new_device": random.choice([True, False]),
        "midnight_transaction": random.choice([True, False]),
        "vpn_used": random.choice([True, False]),
        "new_beneficiary": random.choice([True, False]),
        "failed_logins": random.randint(0, 10)
    })

behaviors_df = pd.DataFrame(behaviors)

behaviors_df.to_csv(
    "data/behaviors.csv",
    index=False
)

print("behaviors.csv generated")