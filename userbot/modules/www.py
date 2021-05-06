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
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Running high speed test . . .`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("`"
                   "Started at "
                   f"{result['timestamp']} \n\n"
                   "Download "
                   f"{speed_convert(result['download'])} \n"
                   "Upload "
                   f"{speed_convert(result['upload'])} \n"
                   "Ping "
                   f"{result['ping']} \n"
                   "ISP "
                   f"{result['client']['isp']}"
                   "`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"



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
