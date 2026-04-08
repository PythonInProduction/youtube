import pytest
from hypothesis import given, strategies as st
from pricing_fixed import Tier, apply_discount


def test_apply_discount_happy_path():
    assert apply_discount(100.0, Tier.GOLD) == 80.0


@pytest.mark.parametrize("tier", Tier)
def test_tier_is_valid_discount_rate(tier):
    assert 0.0 < tier < 1.0


@given(
    price=st.floats(min_value=0, exclude_min=True, allow_subnormal=False, allow_infinity=False),
    tier=st.sampled_from(Tier),
)
def test_discounted_price_stays_between_zero_and_original(price, tier):
    assert 0.0 < apply_discount(price, tier) < price
