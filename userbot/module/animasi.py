# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for having some fun with people. """

from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
from PIL import Image
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.types import MessageMediaPhoto
import re
from urllib.request import urlopen
import time
import datetime
from collections import deque
import urllib
import requests
import io
import asyncio
import os
from bs4 import BeautifulSoup
from cowpy import cow

from userbot import bot, CMD_HELP, LOGS
from userbot.events import register
from userbot.modules.admin import get_user_from_event
"""
Available Commands:
.comli"""






@register(outgoing=True, pattern="^.bulan$")
async def moon(event):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    try:
        for _ in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return








@register(outgoing=True, pattern=r"^.(.*)")
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "comli":

        await event.edit(input_str)

        animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])
CMD_HELP.update(
    {
        "comli": ">`.comli`\
\nUsage:Comli Every Time.\
\n\n>`.bulan`\
\nUsage:Animasi bulan."
    }
)
