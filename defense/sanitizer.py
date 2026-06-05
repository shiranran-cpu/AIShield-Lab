def sanitize(prompt: str) -> str:
    blacklist = [
        "ignore all previous instructions",
        "system override",
        "reveal hidden",
        "bypass"
    ]

    for w in blacklist:
        prompt = prompt.lower().replace(w, "[FILTERED]")

    return prompt
