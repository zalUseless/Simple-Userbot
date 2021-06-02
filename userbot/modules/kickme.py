# For @UniBorg
# ported from Telebot by @Zal
# Courtesy @yasirsiddiqui

"""
.kickme
"""


import time

from telethon.tl.functions.channels import LeaveChannelRequest

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^kickme(?: |$)(.*)")
async def leave(tolol):
    x = bot.me
    name = x.first_name
    if not tolol.text[0].isalpha() and tolol.text[0] not in ("/", "#", "@", "!"):

        await tolol.edit(f"`{name} has left this group, bye!!.`")

        time.sleep(3)

        if "-" in str(tolol.chat_id):

            await borg(LeaveChannelRequest(tolol.chat_id))

        else:

            await tolol.edit("`This is Not A Chat. Please use this in groups :/`")


CMD_HELP.update({"kickme": ".kickme\nUse - Leave the group."})
