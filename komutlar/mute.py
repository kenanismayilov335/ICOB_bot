from pyrogram import Client, Filters, ChatPermissions
from datetime import datetime
import time



def zaman(metin):
    if "gün" in metin:
        metin = metin.replace("gün", "")
        try:return int(int(metin) * 24 * 60 * 60)
        except:return False
    elif "saat" in metin:
        metin = metin.replace("saat", "")
        try:return int(int(metin) * 60 * 60)
        except:return False

    elif "dk" in metin:
        metin = metin.replace("dk", "")
        try:return int(int(metin) * 60)
        except:return False
    else:return False

@Client.on_message(Filters.command(["mute"]))
def mute(client, message):
    mesaj = message.text
    yetkiler = ("creator", "administrator")
    if message.chat.type != "private":
        if message.reply_to_message:
            sure = message.text.split()
            if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                try:client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                except:message.reply("Maalesef yanıtladığınız mesajı atan kullanıcı grubtan çıkmış.");quit()
                if client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["until_date"] == None:
                    if client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["status"] not in yetkiler:
                        if len(sure) == 1:
                            client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(), 0)
                            if message.reply_to_message.from_user.username:
                                message.reply(f"@{message.reply_to_message.from_user.username}[{message.reply_to_message.from_user.id}] sessize alındı.")
                            else:
                                message.reply(f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})[{message.reply_to_message.from_user.id}] sessize alındı.")
                        elif len(sure) > 2:
                            message.reply("""Lütfen komutu "**__/mute 5dk/1gün/10saat__**" şeklinde giriniz. """) 
                        else:
                            if zaman(sure[1]) == False:
                                message.reply("""Lütfen komutu "**__/mute 5dk/1gün/10saat__**" şeklinde giriniz. """) 
                            else:
                                client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(), int(time.time() + zaman(sure[1])))
                                if message.reply_to_message.from_user.username:
                                    message.reply(f"@{message.reply_to_message.from_user.username}[{message.reply_to_message.from_user.id}] {sure[1]} süreyle sessize alındı.")
                                else:
                                    message.reply(f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})[{message.reply_to_message.from_user.id}] {zaman(sure[1])} süreyle sessize alındı.")
                    else:message.reply("Sessize almak istediğiniz kişi yönetici.")
                else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["until_date"])}__** süresine kadar sessizde.""")
            else:message.reply("Birisini sessize almak için yönetici olman gerekir.")
        elif "@" in mesaj:    
            mesaj1 = mesaj.split()
            if len(mesaj1) == 2:    
                if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                    try:client.get_chat_member(message.chat.id, mesaj1[1])
                    except:message.reply(f"Bu grupta {mesaj1[1]} isimli bir kullanıcı bulunamadı.");quit()
                    if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj1[1])["status"] not in yetkiler:
                            client.restrict_chat_member(message.chat.id, mesaj1[1], ChatPermissions())
                            message.reply(f"{mesaj1[1]} sessize alındı.")
                        else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                    else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[1])["until_date"])}__** süresine kadar sessizde.""")
                else:message.reply("Birini sessize almak için yönetici olmanız lazım.")

            elif len(mesaj1) == 3:
                if "@" in mesaj1[1]:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj1[1])
                        except:message.reply(f"Bu grupta {mesaj1[1]} isimli bir kullanıcı bulunamadı.");quit()
                        if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"] == None:
                            if client.get_chat_member(message.chat.id, mesaj1[1])["status"] not in yetkiler:
                                if zaman(mesaj1[2]) == False:
                                    message.reply("""Lütfen komutu "**__/mute @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")
                                else:
                                    client.restrict_chat_member(message.chat.id, mesaj1[1], ChatPermissions(), int(time.time() + zaman(mesaj1[2])))
                                    message.reply(f"""{mesaj1[1]}[{client.get_chat_member(message.chat.id, mesaj1[1])["user"]["id"]}] isimli kullanıcı {mesaj1[2]} süreyle sessize alındı.""")
                            else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                        else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[1])["until_date"])}__** süresine kadar sessizde""")
                    else:message.reply("Birini sessize almak için yönetici olmanız lazım.")
                elif "@" in mesaj1[2]:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj1[2])
                        except:message.reply(f"Bu grupta {mesaj1[2]} isimli bir kullanıcı bulunamadı.");quit()
                        if client.get_chat_member(message.chat.id, mesaj1[2])["until_date"] == None:
                            if client.get_chat_member(message.chat.id, mesaj1[2])["status"] not in yetkiler:
                                if zaman(mesaj1[1]) == False:
                                    message.reply("""Lütfen komutu "**__/mute @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")
                                else:    
                                    client.restrict_chat_member(message.chat.id, mesaj1[2], ChatPermissions(), int(time.time() + zaman(mesaj1[1])))
                                    message.reply(f"""{mesaj1[2]}[{client.get_chat_member(message.chat.id, mesaj1[2])["user"]["id"]}] isimli kullanıcı {mesaj1[1]} süreyle sessize alındı.""")                    
                        else:message.reply(f"""Sessize almak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[2])["until_date"])}__** süresine kadar sessizde.""")
            else:message.reply("""Lütfen komutu "**__/mute @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")

        else:
            mesaj2 = mesaj.split()
            if len(mesaj2) == 1:
                message.reply("Lütfen /mute komutunu sessize alacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")

            elif len(mesaj2) == 2:
                if len(mesaj2[1]) == 9:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[1])
                        except:message.reply(f"Bu grupta {mesaj2[1]} isimli bir kullanıcı bulunamadı.");quit()
                        if client.get_chat_member(message.chat.id, mesaj2[1])["until_date"] == None:
                            if client.get_chat_member(message.chat.id, mesaj2[1])["status"] not in yetkiler:
                                client.restrict_chat_member(message.chat.id, mesaj2[1], ChatPermissions())
                                if client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]:
                                    message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı sessize alındı.""")
                                else:
                                    message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["first_name"]}](tg://user?id={mesaj2[1]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı sessize alındı.""")
                            else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                        else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[1])["until_date"])}__** süresine kadar sessizde""")
                    else:message.reply("Birini sessize almak için yönetici olmanız lazım.")
                else:message.reply("Lütfen /mute komutunu sessize almak kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")
                

            elif len(mesaj2) == 3:
                if zaman(mesaj2[1]) == False and len(mesaj2[1]) == 9 and zaman(mesaj2[2]) != False:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[1])
                        except:message.reply(f"Bu grupta {mesaj2[1]} isimli bir kullanıcı bulunamadı.");quit()
                        if client.get_chat_member(message.chat.id, mesaj2[1])["until_date"] == None:
                            if client.get_chat_member(message.chat.id, mesaj2[1])["status"] not in yetkiler:
                                client.restrict_chat_member(message.chat.id, mesaj2[1], ChatPermissions(), int(time.time() + zaman(mesaj2[2])))
                                if client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]:
                                    message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı {mesaj2[2]} süreyle sessize alındı.""")
                                else:
                                    message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["first_name"]}](tg://user?id={mesaj2[1]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı sessize alındı.""")
                            else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                        else:message.reply(f"""Sessize almak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[1])["until_date"])}__** süresine kadar sessizde.""")
                    else:message.reply("Birini Sessize almak için yönetici olmanız lazım.")

                elif zaman(mesaj2[2]) == False and len(mesaj2[2]) == 9 and zaman(mesaj2[1]) != False:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[2])
                        except:message.reply(f"Bu grupta {mesaj2[2]} isimli bir kullanıcı bulunamadı.");quit()
                        if client.get_chat_member(message.chat.id, mesaj2[2])["until_date"] == None:
                            if client.get_chat_member(message.chat.id, mesaj2[2])["status"] not in yetkiler:
                                client.restrict_chat_member(message.chat.id, mesaj2[2], ChatPermissions(), int(time.time() + zaman(mesaj2[1])))
                                if client.get_chat_member(message.chat.id, mesaj2[2])["user"]["username"]:
                                    message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["username"]}[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["id"]}] isimli kullanıcı {mesaj2[2]} sessize alındı.""")
                                else:
                                    message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["first_name"]}](tg://user?id={mesaj2[2]}[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["id"]}] isimli kullanıcı sessize alındı.""")
                            else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                        else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[2])["until_date"])}__** süresine kadar sessizde.""")
                    else:message.reply("Birini Sessize almak için yönetici olmanız lazım.")

                else:
                    message.reply("Lütfen /mute komutunu sessize alacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")

    else:message.reply("Burası bir özel sohbet. Özel sohbette seni sessize alamam.")
