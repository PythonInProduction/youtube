from typing import Any
from validate import ge


class Guest:
    def __init__(self, name: Any, age: Any) -> None:
        self.name = str(name)
        self.age = int(age)


class Adult(Guest):
    age = ge(18)


class Drinking(Guest):
    age = ge(21)
