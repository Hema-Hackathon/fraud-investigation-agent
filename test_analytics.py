from services.analytics_service import (
    get_suspicious_customers
)

results = get_suspicious_customers()

for customer in results:
    print(customer)