from constants.intents import (
    SHOW_SUSPICIOUS_CUSTOMERS,
    SHOW_CRYPTO_TRANSACTIONS,
    SHOW_HIGH_VALUE_TRANSACTIONS,
    INVESTIGATE_CUSTOMER,
    EXPLAIN_RISK,
    UNKNOWN
)


def interpret_query(query: str):

    query = query.lower()

    if "suspicious" in query:
        return {
            "intent": SHOW_SUSPICIOUS_CUSTOMERS
        }

    elif "crypto" in query:
        return {
            "intent": SHOW_CRYPTO_TRANSACTIONS
        }

    elif "high value" in query:
        return {
            "intent": SHOW_HIGH_VALUE_TRANSACTIONS
        }

    elif "investigate" in query:
        return {
            "intent": INVESTIGATE_CUSTOMER,
            "query": query
        }

    elif "why" in query or "explain" in query:
        return {
            "intent": EXPLAIN_RISK,
            "query": query
        }

    return {
        "intent": UNKNOWN
    }

    