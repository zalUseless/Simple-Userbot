import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST, USERS, bot
from userbot.events import register


@register(outgoing=True, pattern="^.santet(?: |$)(.*)")
async def typewriter(typew):
    global USERS
    user = await bot.get_me()
    user.name = user.first_name
    typew.pattern_match.group(1)
    await typew.edit("`Santet Online.....`")
    sleep(2)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   ▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   █████████████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ██████████████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████████▊")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ███████████████▉")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████████")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████████▎")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████████▍")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████████▌")
    number += 1
    sleep(0.02)
    await typew.edit(str(number) + "%   ████████████████▌")
    sleep(1)
    await typew.edit(f"`Selamat Anda Kena Santet Online.. :v`\n**By** : [{user.first_name}](tg://user?id={user.id})")
    # I did it for two hours :D just ctrl+c - crtl+v


CMD_HELP.update(
    {
        "santet": ".santet\
        \nUsage: Santet Online Gusys :v."
    }
)
