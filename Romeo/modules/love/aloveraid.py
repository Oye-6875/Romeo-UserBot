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



@Client.on_message(
    filters.command(["rlr", "replyloveraid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return
    if user.id == client.me.id:
        return await ex.edit("**Okay Sure..**")
    elif user.id == SUDO_USERS:
        return await ex.edit("**Okay But Failed Because this user in sudos.. 🐽**")
    elif user.id == VERIFIED_USERS:
        return await ex.edit("**Chal Chal Baap ko Mat sikha..**")
    try:
        if user.id in (await get_lraid_users()):
           await ex.edit("Loveraid is activated on this user")
           return
        await lraid_user(user.id)
        LOVES.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) Activated LoveRaid!")
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return
