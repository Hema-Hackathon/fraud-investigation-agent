def calculate_risk(behavior):

    score = 0

    if behavior["new_device"]:
        score += 20

    if behavior["midnight_transaction"]:
        score += 20

    if behavior["vpn_used"]:
        score += 20

    if behavior["new_beneficiary"]:
        score += 20

    if behavior["failed_logins"] >= 5:
        score += 20

    return min(score, 100)