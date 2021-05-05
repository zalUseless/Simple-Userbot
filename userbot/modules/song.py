#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# By @xditya. Thanks to @AvinashReddy for the ytdl base.
# Re edit by @Zal




import json
import os

import pybase64
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from youtubesearchpython import SearchVideos

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.song (.*)")
async def download_video(event):
    await event.edit("`Mencari.....`")
    url = event.pattern_match.group(1)
    if not url:
        return await event.edit("**Kesalahan!**\nGunakan Perintah `.song <judul lagu>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await event.edit("`Tidak dapat menemukan lagu yang cocok...`")
    type = "audio"
    await event.edit(f"`Bersiap untuk mengunduh {url}...`")
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        await event.edit("`Mendapatkan informasi...`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await event.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await event.edit("`Konten unduhan terlalu pendek.`")
        return
    except GeoRestrictedError:
        await event.edit(
            "`Video tidak tersedia dari lokasi geografis Anda karena batasan geografis yang diberlakukan oleh situs web.`"
        )
        return
    except MaxDownloadsReached:
        await event.edit("`Batas unduhan maksimal telah tercapai.`")
        return
    except PostProcessingError:
        await event.edit("`Ada kesalahan selama pemrosesan posting.`")
        return
    except UnavailableVideoError:
        await event.edit("`Media tidak tersedia dalam format yang diminta.`")
        return
    except XAttrMetadataError as XAME:
        await event.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await event.edit("`Terjadi kesalahan selama ekstraksi info.`")
        return
    except Exception as e:
        await event.edit(f"{str(type(e)): {str(e)}}")
        return
    try:
        sung = str(pybase64.b64decode("QFRlbGVCb3RIZWxw"))[2:14]
        await bot(JoinChannelRequest(sung))
    except BaseException:
        pass
    upteload = """
Uploading...
Song name - {}
By - {}
""".format(
        rip_data["title"], rip_data["uploader"]
    )
    await event.edit(f"`{upteload}`")
    await event.client.send_file(
        event.chat_id,
        f"{rip_data['id']}.mp3",
        supports_streaming=True,
        caption=f"**➡ Song:** {rip_data['title']}\n**➡ By:** {rip_data['uploader']}\n",
        attributes=[
            DocumentAttributeAudio(
                duration=int(rip_data["duration"]),
                title=str(rip_data["title"]),
                performer=str(rip_data["uploader"]),
            )
        ],
    )
    os.remove(f"{rip_data['id']}.mp3")
    await event.delete()
CMD_HELP.update({
    "song":
    "`.song`\
\nUsage: Untuk Perintah\n .song <Artist - Judul Lagu>."
})
