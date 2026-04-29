from guest import Drinking, Guest


def order_food(guest: Guest) -> str:
    return f"Ribeye for {guest.name}"


def order_drink(guest: Guest) -> str:
    if not isinstance(guest.age, Drinking):
        raise ValueError(f"{guest} is too young to drink")
    return f"Wine for {guest.name}"
