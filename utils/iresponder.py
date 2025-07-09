import random


def apply_ai_variation(answer: str) -> str:
    """
    """
    variations = [
        answer,
        f"{answer} Let me know if you need more info.",
        f"{answer} Hope that helps!",
        f"Sure! {answer}",
        f"{answer} Feel free to ask more questions.",
    ]
    return random.choice(variations)
