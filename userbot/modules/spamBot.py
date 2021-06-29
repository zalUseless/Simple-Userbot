from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern=r"^\.limit(?: |$)(.*)")
async def _(jesnolimit):
    if jesnolimit.fwd_from:
        return
    chat = "@SpamBot"  # pylint:disable=E0602
    limit = f"start"  # pylint:disable=E0602
    await jesnolimit.edit("Tunggu Bro... ")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{limit}')
            response = await response
        except YouBlockedUserError:
            await jesnolimit.reply("Unblock @SpamBot dulu Goblok!!")
            return
        else:
            await jesnolimit.edit(f"{response.message.message}")
            await jesnolimit.client.delete_messages(response.message.message)
CMD_HELP.update({"spamBot": "`.limit`\\nUsage: Untuk Melihat Limit Akun."})
