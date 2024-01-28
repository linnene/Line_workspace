from fastapi import APIRouter,Depends

from ....models import User
from ....core import deps

user = APIRouter(tags=["用户相关"])



#获取当前用户状态
@user.get("/user_info",summary="Get current user")
async def get_cerr_user_get(user_obj: User = Depends(deps.get_current_user)):
    return User


# 测试用接口
@user.get("/user_info")
async def text_api(rey:int):
    print(rey)
    return{"rey":rey}
