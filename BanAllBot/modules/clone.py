from pyrogram import filters, Client
from BanAllBot import app, API_ID, API_HASH

@app.on_message(filters.private & filters.command("clone"))
async def _(app, message):
     reply = await message.reply("Usage:\n\n/clone <token>")
     token = message.command[1]
     try:
         await reply.edit("Booting Your Client")
         client=Client(
            "BOT",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            in_memory=True,
            plugins=dict(root="BanAllBot/modules")
         )
         await client.start()
         await reply.edit("Your Client Booted Successfully")
     except Exception as e:
         await reply.edit(f"Error:\n`{e}`")
