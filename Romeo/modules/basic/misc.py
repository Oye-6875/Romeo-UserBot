import asyncio
from datetime import datetime
from platform import python_version

from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from config import ALIVE_PIC, ALIVE_TEXT
from Romeo import START_TIME
from Romeo import SUDO_USER
from Romeo.helper.PyroHelpers import ReplyCheck
from Romeo.modules.help import add_command_help
from Romeo.modules.bot.inline import get_readable_time

alive_logo = ALIVE_PIC or "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg"

if ALIVE_TEXT:
   txt = (
        f"**❥︎ 𝐀𝐋𝐈𝐕𝐄 ☟︎︎︎**\n\n"
        f"**🇻𝐄𝐑𝐒𝐈𝐎𝐍 ❥︎** `1.0`\n"
        f"**🇺𝐏★🇹𝐈𝐌𝐄 ❥︎** `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
        f"**🇵𝐘𝐓𝐇𝐎𝐍 ❥︎** `{python_version()}`\n"
        f"**🇵𝐘𝐑𝐎𝐆𝐑𝐀𝐌 ❥︎** `{__version__}`\n"        
    )
    

@Client.on_message(
    filters.command(["alive", "awake"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def alive(client: Client, message: Message):
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    xd = (f"{txt}")
    try:
        await asyncio.gather(
            send(
                message.chat.id,
                alive_logo,
                caption=xd,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await message.reply_text(xd, disable_web_page_preview=True)


@Client.on_message(filters.command("creator", ".") & filters.me)
async def creator(bot: Client, message: Message):
    await message.edit("🇨𝐑𝐄𝐀𝐓𝐎𝐑 ❥︎ [𝕾🅡︎🅐︎🅙︎𝕾](https://t.me/Romeo_RJ_143)")


@Client.on_message(filters.command(["uptime", "up"], ".") & filters.me)
async def uptime(bot: Client, message: Message):
    now = datetime.now()
    current_uptime = now - START_TIME
    await message.edit(f"Uptime 💞\n" f"```{str(current_uptime).split('.')[0]}```")


@Client.on_message(filters.command("id", ".") & filters.me)
async def get_id(bot: Client, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**File ID**: `{rep.audio.file_id}`"
            file_id += "**File Type**: `audio`"

        elif rep.document:
            file_id = f"**File ID**: `{rep.document.file_id}`"
            file_id += f"**File Type**: `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**File ID**: `{rep.photo.file_id}`"
            file_id += "**File Type**: `photo`"

        elif rep.sticker:
            file_id = f"**Sicker ID**: `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**Sticker Set**: `{rep.sticker.set_name}`\n"
                file_id += f"**Sticker Emoji**: `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**Animated Sticker**: `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**Animated Sticker**: `False`\n"
            else:
                file_id += "**Sticker Set**: __None__\n"
                file_id += "**Sticker Emoji**: __None__"

        elif rep.video:
            file_id = f"**File ID**: `{rep.video.file_id}`\n"
            file_id += "**File Type**: `video`"

        elif rep.animation:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `GIF`"

        elif rep.voice:
            file_id = f"**File ID**: `{rep.voice.file_id}`\n"
            file_id += "**File Type**: `Voice Note`"

        elif rep.video_note:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `Video Note`"

        elif rep.location:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.venue.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.venue.location.latitude}`\n\n"
            file_id += "**Address**:\n"
            file_id += f"**title**: `{rep.venue.title}`\n"
            file_id += f"**detailed**: `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`\n\n"
        user_detail += file_id
        await message.edit(user_detail)

    else:
        await message.edit(f"**Chat ID**: `{message.chat.id}`")




add_command_help(
    "start",
    [
        [".alive", "Check if the bot is alive or not."],
        [".creator", "Show the creator of this userbot."],
        [".id", "Send id of what you replied to."],
        [".up `or` .uptime", "Check bot's current uptime."],
    ],
)
