# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# ported from Ultroid by @Zal
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import asyncio
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.ftyping (.*)")
async def _(v):
    l = v.pattern_match.group(1)
    if not (l or l.isdigit()):
        l = 100
    else:
        try:
            l = int(l)
        except BaseException:
            try:
                l = await ban_time(v, l)
            except BaseException:
                return await v.edit( "`Incorrect Format`")
    await v.edit(f"Starting Fake Typing For {l} sec.")
    async with v.client.action(v.chat_id, "typing"):
        await asyncio.sleep(l)


@register(outgoing=True, pattern="^.faudio (.*)")
async def _(v):
    l = v.pattern_match.group(1)
    if not (l or l.isdigit()):
        l = 100
    else:
        try:
            l = int(l)
        except BaseException:
            try:
                l = await ban_time(v, l)
            except BaseException:
                return await v.edit("`Incorrect Format`")
    await v.edit(f"Starting Fake audio recording For {l} sec.")
    async with v.client.action(v.chat_id, "record-audio"):
        await asyncio.sleep(l)


@register(outgoing=True, pattern="^.fvideo (.*)")
async def _(v):
    l = v.pattern_match.group(1)
    if not (l or l.isdigit()):
        l = 100
    else:
        try:
            l = int(l)
        except BaseException:
            try:
                l = await ban_time(v, l)
            except BaseException:
                return await v.edit("`Incorrect Format`")
    await v.edit(f"Starting Fake video recording For {l} sec.")
    async with v.client.action(v.chat_id, "record-video"):
        await asyncio.sleep(l)


@register(outgoing=True, pattern="^.fgame (.*)")
async def _(v):
    l = v.pattern_match.group(1)
    if not (l or l.isdigit()):
        l = 100
    else:
        try:
            l = int(l)
        except BaseException:
            try:
                l = await ban_time(v, l)
            except BaseException:
                return await v.edit("`Incorrect Format`")
    await v.edit(f"Starting Fake Game Playing For {l} sec.")
    async with v.client.action(v.chat_id, "game"):
        await asyncio.sleep(l)

CMD_HELP.update(
    {
        "fakeaction": ".ftyping\
\nUsage: Untuk Melakukan Fake Type.\
\n\n.faudio\
\nUsage: Untuk Melakukan Fake Audio.\
\n\n.fvideo\
\nUsage: Untuk Melakukan Fake Video.\
\n\n.fgame\
\nUsage: Untuk Melakukan Fake Game."
    }
)


