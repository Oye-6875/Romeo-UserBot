import os
import re
import asyncio
import time
from pyrogram import filters, Client
from pyrogram.types import *
from Romeo import app
from config import *

#cloner
@app.on_message(filters.command("cl", ["/", ".", "!", "?"]) & filters.private)
async def cl(app, message):
    k = await message.reply_text("Usage:\n\n`/cl` pyro-session")
    token = message.command[1]
    try:
        await k.edit("Booting Your Client")
        r = Client(name="rj", api_id=API_ID, api_hash=API_HASH, session_string=token, plugins=dict(root="Romeo/modules"))
        await r.start()
        user = await r.get_me()
        await k.edit(f"""
𝐘𝐨𝐮𝐫 𝐂𝐥𝐢𝐞𝐧𝐭 𝐇𝐚𝐬 𝐁𝐞𝐞𝐧 𝐒𝐮𝐜𝐜𝐞𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 ☟︎︎︎ 
𝐈𝐝 ❥︎ {user.id}
𝐍𝐚𝐦𝐞 ❥︎ {user.first_name}
𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ❥︎ @{user.username}
✅✅✅
""")
    except Exception as e:
        await k.edit(f"**ERROR:** `{str(e)}`")

