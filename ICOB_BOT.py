from pyrogram import Client, Filters

ICOB_BOT = Client(
    api_id="",          #https://my.telegram.org/apps den alabilirsiniz
    api_hash ="",       #https://my.telegram.org/apps den alabilirsiniz
    session_name = "",  #Burayı sallayabilirsiniz :D               
    bot_token = "",     #botfather dan alabilirsiniz.
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
🤖 /notlar
🤖 /not
"""

    merhaba.edit(mesaj)

ICOB_BOT.run()
