def generate_summary(result):

    customer = result["customer"][0]

    ai_summary = (
        f"Customer {customer['name']} has been classified as "
        f"{result['risk_level']} risk based on behavioral anomalies, "
        f"transaction analysis and crypto exposure. "
        f"{len(result['findings'])} investigation findings were detected. "
        f"Recommended action: {result['recommendation']}."
    )

    return {
        "customer_name": customer["name"],
        "risk_score": result["risk_score"],
        "risk_level": result["risk_level"],
        "findings": result["findings"],
        "recommendation": result["recommendation"],
        "transactions": result["transactions"][:5],
        "ai_summary": ai_summary
    }