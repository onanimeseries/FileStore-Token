#ultroidofficial : YT

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"""
<b>
  🫧ᴏᴡɴᴇʀ: <a href='tg://user?id={OWNER_ID}'>Ｓａｔｕｒｏ</a><br>
  ○ Channel: <a href='https://t.me/OnAnimeSeries'>ᴏɴ ᴀɴɪᴍᴇꜱᴇʀɪᴇꜱ</a><br>
  ○ 🇴🇺🇷 🇳🇪🇹🇼🇴🇷🇰 ⦂ <a href='https://t.me/OnAnimeSeries_Network'>ᴀɴɪᴍᴇꜱᴇʀɪᴇꜱ ɴᴇᴛᴡᴏʀᴋ</a><br>
  ○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ ⦂ <a href='https://t.me/OnAnimeseriesUniverse'>𝙰𝚗𝚒𝚖𝚎 𝚄𝚗𝚒𝚟𝚎𝚛𝚜𝚎</a><br>
  ○ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ: <a href='https://t.me/OnAnimeseries_Support'>​🇸​​🇺​​🇵​​🇵​​🇴​​🇷​​🇹​</a><br>
</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
