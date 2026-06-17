def generate_summary(result):

    customer = result["customer"][0]

    return {
        "customer_name": customer["name"],
        "risk_score": result["risk_score"],
        "risk_level": result["risk_level"],
        "findings": result["findings"],
        "recommendation": result["recommendation"],
        "transactions": result["transactions"][:5]
    }