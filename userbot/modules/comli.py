"""
Available Commands:

.comli"""


import asyncio
from userbot import CMD_HELP
from userbot.events import register


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
            "comli": ".comli\
\nUsage: gives a nice Gitub Page as output."
        }
    )
