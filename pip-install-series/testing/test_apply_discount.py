import pytest
from pricing import Tier, apply_discount


def test_apply_discount_happy_path():
    assert apply_discount(100.0, Tier.GOLD) == 80.0


@pytest.mark.parametrize("tier", Tier)
def test_discounted_price_is_positive(tier):
    assert apply_discount(100.0, tier) > 0.0
