import random
import asyncio
from pyrogram import filters, Client
from Romeo.modules.help import *
from Romeo.helper.utility import get_arg
from pyrogram.types import *
from pyrogram import __version__
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from Romeo.database.lraid import *
from Romeo import SUDO_USER
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(5368154755)
from Romeo.helper.PyroHelpers import get_ub_chats
from Romeo.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
from .loveraid import LOVES



if LOVES:
 @Client.on_message(filters.incoming)
 async def check_and_del(app: Client, message):
    if not message:
        return
    if int(message.chat.id) in GROUP:
        return
    try:
        if message.from_user.id in (await get_lraid_users()):
            await message.reply_text(f"{random.choice(LOVE)}")
    except AttributeError:
        pass
