
from bot import Bot
import html
from pyrogram.types import Message
from pyrogram import filters, enums
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)

    class Link(str):
        HTML = "<a href={url}>{text}</a>"
        MARKDOWN = "[{text}]({url})"

        def __init__(self, url: str, text: str, style: enums.ParseMode):
            super().__init__()

            self.url = url
            self.text = text
            self.style = style

        @staticmethod
        def format(url: str, text: str, style: enums.ParseMode):
            if style == enums.ParseMode.MARKDOWN:
                fmt = Link.MARKDOWN
            else:
                fmt = Link.HTML

            return fmt.format(url=url, text=html.escape(text))

        # noinspection PyArgumentList
        def __new__(cls, url, text, style):
            return str.__new__(cls, Link.format(url, text, style))

        def __call__(self, other: str = None, *, style: str = None):
            return Link.format(self.url, other or self.text, style or self.style)

        def __str__(self):
            return Link.format(self.url, self.text, self.style)

    @property
    def mention(self):
        return Link(
            f"tg://user?id={self.id}",
            self.first_name or "Deleted Account",
            self._client.parse_mode
        )