from pyrogram import Client, Filters

ICOB_BOT = Client(
    api_id="",
    api_hash ="",    
    session_name = "",                 
    bot_token = "",
    plugins=dict(root="komutlar")
)


@ICOB_BOT.on_message(Filters.command(["start"], ["/", "."]))
def basla_mesaj(client, message):
    message.reply("Hoş geldin! \n/yardim komutuyla neler yapabildiğimi görebilirsin.")

@ICOB_BOT.on_message(Filters.command(["yardim"], ["/", "."]))
def yardim(client, message):
    merhaba = message.reply("Merhaba...")
    mesaj = """
Ben i-cob tarafından yazıldım\n
Komutlarım:\n
🤖 /google
🤖 /tdk
🤖 /imdb 
🤖 /instagram 
🤖 /doviz
🤖 /grub
🤖 /kullanici
🤖 /yukle
🤖 /youtube
🤖 /ban
🤖 /unban
🤖 /mute
🤖 /unmute
"""

    merhaba.edit(mesaj)

ICOB_BOT.run()
