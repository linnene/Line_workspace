from fastapi import APIRouter, Depends, Body,UploadFile,File
from tortoise.contrib.pydantic.creator import pydantic_model_creator
import os
from typing import List

from ....models.invitation import invi_img,create_invitation

from ....core.config import settings
from ....scheams import invitation_Pydantic

invi = APIRouter(tags=["帖子相关"])

#图片写入——————————————————————————————————————————————————————————————————————————————

FileModelPydantic = pydantic_model_creator(invi_img)

@invi.put("/put_img",tags=["图片更新"])
async def put_invi_img(file: UploadFile = File(... ,media_type="image/png")):

    file_path = os.path.join(settings.target_folder, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    file_model = await invi_img.create(filename=file.filename, filepath=file_path)

    return await FileModelPydantic.from_tortoise_orm(file_model)

#——————————————————————————————————————————————————————————————————————————————————————


@invi.post("/invi",tags=["新帖子创建"])
async def put_new_invi(invi:invitation_Pydantic ,  imgs: List[UploadFile] = File(...)):
    for img in imgs:
        await put_invi_img(img)
    return{invi}

# #測試用（for text）
# @invi.get("/")
# async def invitation_text(yua:int):
#     return{"yua":yua}
