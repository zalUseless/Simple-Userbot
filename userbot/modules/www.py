# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime
from asyncio import sleep
from speedtest import Speedtest
from . import *
from userbot import CMD_HELP, StartTime, bot, USERS
from userbot.events import register
import time
async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.speed$")
async def _(event):
    input_str = event.pattern_match.group(1)
    as_text = True
    as_document = False
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    xx = await eor(event, "`Calculating ur Ultroid Server Speed. Please wait!`")
    start = datetime.now()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()  # dchehe
    end = datetime.now()
    ms = (end - start).seconds
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        reply_msg_id = event.reply_to_msg_id
    try:  # heheh
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await xx.edit(
                """`Simple-Userbot Server Speed in {} sec`
`Download: {}`
`Upload: {}`
`Ping: {}`
`Internet Service Provider: {}`
`ISP Rating: {}`""".format(
                    ms,
                    convert_from_bytes(download_speed),
                    convert_from_bytes(upload_speed),
                    ping_time,
                    i_s_p,
                    i_s_p_rating,
                )
            )
        else:
            await event.client.send_file(
                event.chat_id,
                speedtest_image,  # heeehe
                caption="**SpeedTest** completed in {} seconds".format(ms),
                force_document=as_document,
                reply_to=reply_msg_id,
                allow_cache=False,
            )
            await event.delete()
    except Exception as exc:  # dc
        await xx.edit(
            """**SpeedTest** completed in {} seconds
Download: {}
Upload: {}
Ping: {}
__With the Following ERRORs__
{}""".format(
                ms,
                convert_from_bytes(download_speed),
                convert_from_bytes(upload_speed),
                ping_time,
                str(exc),
            )
        )


def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {0: "", 1: "kilobytes", 2: "megabytes", 3: "gigabytes", 4: "terabytes"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"

@register(outgoing=True, pattern="^.pink$")
async def pingme(pong):
    """ For .pink command, ping the userbot from any chat.  """
    global USERS
    user = await bot.get_me()
    user.name = user.first_name
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(
        "Wait.....0%")
    await pong.edit(
        "Wait.....5%")
    await pong.edit(
        "Wait.....10%")
    await pong.edit(
        "Wait.....15%")
    await pong.edit(
        "Wait.....20%")
    await pong.edit(
        "Wait.....25%")
    await pong.edit(
        "Wait.....30%")
    await pong.edit(
        "Wait.....35%")
    await pong.edit(
        "Wait.....40%")
    await pong.edit(
        "Wait.....45%")
    await pong.edit(
        "Wait.....50%")
    await pong.edit(
        "Wait.....55%")
    await pong.edit(
        "Wait.....60%")
    await pong.edit(
        "Wait.....65%")
    await pong.edit(
        "Wait.....70%")
    await pong.edit(
        "Wait.....75%")
    await pong.edit(
        "Wait.....80%")
    await pong.edit(
        "Wait.....85%")
    await pong.edit(
        "Wait.....90%")
    await pong.edit(
        "Wait.....95%")
    await pong.edit(
        "Wait.....100%")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"🌪 Simple-Userbot Ping 🌪\n➥ **PING** : %sms\n➥ **UPTIME** : {uptime}\n➥ **USER** : [{user.first_name}](tg://user?id={user.id})\n" % (duration))

CMD_HELP.update(
    {"ping": "`.pink`\
    \nUsage: Shows how long it takes to ping your bot.\
    \n\n`.speed`\
    \nUsage: Does a speedtest and shows the results."})
