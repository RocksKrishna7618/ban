import os
import logging 
from pyrogram import Client
from config import Config 

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)


ENV = bool(os.environ.get("ENV",False))

if ENV:
    API_ID=int(os.environ.get("API_ID","28422427"))
    API_HASH=str(os.environ.get("API_HASH","9d83e9bc46cab0c6793faebbd324d4e3"))
    TOKEN=str(os.environ.get("TOKEN","5867205386:AAE-fbedTagRGqHcmaJ7a1Cm9seeQTp-mo8"))
    SUDO = list(int(i) for i in os.environ.get("SUDO", "5314932005").split(" "))
    START_IMG=str(os.environ.get("START_IMG","https://te.legra.ph/file/4dfa9b6a0305653017978.jpg"))
    BOT_ID=int(os.environ.get("BOT_ID","5867205386"))
    BOT_USERNAME=str(os.environ.get("BOT_USERNAME","BanAllRobot"))
    BOT_NAME=str(os.environ.get("BOT_NAME","ʀᴏᴄᴋs ꭙ ʙᴀɴᴀʟʟ"))

else:
    API_ID=Config.API_ID
    API_HASH=Config.API_HASH
    TOKEN=Config.TOKEN
    SUDO=Config.SUDO
    START_IMG=Config.START_IMG
    BOT_ID=Config.BOT_ID
    BOT_USERNAME=Config.BOT_USERNAME
    BOT_NAME=Config.BOT_NAME



app=Client(
    "BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="BanAllBot/modules")
     )

LOG.info("starting the bot....")
