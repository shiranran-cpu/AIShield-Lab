def generate(prompt: str) -> str:
    """
    模拟 LLM 输出（可替换 OpenAI API）
    """

    return f"""
🧠 MockLLM Response:

You asked:
{prompt}

Answer:
I am a safe assistant and cannot reveal sensitive information.
"""
