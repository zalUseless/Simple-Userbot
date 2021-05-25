# credits ultroid
# lorduserbot


from userbot.events import register
from userbot import CMD_HELP, bot

@register(outgoing=True, pattern="^.send (.*)")
async def bcast(event):
    a = event.pattern_match.group(1)
    if not a:
        return await event.edit("`Please Give A Message..`")
    b = event.text
    msg = b[6:]
    c = await event.edit("`Wait Is Sending Messages Globally....`")
    d = 0
    done = 0
    async for e in bot.iter_dialogs():
        if e.is_group:
            chat = e.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                d += 1
    await c.edit(f"**Successfully Sending Message To** `{done}` **Group, Failed To Send Message To** `{d}` **Group**")

CMD_HELP.update({"bcast": "`.send <pesan>`\
                \nPenjelasan: Global Broadcast mengirim pesan ke Seluruh Grup yang Lord Masuki."})
