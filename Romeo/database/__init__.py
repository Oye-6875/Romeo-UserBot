from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

cli = AsyncIOMotorClient(MONGO_URL)

dbb = cli.program
