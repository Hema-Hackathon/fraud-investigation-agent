def generate_summary(result):

    customer = result["customer"][0]

    summary = f"""
Investigation Summary

Customer:
{customer['name']}

Risk Score:
{result['risk_score']}

Risk Level:
{result['risk_level']}

Findings:
"""

    for finding in result["findings"]:
        summary += f"\n• {finding}"

    summary += f"""

Recommendation:
{result['recommendation']}
"""

    return summary