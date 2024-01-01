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

print("Done Bot Active ✅")
asyncio.run(main())
