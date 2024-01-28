import secrets
from typing import Optional,ClassVar

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
#     TITLE: Optional[str] = "电影列表接口"

    Default_user_name: Optional[str] = "luna"
    
    target_folder: str = '' #帖子的图片文件保存路径

    ALGORITHM: str = "HS256"  # 加密算法
    SECRET_KEY: str = secrets.token_urlsafe(32)  # 随机生成的base64位字符串
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # token的时效 3 天 = 60 * 24 * 3
    
    #迁移config
    config: ClassVar[dict] ={
        'connections':{
            'default':{
                # 'engine' : 'tortoise.backends.asyncpg' , # PostgreSQL
                'engine' : 'tortoise.backends.mysql' ,# MySQL or Mariadb
                'credentials':{
                    'host': '127.0.0.1',
                    'port': '3306',
                    'user': 'root',
                    'password':'ioiz73763',
                    'database':'luna',
                    'minsize':1,
                    'maxsize':5,
                    'charset':'utf8m64',
                    'echo':True
                }
            }
        },
        'apps':{
            'models':{
                'models':['backend.models'],
                'default_connection':'default'
            }
        },
        'user_tz':False,
        'timezone':'Asia/Shanghai'
    }


settings = Settings()
