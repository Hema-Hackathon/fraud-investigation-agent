from tools.context_tool import get_customer
from tools.transaction_tool import get_transactions
from tools.behavior_tool import get_behavior
from services.transaction_analysis_service import analyze_transactions

from services.risk_service import calculate_risk


def investigate(customer_id: str):

    customer = get_customer(customer_id)

    transactions = get_transactions(customer_id)

    behaviors = get_behavior(customer_id)

    if not behaviors:
        return {
            "error": f"No behavior data found for {customer_id}"
        }

    behavior = behaviors[0]

    risk_score = calculate_risk(behavior)

    findings = []

    if behavior["new_device"]:
        findings.append("New Device Login")

    if behavior["midnight_transaction"]:
        findings.append("Midnight Transaction")

    if behavior["vpn_used"]:
        findings.append("VPN Usage")

    if risk_score >= 80:
        risk_level = "HIGH"
        recommendation = "Escalate Investigation"

    elif risk_score >= 50:
        risk_level = "MEDIUM"
        recommendation = "Monitor Customer"

    else:
        risk_level = "LOW"
        recommendation = "No Action Required"

    
    print("DEBUG - Transactions Count:", len(transactions))

    transaction_findings = analyze_transactions(transactions)

    print("DEBUG - Transaction Findings:", transaction_findings)

    findings.extend(transaction_findings)

    print("DEBUG - Final Findings:", findings)

    
    return {
        "customer": customer,
        "transactions": transactions,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "findings": findings,
        "recommendation": recommendation
    }
