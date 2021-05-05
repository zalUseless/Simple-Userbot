""" Userbot module for other small commands. """
import sys
from userbot import CMD_HELP,USERS,bot
from userbot.events import register


@register(outgoing=True, pattern="^.repo$")
async def shalom(e):
    await e.edit(
        f"    🌪 My Repo 🌪\n\n"
        f" ➥ [TestBot](https://github.com/bambank9/testbot)\n"
        f" ┈┈┈╭━━━━━╮┈┈┈┈┈\n"
        f" ┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
        f" ┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
        f" ┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
        f" ┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
        f" ┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
        f" ┈┈┈┃┊┃╰━━┫┈\n" 
        f" ┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")
    CMD_HELP.update(
        {
            "repo": ".repo\
\nUsage: repo for bambank."
        }
    )
