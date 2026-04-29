from typing import Annotated
from pydantic import BaseModel, Field, field_validator


class Adult(BaseModel):
    name: str
    age: Annotated[int, Field(ge=18)]


class Drinking(Adult):
    # validate age field further
    @field_validator("age")
    @classmethod
    def check_drinking_age(cls, age: int) -> int:
        if age < 21:
            raise ValueError(f"age {age} is below drinking age")
        return age
