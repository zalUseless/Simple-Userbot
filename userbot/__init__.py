# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot initialization. """


import os
import re
import asyncio
import time
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil
from platform import python_version
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from dotenv import load_dotenv
from telethon import version
from telethon.sync import TelegramClient, custom, events
from telethon.sessions import StringSession

load_dotenv("config.env")

StartTime = time.time()

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get(
    "CONSOLE_LOGGER_VERBOSE") or "False")

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info(
        "You MUST have a python version of at least 3.8."
        "Multiple features depend on this. Bot quitting."
    )

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = (os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________") or None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = os.environ.get("API_KEY")
API_HASH = os.environ.get("API_HASH")


# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", 0))

#Botlog
BOTLOG = sb(os.environ.get("BOTLOG", "False"))

# Userbot logging feature switch.
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False")) if BOTLOG_CHATID else False
# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Genius lyrics get this value from https://genius.com/developers both has
# same values
GENIUS = os.environ.get("GENIUS_API_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL", "https://github.com/rizgustiadi/Simple-Userbot.git")
UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "master")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get(
    "CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))


# Send .chatid in any group with all your administration bots (added)
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", None)
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Default .alive logo
ALIVE_LOGO = os.environ.get("ALIVE_LOGO", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API is not None:
    lastfm = LastFMNetwork(
        api_key=LASTFM_API,
        api_secret=LASTFM_SECRET,
        username=LASTFM_USERNAME,
        password_hash=LASTFM_PASS,
    )
else:
    lastfm = None

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
    "TMP_DOWNLOAD_DIRECTORY", "./downloads/")

# Terminal alias
TERM_ALIAS = os.environ.get("TERM_ALIAS", "UserButt")

# Zipfile module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

# Uptobox
USR_TOKEN = os.environ.get("USR_TOKEN_UPTOBOX", None)


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)


async def check_botlog_chatid():
    if not BOTLOG_CHATID:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        quit(1)


async def send_alive_status():
    if BOTLOG_CHATID:
        message = (
            "**Bot is up and running!**\n\n"
            f"**Telethon:** {version.__version__}\n"
            f"**Python:** {python_version()}\n"
            f"**User:** {ALIVE_NAME or 'Set `ALIVE_NAME` ConfigVar!'}"
        )
        await bot.send_message(BOTLOG_CHATID, message)
        return True



# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
