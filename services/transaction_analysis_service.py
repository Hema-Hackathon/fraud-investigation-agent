def analyze_transactions(transactions):

    findings = []

    high_value_count = 0
    crypto_count = 0

    high_value_transactions = []
    crypto_transactions = []

    for txn in transactions:

        if txn["amount"] > 250000:

            high_value_count += 1

            high_value_transactions.append({
                "transaction_id": txn["transaction_id"],
                "amount": txn["amount"]
            })

        if txn["transaction_type"] == "CRYPTO":

            crypto_count += 1

            crypto_transactions.append({
                "transaction_id": txn["transaction_id"],
                "amount": txn["amount"]
            })

    if high_value_count > 0:
        findings.append(
            f"High Value Transactions ({high_value_count})"
        )

    if crypto_count > 0:
        findings.append(
            f"Crypto Transactions ({crypto_count})"
        )

    return {
        "findings": findings,
        "high_value_transactions": high_value_transactions,
        "crypto_transactions": crypto_transactions
    }