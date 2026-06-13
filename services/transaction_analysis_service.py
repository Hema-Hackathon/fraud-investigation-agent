def analyze_transactions(transactions):

    findings = []

    high_value_count = 0

    for txn in transactions:

        amount = txn["amount"]

        if amount > 100000:
            high_value_count += 1

        if amount > 250000:
            findings.append(
                f"High Value Transaction: {amount}"
            )

        if txn["transaction_type"] == "CRYPTO":
            findings.append(
                "Crypto Transaction Detected"
            )

    if high_value_count >= 3:
        findings.append(
            "Multiple High Value Transactions"
        )

    return findings