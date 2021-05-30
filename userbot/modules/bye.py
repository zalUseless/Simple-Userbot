""" Userbot module for other small commands. """
import sys
from userbot import CMD_HELP,USERS,bot
from userbot.events import register


@register(outgoing=True, pattern="^.bye$")
async def shalom(e):
    global USERS
    user = await bot.get_me()
    user.username = user.first_name
    await e.edit(f"[{user.first_name}](tg://user?id={user.id}) Has Left The Chat")
    CMD_HELP.update(
        {
            "Bye": ".bye\
\nUsage: gives a nice Gitub Page as output."
        }
    )
