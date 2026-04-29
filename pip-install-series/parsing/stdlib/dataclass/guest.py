from dataclasses import dataclass


@dataclass
class Drinking:
    name: str
    age: int

    def __post_init__(self):
        self.name, self.age = str(self.name), int(self.age)
        if self.age < 21:
            raise ValueError(f"Guest is below drinking age: {self.age}")
