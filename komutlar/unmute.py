
from pyrogram import Client, Filters, ChatPermissions


@Client.on_message(Filters.command(["unmute"]))
def unmute(client, message):
    yetkiler = ("creator", "administrator")
    mesaj = message.text
    mesaj1 = mesaj.split()

    if message.chat.type != "private":
        if message.reply_to_message:
            if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                if client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["until_date"]:
                    client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_invite_users=True,
                        can_add_web_page_previews=True,
                        can_send_polls=True,
                        can_send_other_messages=True,
                        can_pin_messages=True,
                        can_change_info=True))
                    message.reply(f"@{message.reply_to_message.from_user.username} sesi açıldı.")
                else:message.reply("Kullanıcının zaten sesi açık.")
            else:message.reply("siz yönetici değilsiniz.")
        
        elif "@" in mesaj:
            if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                try:client.get_chat_member(message.chat.id, mesaj1[1])
                except:message.reply(f"{mesaj1[1]} isminde bir kullanıcı bulunamadı.");quit()
                if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"]:
                    client.restrict_chat_member(message.chat.id, mesaj1[1],  ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_invite_users=True,
                        can_add_web_page_previews=True,
                        can_send_polls=True,
                        can_send_other_messages=True,
                        can_pin_messages=True,
                        can_change_info=True))
                            
                    message.reply(f"{mesaj1[1]} kullanıcının sesi açıldı.")
                else:message.reply("Kullanıcının zaten sesi açık.")
            else:message.reply("siz yönetici değilsiniz.")

        else:
            if len(mesaj1) == 2:
                if len(mesaj1[1]) == 9:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj1[1])
                        except:message.reply(f"Kullanıcı bulunamadı.");quit()
                        print(client.get_users(mesaj1[1]))
                        if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"]:
                            client.restrict_chat_member(message.chat.id, mesaj1[1],  ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_invite_users=True,
                        can_add_web_page_previews=True,
                        can_send_polls=True,
                        can_send_other_messages=True,
                        can_pin_messages=True,
                        can_change_info=True))
                            message.reply(f"""[{client.get_users(mesaj1[1])["first_name"]}](tg://user?id={mesaj1[1]})[{mesaj1[1]}] sesi açıldı.""")
                        else:message.reply("Kullanıcının sesi zaten açık.")
                    else:message.reply("Siz yönetici değilsiniz.")
                else:message.reply("/unmute komutunu mesaj yanıtlayarak veye kullanıcının id/username bilgilerini girerek kullanınız.")
            else:message.reply("/unmute komutunu mesaj yanıtlayarak veye kullanıcının id/username bilgilerini girerek kullanınız.")
    else:message.reply("Burası özel sohbet.")

