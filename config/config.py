import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "21944949"))
API_HASH = getenv("API_HASH", "d1abedd1624be80538e5d6da730f7963")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001898745590"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "˹ɪsʜᴜ ✘ ᴅɪʟ˼")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5382538422").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SAGAR1215g/IshuXDil")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tesyyai12345")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/tesyyai12345")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
 
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "90000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180000"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID","19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET","409e31d3ddd64af08cfcc3b0f064fcbe")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION","BQBm7Na3j-s-BEfkHuy3ZkjKa4jNtQhOm-g72BYb80wptL8C1KEjv-rAGJcNMVe2452qd5UPFSvuXoSw9M6-lw1QDSOSBvWR5SFobpH1q2DYa7Q2qkxlPMTfh434uVWMoXEhXn1GJ2Dsv5onnJwO42J12rSPsmaJEv4Dc-g2qvK8XxbOa1KPJ7KHovnkTdkCzx4ODxum7E14TOuWQGtAZPS7KPVXrmQ6dWlwSQrXUz_hFCYMCx1roJrcewdOqtJeZQczVO2OXzrF7ss33MlUSqW0o2HKCj3jkxoGdrn2BZ_3ldlzqE7xaAd8_IKP5-0g1LgWbaei8tT1KzJ13V-VG_K3AAAAAUNUBBQA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "AarohiXlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"


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
            PING_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/ac786e3464ecf452acf6d.jpg"
