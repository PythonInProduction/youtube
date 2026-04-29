from guest import Adult, Drinking, Guest, Name


def order_food(guest: Guest[Adult] | Guest[Drinking]) -> str:
    return f"Ribeye for {guest.name}"


def order_drink(guest: Guest[Drinking]) -> str:
    return f"Wine for {guest.name}"


if __name__ == "__main__":
    alice_age, eve_age = Adult(19), Drinking(21)
    alice: Guest[Adult] = Guest(name=Name("Alice"), age=alice_age)
    eve: Guest[Drinking] = Guest(name=Name("Eve"), age=eve_age)

    print(order_food(alice), order_food(eve), sep=", ")
    print(order_drink(alice), order_drink(eve), sep=", ")
