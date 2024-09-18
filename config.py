import os
import logging
from logging.handlers import RotatingFileHandler
import re, time
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7480704508:AAFTLThR9uW99NT96YtMhbM8Ni-6shUtJX8")

#Your API ID & API HASH from my.telegram.org [https://youtu.be/gZQJ-yTMkEo?si=H4NlUUgjsIc5btzH]
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9389796"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bdc43a2e0501624d3f0a491345a5ac84")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002001819513"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5197673717"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://OnAnimeSeries:OnAnimeSeries@filexonanimeseries.2lwf4gr.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "FileXOnAnimeSeries")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001877631854"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002090375801"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Shortner (token system)  check my discription to help by using my refer link of shareus.io
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "971f149c5c6978f6638759fe769a54bd695cf704")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/Ultroid_Official/18") # shareus ka tut_vid he 

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002169251162"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴀᴋᴋᴀᴀᴀ!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5197673717").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "{filename}\n\n {previouscaption} \n\n<b>• ʙʏ @OnAnimeSeries</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want To Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5197673717)



LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

