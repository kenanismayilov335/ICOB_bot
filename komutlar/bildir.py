from pyrogram import Client, Filters

@Client.on_message(Filters.command(["bildir"]))
def bildir(client, message):
    aciklama = " ".join(message.text.split()[1:])
    if len(aciklama) == 0:aciklama = "Yok"

    if message.chat.type != "private":
        yetkiler = ("creator", "administrator")
        if message.reply_to_message:
            if message.from_user.id == message.reply_to_message.from_user.id:
                message.reply("Kendini mi bildirmek istiyosun 🙄")
            
            elif client.get_chat_member(message.chat.id, message.from_user.id).status in yetkiler:
                message.reply("Sen zaten yöneticisin. Kendine mi mesaj atmak istiyorsun 🙄")
    
            else:
                for uye in client.iter_chat_members(message.chat.id):
                    if uye.user.is_bot == False:
                        if uye.status == "creator" or uye.status == "administrator":
                            client.send_message(uye.user.id, """[{}](tg://user?id={})[`{}`] kullanıcı **__{}__** grubundaki bir mesajı bildirdi.\n\n**__Bildirilen Kişi__**;\nUsername : **__{}__**\nID : **__{}__**\nİsim : **__{}__**\nSoyad : **__{}__**\n\n📂 Açıklama : **__{}__**\n\n            **MESAJ**\n👇👇👇👇👇👇""".format(
                                message.from_user.first_name, message.from_user.id, message.from_user.id, message.chat.title, message.reply_to_message.from_user.username, message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.last_name, aciklama                                 
                            ))
                            client.forward_messages(uye.user.id, message.chat.id, message.reply_to_message.message_id, as_copy=True)
                            message.reply("Mesaj yöneticilerimize bildirilmiştir.")
                        else:pass
                    else:pass
        else:message.reply("Lütfen bildirmek istediğiniz mesajı yanıtlayınız.")
    else:message.reply("Özel sohbet bizi ilgilendirmez. :D")
