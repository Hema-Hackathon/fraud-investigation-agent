from agents.investigation_agent import (
    investigate
)

from services.explanation_service import (
    generate_summary
)

result = investigate("C0001")

print(
    generate_summary(result)
)