from typing import Annotated

from pydantic import BaseModel, Field


class Credentials(BaseModel):
    id: str
    token: str  # JWT


class GuestBase(BaseModel):
    id: str
    name: str


class Adult(GuestBase):
    age: Annotated[int, Field(ge=18, lt=21)]


class Drinking(GuestBase):
    age: Annotated[int, Field(ge=21)]


Guest = Adult | Drinking


class DrinkCount(BaseModel):
    guest_id: str
    count: int
