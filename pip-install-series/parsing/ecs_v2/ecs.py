from collections.abc import Iterator
from typing import Any, NewType
from validate import is_valid

# Entity
Guest = NewType("Guest", int)

# Component
Name = NewType("Name", str)  # data component
class Drinking: pass  # tag component

# World
class RestaurantBar:
    def __init__(self):
        self._id: int = 0
        self.names: dict[Guest, Name] = {}
        self.drinkers: dict[Guest, Drinking] = {}

    def _admit(self, name: str) -> Guest:
        guest = Guest(self._id)
        self._id += 1
        self.names[guest] = Name(name)
        return guest

    def parse_guest(self, raw_name: Any, raw_age: Any) -> None:
        name, age = str(raw_name), int(raw_age)
        if not is_valid(age, 18):
            raise ValueError(f"Guest {name} is underage: {age}")
        guest = self._admit(name)
        if is_valid(age, 21):
            self.drinkers[guest] = Drinking()

# System
def serve_food(names: dict[Guest, Name]) -> Iterator[str]:
    return (f"Ribeye for {name}" for name in names.values())

def serve_drink(
    drinkers: dict[Guest, Drinking],
    names: dict[Guest, Name],
) -> Iterator[str]:
    return (f"Wine for {names[guest]}" for guest in drinkers)
