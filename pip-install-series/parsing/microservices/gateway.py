import jwt
from fastapi import FastAPI, HTTPException
from models import Credentials, Guest
from pydantic import TypeAdapter

app = FastAPI()
_parse_guest = TypeAdapter(Guest).validate_python


@app.post("/guests")
def check_in(creds: Credentials) -> Guest:
    try:
        claims = jwt.decode(creds.token, key="secret", algorithms=["HS256"])
    except jwt.InvalidTokenError as err:
        raise HTTPException(401, "Invalid ID") from err
    return _parse_guest(
        {"id": claims["id"], "name": claims["name"], "age": claims["age"]}
    )
