import math

def get_circumference(radius: int | float, ndigits: int) -> float:
    return round(2 * math.pi * radius, ndigits)

print(get_circumference(5))
