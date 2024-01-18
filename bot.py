from pyrogram import Client
from pyrogram.types import Message
api_id = "27175683"
api_hash = "ff5bd7a1d985ad6e6db389e4ef104fe6"
bot_token = "6778102881:AAEJ0PvBN8qDjR3MqNSGNFWUXaLacuKbQ7Y"

app = Client(
    "kjjjkljklbot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message()
async def echo(client: Client, message: Message):
    await message.reply(message.text)

app.run()