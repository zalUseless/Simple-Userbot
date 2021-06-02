# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# ported from Ultroid by @Zal
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from userbot import CMD_HELP, bot
from userbot.events import register

"""
For Command

• `{i}dm <username/id> <reply/type>`
    Direct Message the User.

"""


@register(outgoing=True, pattern="^.dm (.*)")
async def dm(tolol):
    if len(tolol.text) > 3:
        if not tolol.text[3] == " ":  # weird fix
            return
    d = tolol.pattern_match.group(1)
    c = d.split(" ")
    try:
        chat_id = await get_user_id(c[0])
    except Exception as ex:
        return await tolol.edit("`" + str(ex) + "`", time=5)
    msg = ""
    masg = await tolol.get_reply_message()
    if tolol.reply_to_msg_id:
        await bot.send_message(chat_id, masg)
        await tolol.edit("`⚜️Message Delivered!`", time=4)
    for i in c[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await bot.send_message(chat_id, msg)
        await tolol.edit("`⚜️Message Delivered!⚜️`", time=4)
    except BaseException:
        await tolol.edit(
            "`{i}help dm`",
            time=4,
        )
CMD_HELP.update({"dm": "`.dm <username/id> <reply/type>`\
                \nPenjelasan: Direct Pesan...."})
