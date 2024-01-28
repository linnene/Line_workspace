from typing import Optional, Iterable

from tortoise import models, BaseDBAsyncClient
from tortoise import fields

from ..core import get_password_hash
from enum import Enum
from ..models  import invitation

#用户

class Gender(Enum):
    '''
    性别
    '''
    man = "M"
    woman = "W"

class User(models.Model):
    id = fields.IntField(max_length=20, null=False, description="user_id", unique=True, pk= True)
    password = fields.CharField(max_length=128, null=False, description="password")

    nickname = fields.CharField(max_length=20, null=True, description="nickname", default ="luna")
    
    # your_Followings = fields.ManyToManyField(
    #     "User.User",
    #     related_name = "followings"
    #     """
    #     ,through="Followings"
    #     """
    #     )
    
    gender = fields.CharEnumField( max_length=1,enum_type=Gender)
    
    invitation = fields.ForeignKeyField("models.create_invitation")

#保存操作
    async def save(
        self,
        using_db: Optional[BaseDBAsyncClient] = None,
        update_fields: Optional[Iterable[str]] = None,
        force_create: bool = False,
        force_update: bool = False,
    ) -> None:
        if force_create or "password" in update_fields:
            self.password = get_password_hash(self.password)

        await super(User, self).save(using_db, update_fields, force_create, force_update)

#关注关系表
# class Followings(models.Model):
#     #关注人
#     user=fields.ForeignKeyField("User.User" , related_name="user_followings")
#     #被关注人
#     followings=fields.ForeignKeyField("User.User" , related_name="followingsed")




