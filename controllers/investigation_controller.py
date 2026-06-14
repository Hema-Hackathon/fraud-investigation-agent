from services.query_processor import (
    process_query
)

from services.analytics_service import (
    get_suspicious_customers
)

from services.customer_resolver import (
    resolve_customer
)

from constants.intents import (
    SHOW_SUSPICIOUS_CUSTOMERS
)

from agents.investigation_agent import (
    investigate
)

from constants.intents import (
    SHOW_SUSPICIOUS_CUSTOMERS,
    INVESTIGATE_CUSTOMER
)


def handle_query(query: str):

    intent_data = process_query(query)
    
    if intent_data["intent"] == SHOW_SUSPICIOUS_CUSTOMERS:
    
        return get_suspicious_customers()
    
    elif intent_data["intent"] == INVESTIGATE_CUSTOMER:
    
        customer = resolve_customer(query)

        return investigate(
            customer["customer_id"]
        )
    
    return intent_data




"""
Investigation Controller

Purpose:
Receives user requests and routes them
to the appropriate investigation service.

Current Support:
- Show Suspicious Customers

Future Support:
- Investigate Customer
- Explain Risk
- Crypto Analysis
- High Value Transaction Analysis
"""