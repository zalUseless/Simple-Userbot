from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern=r"^\.dare(?: |$)(.*)")
async def _(kontol):
    if kontol.fwd_from:
        return
    chat = "@truthordares_bot"  # pylint:disable=E0602
    tolol = f"dare"  # pylint:disable=E0602
    await kontol.edit("Tunggu Bro... ")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1335899453))
            await conv.send_message(f'/{tolol}')
            response = await response
        except YouBlockedUserError:
            await kontol.reply("Unblock @truthordares_bot dulu Goblok!!")
            return
        else:
            await kontol.edit(f"{response.message.message}")
            await kontol.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.truth(?: |$)(.*)")
async def _(kontol):
    if kontol.fwd_from:
        return
    chat = "@truthordares_bot"  # pylint:disable=E0602
    tolol = f"truth"  # pylint:disable=E0602
    await kontol.edit("Tunggu Bro... ")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1335899453))
            await conv.send_message(f'/{tolol}')
            response = await response
        except YouBlockedUserError:
            await kontol.reply("Unblock @truthordares_bot dulu Goblok!!")
            return
        else:
            await kontol.edit(f"{response.message.message}")
            await kontol.client.delete_messages(response.message.message
CMD_HELP.update(
    {"truthdare": "`.dare`\
    \nUsage: tantangan.\
    \n\n `truth`\
    \nUsage: kejujuran."})
