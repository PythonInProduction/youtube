import httpx
import jwt
from fastapi import Depends, FastAPI, Header, HTTPException
from models import DrinkCount
from pydantic import TypeAdapter

app = FastAPI()
_parse_drink_count = TypeAdapter(DrinkCount).validate_json

RESTAURANT = "http://restaurant:8000"


def verify_caller(authorization: str = Header(...)) -> str:
    try:
        return jwt.decode(
            authorization.removeprefix("Bearer "),
            key="secret",
            algorithms=["HS256"],
        )["id"]
    except jwt.InvalidTokenError as err:
        raise HTTPException(401, "Invalid token") from err


@app.post("/valet/release/{guest_id}")
def release_car(
    guest_id: str,
    caller_id: str = Depends(verify_caller),
    authorization: str = Header(...),
) -> str:
    if caller_id != guest_id:
        raise HTTPException(403, "You can only release your own car")
    response = httpx.get(
        f"{RESTAURANT}/guests/{guest_id}/drinks",
        headers={"Authorization": authorization},
    )
    drinks = _parse_drink_count(response.content)
    if drinks.count > 0:
        raise HTTPException(
            403, "You have been drinking. Please use our Take Me Home service."
        )
    return f"Your car is on the way, guest {guest_id}"
