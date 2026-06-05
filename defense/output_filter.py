def filter_output(text: str) -> str:
    banned = ["password", "secret", "system prompt"]

    for b in banned:
        if b in text.lower():
            text += "\n⚠️ Output blocked by safety filter"

    return text
