def parse_results(results):

    mapping = {
        "artificial": "AI",
        "fake": "AI",
        "ai": "AI",
        "AI": "AI",
        "real": "Real",
        "human": "Real",
        "Real": "Real"
    }

    parsed = {}
    for item in results:
        label = mapping.get(item["label"].lower(), item["label"])
        parsed[label] = item["score"]
    return parsed


def cross_validate(result1, result2, result3):

    res1 = parse_results(result1)
    res2 = parse_results(result2)
    res3 = parse_results(result3)


    weights = {"res1": 0.4, "res2": 0.4, "res3": 0.2}

    ai_avg = (
        res1.get("AI", 0) * weights["res1"] +
        res2.get("AI", 0) * weights["res2"] +
        res3.get("AI", 0) * weights["res3"]
    )

    real_avg = (
        res1.get("Real", 0) * weights["res1"] +
        res2.get("Real", 0) * weights["res2"] +
        res3.get("Real", 0) * weights["res3"]
    )


    if ai_avg > 0.7:
        decision = "AI Generated"
        confidence = "High"
    elif real_avg > 0.7:
        decision = "Real Image"
        confidence = "High"
    else:
        decision = "Uncertain"
        confidence = "Medium"

    return {
        "AI": round(ai_avg * 100, 2),
        "Real": round(real_avg * 100, 2),
        "final_decision": decision,
        "confidence": confidence
    }
