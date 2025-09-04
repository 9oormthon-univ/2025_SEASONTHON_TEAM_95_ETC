def parse_results(results):

    return {item["label"].lower(): item["score"] for item in results}

def cross_validate(result1, result2, result3):

    res1 = parse_results(result1)
    res2 = parse_results(result2)
    res3 = parse_results(result3)

    # 가중치 (Ateeqq=0.4, Smogy=0.4, Mirage=0.2)
    weights = {"res1": 0.4, "res2": 0.4, "res3": 0.2}

    ai_avg = (
        res1.get("AI", res1.get("artificial", 0)) * weights["res1"]
        + res2.get("AI", res2.get("artificial", 0)) * weights["res2"]
        + res3.get("artificial", 0) * weights["res3"]
    )

    real_avg = (
        res1.get("Real", res1.get("human", 0)) * weights["res1"]
        + res2.get("Real", res2.get("human", 0)) * weights["res2"]
        + res3.get("human", 0) * weights["res3"]
    )


    if ai_avg > 0.7:
        decision, confidence = "AI Generated", "High"
    elif real_avg > 0.7:
        decision, confidence = "Real Image", "High"
    elif 0.3 < ai_avg < 0.7 and 0.3 < real_avg < 0.7:
        decision, confidence = "Uncertain", "Medium"
    else:
        decision, confidence = "Risk", "Low"

    return {
        "AI": round(ai_avg * 100, 2),
        "Real": round(real_avg * 100, 2),
        "final_decision": decision,
        "confidence": confidence,
    }