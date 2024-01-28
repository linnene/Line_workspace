from typing import Optional, Iterable

from tortoise import models, BaseDBAsyncClient
from tortoise import fields
from ..models import User

class create_invitation(models.Model):
    invi_id = fields.CharField(max_length=20,pk = True)
    author = fields.ForeignKeyField("models.User",related_name="your_invitation") 
    #记录发帖时间
    release_time = fields.DatetimeField(auto_now_add=True)



class invi_img(models.Model):
    id = fields.IntField(pk=True)
    filename = fields.CharField(max_length=255)
    filepath = fields.CharField(max_length=255)
    invi = fields.ForeignKeyField("models.create_invitation",related_name="img")

    class Meta:
        table = 'files'
