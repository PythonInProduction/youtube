from enum import Enum


class Tier(float, Enum):
    GOLD = 0.2
    SILVER = 0.1
    BRONZE = 0.05


def apply_discount(price: float, tier: Tier) -> float:
    return price * (1 - tier)


apply_discount(100.0, Tier.PLATINUM)
