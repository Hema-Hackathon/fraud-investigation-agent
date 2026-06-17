def generate_summary(result):

    customer = result["customer"][0]

    ai_summary = (
        f"Customer {customer['name']} has been classified as "
        f"{result['risk_level']} risk. Behavioral analysis identified "
        f"new device activity, VPN usage and unusual transaction timing. "
        f"Transaction analysis detected crypto exposure and multiple "
        f"high-value transfers. Recommended action: "
        f"{result['recommendation']}."
    )

    return {
        "customer_id": customer["customer_id"],
        "customer_name": customer["name"],
        "age": customer["age"],
        "country": customer["country"],
        "risk_profile": customer["risk_profile"],
    
        "risk_score": result["risk_score"],
        "risk_level": result["risk_level"],
        "findings": result["findings"],
        "recommendation": result["recommendation"],
        "transactions": result["transactions"][:5],
        "ai_summary": ai_summary,
        "high_value_transactions": result["high_value_transactions"],
        "crypto_transactions": result["crypto_transactions"]
    }
