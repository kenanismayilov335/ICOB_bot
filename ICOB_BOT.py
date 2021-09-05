from pyrogram import Client, Filters

ICOB_BOT = Client(
    api_id="7319490",          #https://my.telegram.org/apps den alabilirsiniz
    api_hash ="3987ed5fcb72635ca4da8c5e93ec7493",       #https://my.telegram.org/apps den alabilirsiniz
    session_name = "AQBJjYTKWs3qtJOXXDIhq79q2vXMSgL8Y81h98G4JyL8CVqRa_JUIV54E20qsdcBRkzdm7_xKUHqrsCEpGDX7eEU5J9yY50ZnsnFCdSlwuG3RxIEt88vstparvPP84DfaY2Jgu0xcQWH1CHkl2ZEZ35QcfHlMariomHpV9qafbjSz6s63CwcAu3itzQg8C2agxGQkI_3PRNZUflCwyUpHz8uO8ifHmLjt3EtK2G2sOWbnNHwEbugc8xEhjjoNEEmP-Rb4Dxyi1K8pjGUzuZjazBuWOaX4JQ4HIqFIsV1Jx2HxDxTcSrrngSxoiHnKjPtW2m6PrUjVzUpsG64wGKjqKouVTEDbQA",
    bot_token = "1372871302:AAHRWzkOGm7dJdzJQefDJOqHyUsWrFzjPJE",     #botfather dan alabilirsiniz.
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
🤖 /admin 
🤖 /doviz
🤖 /kullanici
🤖 /bildir
🤖 /youtube
🤖 /iftar
🤖 /cevir
🤖 /ban
🤖 /unban
🤖 /mute
🤖 /unmute
🤖 /notlar
🤖 /not
"""

    merhaba.edit(mesaj)

ICOB_BOT.run()
