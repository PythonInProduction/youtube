from typing import Any, NamedTuple
from validate import is_valid


class Guest(NamedTuple):
    name: str
    age: int  # age is just a number


def parse_guest(raw_name: Any, raw_age: Any) -> Guest:
    name, age = str(raw_name), int(raw_age)
    if not is_valid(age, 18):
        raise ValueError(f"Guest {name} is underage: {age}")
    return Guest(name, age)
