from typing import Any, NamedTuple, NewType
from validate import is_valid

Name = NewType("Name", str)
Adult = NewType("Adult", int)
Drinking = NewType("Drinking", int)


class Guest[T: (Adult, Drinking)](NamedTuple):
    name: Name
    age: T  # age is NOT just a number


def parse_guest(raw_name: Any, raw_age: Any) -> Guest:
    name, age = str(raw_name), int(raw_age)
    if not is_valid(age, 18):
        raise ValueError(f"Guest {name} is underage: {age}")
    name, age = Name(name), Adult(age)
    if not is_valid(age, 21):
        return Guest(name, age)
    return Guest(name, Drinking(age))
