from enum import Enum


class Tier(float, Enum):
    DIAMOND = 0.4
    PLATINUM = 0.3
    GOLD = 0.2
    SILVER = 0.1
    BRONZE = 0.05


def apply_discount(price: float, tier: Tier) -> float:
    return price * (1 + tier)
