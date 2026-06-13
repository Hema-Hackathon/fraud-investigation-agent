from constants.intents import *


def identify_intent(query: str):

    query = query.lower()

    if "suspicious" in query:
        return SHOW_SUSPICIOUS_CUSTOMERS

    if "crypto" in query:
        return SHOW_CRYPTO_TRANSACTIONS

    if "high value" in query:
        return SHOW_HIGH_VALUE_TRANSACTIONS

    if "investigate" in query:
        return INVESTIGATE_CUSTOMER

    if "why" in query or "explain" in query:
        return EXPLAIN_RISK

    return "UNKNOWN"