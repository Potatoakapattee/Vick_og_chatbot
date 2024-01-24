

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import PNG_BTN


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://graph.org/file/207b09c0651067ad3252b.jpg",
    "https://graph.org/file/3b9e361a201ecb663d18b.jpg",
    "https://graph.org/file/5a3aba4997e713a94219f.jpg",
    "https://graph.org/file/8482d5016e0aeb304719a.jpg",
    "https://graph.org/file/81ca30f2b28868b395455.jpg",
    "https://graph.org/file/bd1c9ef3b4b595735fdfc.jpg",
    "https://graph.org/file/b6d0b6c34d6153b20395f.jpg",
    "https://graph.org/file/6f0ea4516ae065c2af53d.jpg",
    "https://graph.org/file/6a3903664bd0812f8d66c.jpg",
    "https://graph.org/file/9ef5693d35cc4db0444aa.jpg",
    "https://graph.org/file/e49b855fc1da045117198.jpg",
    "https://graph.org/file/c21d04cb26a9aa37eb3f7.jpg",
    "https://graph.org/file/512ce133a0775f869c025.jpg",
    "https://graph.org/file/54d05af6abe9c6846ba8c.jpg",
]


#----------------IMG-------------#

#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#



@nexichat.on_cmd("ping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{nexichat.name} ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>|| мαdє ωιтн ❣️ ву [Decent Boy❣️](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
