def parse_results(results):
    return {item["label"]: item["score"] for item in results}

def cross_validate(result1, result2):
    res1 = parse_results(result1)
    res2 = parse_results(result2)

    ai_avg = (res1.get("AI", 0) + res2.get("AI", 0)) / 2
    real_avg = (res1.get("Real", 0) + res2.get("Real", 0)) / 2

    total = ai_avg + real_avg
    ai_prob = (ai_avg / total) * 100 if total > 0 else 0
    real_prob = (real_avg / total) * 100 if total > 0 else 0

    # confidence 등급
    if ai_prob >= 70 or real_prob >= 70:
        decision = "Certain"
        confidence = "High"
    elif 30 <= ai_prob <= 70 or 30 <= real_prob <= 70:
        decision = "Uncertain"
        confidence = "Medium"
    else:
        decision = "Risk"
        confidence = "Low"

    return {
        "AI": round(ai_prob, 2),
        "Real": round(real_prob, 2),
        "final_decision": decision,
        "confidence": confidence
    }
