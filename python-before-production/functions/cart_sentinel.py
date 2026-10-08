def add_to_cart(item: str, cart: list[str] | None = None) -> list[str]:
    if cart is None:
        cart = []
    cart.append(item)
    return cart

alice_cart = add_to_cart("apple")
bob_cart = add_to_cart("banana")

print(alice_cart)
print(bob_cart)
