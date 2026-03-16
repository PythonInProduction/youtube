from typing import Literal


def apply_discount(
    price: float,
    tier: Literal["gold", "silver", "bronze"],
) -> float:
    discounts = {
        "gold": 0.2,
        "silver": 0.1,
        "bronze": 0.05,
    }
    if tier not in discounts:
        raise ValueError(f"Invalid tier: {tier}")
    discount = discounts[tier]
    return price * (1 - discount)


discounted_price = apply_discount(100.0, "platinum")
print(discounted_price)
