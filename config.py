import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2084663879:AAF9zfggaReMdNUdzOmhemaiuY6JE3Gb0S0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", " 8462643"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d0f14718be2962e38d935b06c8f70d25")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001548813220"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2091292823"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://dvqbzihwaqhqvo:b0644ede1af86de59f9ee6fd52c03441de737d9012aec1cd274e27c111d4a5f2@ec2-3-222-24-178.compute-1.amazonaws.com:5432/d2fov25qttdva5")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first} {username} just tap the lin")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "2076466857").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

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
