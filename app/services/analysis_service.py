import random

def analyze_image(image_id: str) -> dict:
    """
    Mock AI analysis logic.
    Later this can be replaced with a real ML model.
    """

    skin_types = ["Oily", "Dry", "Combination", "Normal"]
    issues_pool = [
        "Acne",
        "Hyperpigmentation",
        "Wrinkles",
        "Dark circles",
        "Redness",
    ]

    result = {
        "image_id": image_id,
        "skin_type": random.choice(skin_types),
        "issues": random.sample(issues_pool, k=random.randint(1, 2)),
        "confidence": round(random.uniform(0.75, 0.95), 2),
    }

    return result
