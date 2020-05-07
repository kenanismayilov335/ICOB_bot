from pyrogram import Client, Filters


@Client.on_message(Filters.command(["unban"]))
def unban(client, message):
    yetkiler = ("creator", "administrator")
    mesaj = message.text
    mesaj1 = mesaj.split()

    if message.chat.type != "private":
        if message.reply_to_message:
            if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                if client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["until_date"]:
                    client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                    message.reply(f"@{message.reply_to_message.from_user.username} banı kaldırıldı.")
                else:message.reply("kullanıcının banı yok")
            else:message.reply("siz yönetici değilsiniz.")
        
        elif "@" in mesaj:
            if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                try:client.get_chat_member(message.chat.id, mesaj1[1])
                except:message.reply(f"{mesaj1[1]} isminde bir kullanıcı bulunamadı.");quit()
                if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"]:
                    client.unban_chat_member(message.chat.id, mesaj1[1])
                    message.reply(f"{mesaj1[1]} kullanıcının banı kaldırıldı.")
                else:message.reply("Kullanıcının banı yok.")
            else:message.reply("siz yönetici değilsiniz.")

        else:
            if len(mesaj1) == 2:
                if len(mesaj1[1]) == 9:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj1[1])
                        except:message.reply(f"Kullanıcı bulunamadı.");quit()
                        print(client.get_users(mesaj1[1]))
                        if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"]:
                            client.unban_chat_member(message.chat.id, mesaj1[1])
                            message.reply(f"""[{client.get_users(mesaj1[1])["first_name"]}](tg://user?id={mesaj1[1]})[{mesaj1[1]}] ban kaldırıldı.""")
                        else:message.reply("Kullanıcının banı yok.")
                    else:message.reply("Siz yönetici değilsiniz.")
                else:message.reply("/unban komutunu mesaj yanıtlayarak veye kullanıcının id/username bilgilerini girerek kullanınız.")
            else:message.reply("/unban komutunu mesaj yanıtlayarak veye kullanıcının id/username bilgilerini girerek kullanınız.")
    else:message.reply("Burası özel sohbet.")

