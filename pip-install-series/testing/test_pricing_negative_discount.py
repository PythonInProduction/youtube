import pytest
from pricing_negative_discount import Tier, apply_discount


def test_apply_discount_happy_path():
    assert apply_discount(100.0, Tier.GOLD) == 80.0


@pytest.mark.parametrize("tier", Tier)
def test_tier_is_valid_discount_rate(tier):
    assert 0.0 < tier < 1.0
