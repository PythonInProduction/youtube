from collections import Counter

import jwt
from fastapi import Depends, FastAPI, Header, HTTPException
from models import DrinkCount, Drinking, Guest

app = FastAPI()
_drinks: Counter[str] = Counter()


def verify_caller(authorization: str = Header(...)) -> str:
    try:
        return jwt.decode(
            authorization.removeprefix("Bearer "),
            key="secret",
            algorithms=["HS256"],
        )["id"]
    except jwt.InvalidTokenError as err:
        raise HTTPException(401, "Invalid token") from err


@app.post("/order/food")
def order_food(guest: Guest, caller_id: str = Depends(verify_caller)) -> str:
    if guest.id != caller_id:
        raise HTTPException(403, "Token does not match guest")
    return f"Ribeye for {guest.name}"


@app.post("/order/drink")
def order_drink(guest: Drinking, caller_id: str = Depends(verify_caller)) -> str:
    if guest.id != caller_id:
        raise HTTPException(403, "Token does not match guest")
    _drinks[guest.id] += 1
    return f"Wine for {guest.name}"


@app.get("/guests/{guest_id}/drinks")
def drink_count(guest_id: str, caller_id: str = Depends(verify_caller)) -> DrinkCount:
    if caller_id != guest_id:
        raise HTTPException(403, "You can only check your own drinks")
    return DrinkCount(guest_id=guest_id, count=_drinks[guest_id])
