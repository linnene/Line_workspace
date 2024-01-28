from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request

from models import User
# from core import verify_password, create_access_token, deps
from scheams import (
    # UserIn_Pydantic,
    Response400,
    ResponseToken,
    Response200,
    # User_Pydantic,
)

