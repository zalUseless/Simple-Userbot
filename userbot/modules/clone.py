# Ported from Telebot by @Zal
# Credits of Plugin @ViperAdnan and @mrconfused(revert)[will add sql soon]


import html
from userbot.events import register
from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot import (
     CMD_HELP, 
     bot, 
     TEMP_DOWNLOAD_DIRECTORY, 
     ALIVE_NAME, 
     DEFAULT_BIO
)


@register(outgoing=True, pattern="^clone(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    user_id = replied_user.user.id
    profile_pic = await event.client.download_profile_photo(user_id, TEMP_DOWNLOAD_DIRECTORY)
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their
        # names
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.user.last_name
    # last_name is not Manadatory in @Telegram
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    # inspired by https://telegram.dog/afsaI181
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = html.escape(replied_user.about)
    await bot(functions.account.UpdateProfileRequest(
        first_name=first_name
    ))
    await bot(functions.account.UpdateProfileRequest(
        last_name=last_name
    ))
    await bot(functions.account.UpdateProfileRequest(
        about=user_bio
    ))
    pfile = await bot.upload_file(profile_pic)  # pylint:disable=E060
    await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
        pfile
    ))
    #message_id_to_reply = event.message.reply_to_msg_id
    # if not message_id_to_reply:
    #    message_id_to_reply = event.message.id
    # await bot.send_message(event.chat_id,"Fuck Me Bitch?",reply_to=message_id_to_reply,)
    await event.delete()
    await bot.send_message(event.chat_id,"`Clone Sukses....`",reply_to=reply_message)



@register(outgoing=True, pattern="^revert(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    name = f"{ALIVE_NAME}"
    bio = f"{DEFAULT_BIO}"
    n = 1
    await bot(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=n)))
    await bot(functions.account.UpdateProfileRequest(about=bio))
    await bot(functions.account.UpdateProfileRequest(first_name=name))
    await event.edit("`Revert Sukses.... `")
    await event.delete()


async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.from_id or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.from_id
                )
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(
                    probable_user_mention_entity,
                    MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e



CMD_HELP.update(
    {"clone": "`clone`\
    \nUsage: Meng clone lonte.\
    \n\n`revert`\
    \nUsage: Kembali biar ga jadi lonte."})
