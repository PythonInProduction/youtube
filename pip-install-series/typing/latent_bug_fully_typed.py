from typing import Literal


def apply_discount(
    price: float,
    tier: Literal["gold", "silver", "bronze"],
) -> float:
    discounts: dict[Literal["gold", "silver", "bronze"], float] = {
        "gold": 0.2,
        "silver": 0.1,
        "bronze": 0.05,
    }
    discount: float = discounts[tier]
    return price * (1 - discount)
