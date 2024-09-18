from aiohttp import web
import config
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from pytz import timezone

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
        self.started = False

    async def start(self):
        self.LOGGER(__name__).info("Starting bot")
        if self.started:
            self.LOGGER(__name__).info("Bot already started")
            return

        self.started = True
        print("Debug: Entering start method")
        await super().start()
        print("Debug: After super().start()")
        me = await self.get_me()
        self.LOGGER(__name__).info(f"Bot started as @{me.username}")
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        self.mention = me.mention
        self.username = me.username

        print(f"\033[1;96m @{me.username} Sᴛᴀʀᴛᴇᴅ......⚡️⚡️⚡️\033[0m")
        try:
            await self.send_message(config.ADMINS[0], f"**__{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
            self.LOGGER(__name__).info("Startup message sent to admin")
        except Exception as e:
            self.LOGGER(__name__).error(f"Error sending message to admin: {e}")
        except:
            pass

        if config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time_str = curr.strftime('%I:%M:%S %p')
                await self.send_message(
                    config.LOG_CHANNEL,
                    f"**__{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time_str}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`</b>"
                )
            except Exception as e:
                print(f"Error sending message to log channel: {e}")

            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")


        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).info("Reached this point in the bot logic")

                self.LOGGER(__name__).warning("ʙᴏᴛ ᴄᴀɴ'ᴛ ᴇxᴘᴏʀᴛ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ꜰʀᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ!")
                self.LOGGER(__name__).warning(f"ᴘʟᴇᴀꜱᴇ ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ FORCE_SUB_CHANNEL ᴠᴀʟᴜᴇ ᴀɴᴅ ᴍᴀᴋᴇ ꜱᴜʀᴇ ʙᴏᴛ ɪꜱ ᴀᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜꜱᴇʀꜱ ᴠɪᴀ ʟɪɴᴋ ᴘᴇʀᴍɪꜱꜱɪᴏɴ, ᴄᴜʀʀᴇɴᴛ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ ᴠᴀʟᴜᴇ: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nʙᴏᴛ ꜱᴛᴏᴘᴘᴇᴅ. ᴊᴏɪɴ https://t.me/OnAnimeSeries ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛ")
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("ʙᴏᴛ ᴄᴀɴ'ᴛ ᴇxᴘᴏʀᴛ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ꜰʀᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ 2 ᴄʜᴀɴɴᴇʟ!")
                self.LOGGER(__name__).warning(f"ᴘʟᴇᴀꜱᴇ ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ FORCE_SUB_CHANNEL2 ᴠᴀʟᴜᴇ ᴀɴᴅ ᴍᴀᴋᴇ ꜱᴜʀᴇ ʙᴏᴛ ɪꜱ ᴀᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜꜱᴇʀꜱ ᴠɪᴀ ʟɪɴᴋ ᴘᴇʀᴍɪꜱꜱɪᴏɴ, ᴄᴜʀʀᴇɴᴛ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ ᴠᴀʟᴜᴇ:{FORCE_SUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nʙᴏᴛ ꜱᴛᴏᴘᴘᴇᴅ. ᴊᴏɪɴ https://t.me/OnAnimeSeries ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛ")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"ᴍᴀᴋᴇ ꜱᴜʀᴇ ʙᴏᴛ ɪꜱ ᴀᴅᴍɪɴ ɪɴ ᴅʙ ᴄʜᴀɴɴᴇʟ, ᴀɴᴅ ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ CHANNEL_ID ᴠᴀʟᴜᴇ, ᴄᴜʀʀᴇɴᴛ ᴠᴀʟᴜᴇ {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nʙᴏᴛ ꜱᴛᴏᴘᴘᴇᴅ. ᴊᴏɪɴ https://t.me/OnAnimeSeries ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛ")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"\nhttps://t.me/OnAnimeSeries")
        self.LOGGER(__name__).info(f"""\n\n
         ____        _                   
        / ___|  __ _| |_ _   _ _ __ ___  
        \___ \ / _` | __| | | | '__/ _ \ 
         ___) | (_| | |_| |_| | | | (_) |
        |____/ \__,_|\__|\__,_|_|  \___/ 
                                        \n\n""")
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("stop")

