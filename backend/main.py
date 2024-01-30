from uvicorn import run

from .api import all
from .core import TORTOISE_ORM

# from tortoise import Tortoise, run_async


# async def init_db():
#     await Tortoise.init(config=TORTOISE_ORM)
#     await Tortoise.generate_schemas()

# run_async(init_db())