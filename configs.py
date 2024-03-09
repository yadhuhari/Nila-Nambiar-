# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("19383278"))
	API_HASH = os.environ.get("6e6c8100d5564c59bfd82a7a86aadb95")
	BOT_TOKEN = os.environ.get("6711470972:AAHZWOlCGp-TgqQ0ic_RS3UUvpqlh5w4lrk")
	BOT_USERNAME = os.environ.get("MDCNilaBot")
	DB_CHANNEL = int(os.environ.get("-1002065818511"))
	BOT_OWNER = int(os.environ.get("7127020589"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
**Nᴏᴛʜɪɴɢ ഇതിൽ ലൈറ്റ് കത്തും..!**
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @MDCAdminRobot 
"""
	HOME_TEXT = f"""
**Hᴇʏ ᴛʜᴇʀᴇ [{}](tg://user?id={}) 🙌

I ᴀᴍ Nɪʟᴀ Nᴀᴍʙɪᴀᴇʀ,  A Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ ᴡᴏʀᴋɪɴɢ ғᴏʀ Mᴀʟᴀʏᴀʟᴀᴍ Dᴜʙʙɪɴɢ Cᴏᴍᴍᴜɴɪᴛʏ. Oɴʟʏ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴍᴇ. Sᴏ ᴅᴏɴ'ᴛ ᴡᴀsᴛᴇ ʏᴏᴜʀ ᴛɪᴍᴇ 😊**"""
