from MiaKhalifaX.core.bot import MiaKhalifaXBot
from MiaKhalifaX.core.dir import dirr
from MiaKhalifaX.core.git import git
from MiaKhalifaX.core.userbot import Userbot
from MiaKhalifaX.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = MiaKhalifaXBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
