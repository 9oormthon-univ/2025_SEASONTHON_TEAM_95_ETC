def parse_results(results):

    return {item["label"].lower(): item["score"] for item in results}

def cross_validate(results_list):

    ai_scores, real_scores = [], []

    for result in results_list:
        parsed = parse_results(result)
        ai_scores.append(parsed.get("artificial", parsed.get("ai", 0)))
        real_scores.append(parsed.get("human", parsed.get("real", 0)))

    ai_avg = sum(ai_scores) / len(ai_scores)
    real_avg = sum(real_scores) / len(real_scores)

    # Confidence level
    if ai_avg > 0.7:
        decision = "AI Generated"
        confidence = "High"
    elif real_avg > 0.7:
        decision = "Real Image"
        confidence = "High"
    elif 0.3 < ai_avg < 0.7:
        decision = "Uncertain"
        confidence = "Medium"
    else:
        decision = "Risk"
        confidence = "Low"

    return {
        "AI": round(ai_avg * 100, 2),
        "Real": round(real_avg * 100, 2),
        "final_decision": decision,
        "confidence": confidence
    }
