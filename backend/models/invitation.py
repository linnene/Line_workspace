from typing import Optional, Iterable

from tortoise import models, BaseDBAsyncClient
from tortoise import fields
from ..models import user

class create_invitation(models.Model):
    invi_id = fields.UUIDField(pk=True, auto_created=True)
    #作者
    author = fields.ForeignKeyField("models.user",related_name="your_invitation") 
    #记录发帖时间
    release_time = fields.DatetimeField(auto_now_add=True)
    #正文内容
    value_invi = fields.CharField(max_length= 100)

#帖子的相关图片
class invi_img(models.Model):
    filename = fields.CharField(max_length=255)
    filepath = fields.CharField(max_length=255)
    invi = fields.ForeignKeyField("models.create_invitation",related_name="img")
