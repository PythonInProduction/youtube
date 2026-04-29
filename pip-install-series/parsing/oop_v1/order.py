from guest import Guest
from validate import is_valid


def order_food(guest: Guest) -> str:
    return f"Ribeye for {guest.name}"


def order_drink(guest: Guest) -> str:
    if not is_valid(guest.age, 21):
        raise ValueError(f"{guest} is too young to drink")
    return f"Wine for {guest.name}"
