def apply_discount(price: float, tier: str) -> float:
    discounts = {
        "gold": 0.2,
        "silver": 0.1,
        "bronze": 0.05,
    }
    discount = discounts[tier]
    return price * (1 - discount)


apply_discount(100.0, "platinum")
