import os
import asyncio
from pyrogram import Client, compose, filters, enums
import re
from pyrogram.types import *

plugins = dict(root="helper")


api_id = 12380656
api_hash = "d927c13beaaf5110f25c505b7c071273"
bot_token = "6479300434:AAFJP-O_OBuXzoRrQRMBrbmZeBequL1EVJA"

for file in os.listdir():
    if file.endswith(".session"):
        os.remove(file)
for file in os.listdir():
    if file.endswith(".session-journal"):
        os.remove(file)
        
async def main():
    app = Client(
    name = "KAALWARE",
    api_id = api_id,
    api_hash = api_hash,
    bot_token = bot_token,
    plugins=plugins,
)
    app.set_parse_mode(enums.ParseMode.HTML)


@app.on_message(filters.command(["start", "help"], ["/", "!", "."]))
async def start_message(client, message):
    await message.reply_text(f"Hello, {message.from_user.mention}")


@app.on_message(filters.command(["pic"], ["/", "!", "."]) & filters.private)
async def start_photo(client, message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7d6675f32fd14d710ebc9.jpg",
        caption="**Hi, I am A New Robot For Telegram**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="😎 Owner",
                        url=f"https://t.me/iamkaal",
                    ),
                    InlineKeyboardButton(
                        text="🤓 Updates",
                        url=f"https://t.me/Kaalware",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="😎 Support",
                        url=f"https://t.me/kaalgram",
                    ),
                ],
           ],
        )
    )
    

print("Done Bot Active ✅")

    await compose(clients)


asyncio.run(main())
