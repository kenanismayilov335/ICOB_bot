from pyrogram import Client, Filters

@Client.on_message(Filters.command(["ping"]))
def ping(client, message):
  message.reply("Ben çalışıyorum merak etme")

