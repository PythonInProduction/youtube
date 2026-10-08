import math

def get_circumference(radius: int | float, ndigits: int | None = None) -> float:
    circumference = 2 * math.pi * radius
    if ndigits is None:
        return circumference
    return round(circumference, ndigits)

print(get_circumference(5))  # still works as before
print(get_circumference(5, 2))  # NEW FEATURE!
