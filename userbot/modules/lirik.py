from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern=r"^\.lirik(?: |$)(.*)")
async def _(goblok):
    if goblok.fwd_from:
        return
    song = goblok.pattern_match.group(1)
    chat = "@iLyricsBot"  # pylint:disable=E0602
    lirik = f"start"  # pylint:disable=E0602
    await goblok.edit("Tunggu Bro... ")
    async with bot.conversation("@iLyricsBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=232268607))
            await conv.send_message(f'/{lirik}')
            response = await response
            await conv.send_message(f'{song}')
            response = await response
        except YouBlockedUserError:
            await goblok.reply("Unblock @iLyricsBot dulu Goblok!!")
            return
        else:
            await goblok.edit(f"{response.message.message}")
            await goblok.client.delete_messages(response.message.message)
CMD_HELP.update({"lirik": "`.lirik <judul - penyanyi>`" "\nUsage: Untuk Memcari Lirik Lagu."})
