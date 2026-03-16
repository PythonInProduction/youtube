def apply_discount(price, tier):
    discounts = {
        "gold": 0.2,
        "silver": 0.1,
        "bronze": 0.05,
    }
    discount = discounts[tier]
    return price * (1 - discount)


discounted_price = apply_discount(100.0, "gold")
print(discounted_price)
