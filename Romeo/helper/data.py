from pyrogram.types import InlineKeyboardButton, WebAppInfo

class Data:

    text_help_menu = (
        "ㅤ\n\n**☞︎︎︎ 𝐑𝐨𝐦𝐞𝐨𝐁𝐨𝐭 ★ 𝐏𝐥𝐮𝐠𝐢𝐧𝐬 ☟︎︎︎**"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("Re-Open", callback_data="reopen")]]
