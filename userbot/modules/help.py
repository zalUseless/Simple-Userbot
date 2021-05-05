# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP, USERS, bot
from userbot.events import register
from platform import uname

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    global USERS
    user = await bot.get_me()
    user.name = user.first_name
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Tulis Modulenya Yang Bener Asu... **")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t🌪  "
        await event.edit("**🌪 Akeno 🌪**\n\n"
                         f"**OWNER : [{user.first_name}](tg://user?id={user.id})**\n**MODULES : {len(modules)}**\n\n"
                         "**MODULES:**\n"
                         f"➥🌪 {string} ⬅️\n\n")
        await event.reply(f"\n**Contoh** : **Ketik** `.help comli` **Untuk Informasi Pengunaan.\nAtau Bisa Juga Ketik** `.helpme` **Untuk Main Menu Yang Lain-Nya.**")
        await asyncio.sleep(1000)
        await event.delete()
