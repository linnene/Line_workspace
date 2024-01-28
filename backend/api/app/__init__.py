from fastapi import APIRouter
from .endpoints.user import user 
from .endpoints.invitation import invi
 

app = APIRouter(tags=["初始化输入接口"])


app.include_router(user,prefix= "/user")
app.include_router(invi,prefix= "/invi")
# app.include_router(login,prefix= "/login")

