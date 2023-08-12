import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","9181844"))
API_HASH = getenv("API_HASH", "996a3e7194a4f07576fda5c20bb1138b")

BOT_TOKEN = getenv("BOT_TOKEN", "6596067451:AAGuBksuIrnI-YfgZHm7ZM7VTOsEbMO9XuA")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://timedb:timedb@cluster0.hwgu2mk.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001575025353"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "◄⏤͟͞ ⍣⃟💋⃟𝄟⃝🤍🇲𝑖𝑎 🇰ℎ𝑎𝑙𝑖𝑓𝑎 𝓜𝓾𝓼𝓲𝓬𐏓⍣⃟🌸࿐﹡")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5882743383").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/mukeshmoni/keerthu-music")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", "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")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/miiakhalifamusic_support")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/miiakhalifamusic_support")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "4800000000000000000000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "780000000000000000000"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "cf6365361b7041b4a51036553acd9d4f" )
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "8b96133fe3d942faae5066be2f3cde91")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "50000000000000000000000"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "1500000000000000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500000000000000000000000000000000"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQACS6WkP5Uw-ZH-2YmQocjj6ye1BdLoEbJpMcAWB79Js6g0H1o5gT5HYTC0zCXQGSlXDU4_S4YCYWp_0XG-0S884Po8_hsiYBjgfOotCqdA0s6Y1ZVpvnm74NREZMJ4HphwE6qTkEjElox9-BVCN_IJ6GV_wah63v1zymuyJH98ROUVtByJTpqNg1Pkl__ewc4AYXYgF8PwSrALAw16_J-AMnd92AlkgnaCHyR7U4gxgGstAuQbp9Q0Z9fdvDmOer5MXAzYUs_LfZ3-b73dNgrWK-LEwWl-zyoYQUKsevzbxXaQFpYdPpcfsT1DLO8rXnMZSBqn-vR2EWPebI_BV2DkAAAAAUbI32AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/86d893ccb24d1baebe8f9.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph//file/bc9e3b03da0293cfd51cb.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/e4e1651feae9e9b41d0a7.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/37d03ea1ab1e6c0463fc7.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/9328d46f0059672d696c6.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/093a2ba6885da2ce40f2c.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/0a88975d0f0185cdecafc.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/150b304ac04d79e384c22.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/150b304ac04d79e384c22.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/150b304ac04d79e384c22.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph//file/bc9e3b03da0293cfd51cb.jpg"
if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/12546684377a8bfd84100.jpg"
