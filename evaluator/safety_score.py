def compute_score(prompt: str, output: str):
    risk_words = [
        "ignore", "override", "system prompt",
        "password", "secret"
    ]

    score = 0.0

    for w in risk_words:
        if w in prompt.lower():
            score += 0.4
        if w in output.lower():
            score += 0.3

    score = min(score, 1.0)

    return {
        "risk_score": round(score, 2),
        "safe": score < 0.5
    }
