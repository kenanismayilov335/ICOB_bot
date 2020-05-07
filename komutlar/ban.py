from pyrogram import Client, Filters
import time
from datetime import datetime


def zaman(metin):
    if "gün" in metin:
        metin = metin.replace("gün", "")
        try:return int(int(metin) * 24 * 60 * 60)
        except:return "hata"
    elif "saat" in metin:
        metin = metin.replace("saat", "")
        try:return int(int(metin) * 60 * 60)
        except:return "hata"

    elif "dk" in metin:
        metin = metin.replace("dk", "")
        try:return int(int(metin) * 60)
        except:return "hata"
    else:return "hata"

@Client.on_message(Filters.command(["ban"]))
def ban(client, message):
    mesaj = message.text
    yetkiler = ("creator", "administrator")
    if message.chat.type != "private":
        if message.reply_to_message:
            sure = message.text.split()
            if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                try:client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                except:message.reply("Maalesef yanıtladığınız mesajı atan kullanıcı grubtan çıkmış.");quit()
      #gereksiz#if client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["until_date"] == None:
                if client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["status"] not in yetkiler:
                    if len(sure) == 1:
                        client.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, 0)
                        if message.reply_to_message.from_user.username:
                            message.reply(f"@{message.reply_to_message.from_user.username}[{message.reply_to_message.from_user.id}] banlandı.")
                        else:
                            message.reply(f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})[{message.reply_to_message.from_user.id}] banlandı")
                    elif len(sure) > 2:
                        message.reply("""Lütfen komutu "**__/ban 5dk/1gün/10saat__**" şeklinde giriniz. """) 
                    else:
                        if zaman(sure[1]) == "hata":
                            message.reply("""Lütfen komutu "**__/ban 5dk/1gün/10saat__**" şeklinde giriniz. """) 
                        else:
                            client.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, int(time.time() + zaman(sure[1])))
                            if message.reply_to_message.from_user.username:
                                message.reply(f"@{message.reply_to_message.from_user.username}[{message.reply_to_message.from_user.id}] {sure[1]} süreyle banlandı.")
                            else:
                                message.reply(f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})[{message.reply_to_message.from_user.id}] {zaman(sure[1])} süreyle banlandı")
                else:message.reply("Banlamak istediğiniz kişi yönetici.")
      #gereksiz#else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["until_date"])}__** süresine kadar banı var.""")
            else:message.reply("Birisini banlamak için yönetici olman gerekir.")
        elif "@" in mesaj:    
            mesaj1 = mesaj.split()
            if len(mesaj1) == 2:    
                if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                    try:client.get_chat_member(message.chat.id, mesaj1[1])
                    except:message.reply(f"Bu grupta {mesaj1[1]} isimli bir kullanıcı bulunamadı.");quit()
                    #if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"] == None:
                    if client.get_chat_member(message.chat.id, mesaj1[1])["status"] not in yetkiler:
                        client.kick_chat_member(message.chat.id, mesaj1[1])
                        message.reply(f"{mesaj1[1]} banlandı.")
                    else:message.reply("Banlamak istediğiniz kişi bir yönetici.")
                    #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[1])["until_date"])}__** süresine kadar banı var.""")
                else:message.reply("Birini banlayabilmek için yönetici olmanız lazım.")

            elif len(mesaj1) == 3:
                if "@" in mesaj1[1]:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj1[1])
                        except:message.reply(f"Bu grupta {mesaj1[1]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj1[1])["status"] not in yetkiler:
                            if zaman(mesaj1[2]) == "hata":
                                message.reply("""Lütfen komutu "**__/ban @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")
                            else:
                                client.kick_chat_member(message.chat.id, mesaj1[1], int(time.time() + zaman(mesaj1[2])))
                                message.reply(f"""{mesaj1[1]}[{client.get_chat_member(message.chat.id, mesaj1[1])["user"]["id"]}] isimli kullanıcı {mesaj1[2]} süreyle banlandı.""")
                        else:message.reply("Banlamak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[1])["until_date"])}__** süresine kadar banı var.""")
                    else:message.reply("Birini banlayabilmek için yönetici olmanız lazım.")
                elif "@" in mesaj1[2]:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj1[2])
                        except:message.reply(f"Bu grupta {mesaj1[2]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj1[2])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj1[2])["status"] not in yetkiler:
                            if zaman(mesaj1[1]) == "hata":
                                message.reply("""Lütfen komutu "**__/ban @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")
                            else:    
                                client.kick_chat_member(message.chat.id, mesaj1[2], int(time.time() + zaman(mesaj1[1])))
                                message.reply(f"""{mesaj1[2]}[{client.get_chat_member(message.chat.id, mesaj1[1])["user"]["id"]}] isimli kullanıcı {mesaj1[1]} süreyle banlandı.""")                    
                        #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[2])["until_date"])}__** süresine kadar banı var.""")
            else:message.reply("""Lütfen komutu "**__/ban @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")

        else:
            mesaj2 = mesaj.split()
            if len(mesaj2) == 1:
                message.reply("Lütfen /ban komutunu banlayacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")

            elif len(mesaj2) == 2:
                if len(mesaj2[1]) == 9:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[1])
                        except:message.reply(f"Bu grupta {mesaj2[1]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj2[1])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj2[1])["status"] not in yetkiler:
                            client.kick_chat_member(message.chat.id, mesaj2[1])
                            if client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]:
                                message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı banlandı.""")
                            else:
                                message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["first_name"]}](tg://user?id={mesaj2[1]})[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı banlandı.""")
                        else:message.reply("Banlamak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[1])["until_date"])}__** süresine kadar banı var.""")
                    else:message.reply("Birini banlayabilmek için yönetici olmanız lazım.")
                else:message.reply("Lütfen /ban komutunu banlayacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")
                

            elif len(mesaj2) == 3:
                if zaman(mesaj2[1]) == "hata" and len(mesaj2[1]) == 9 and zaman(mesaj2[2]) != "hata":
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[1])
                        except:message.reply(f"Bu grupta {mesaj2[1]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj2[1])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj2[1])["status"] not in yetkiler:
                            client.kick_chat_member(message.chat.id, mesaj2[1], int(time.time() + zaman(mesaj2[2])))
                            if client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]:
                                message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı {mesaj2[2]} süreyle banlandı.""")
                            else:
                                message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["first_name"]}](tg://user?id={mesaj2[1]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı banlandı.""")
                        else:message.reply("Banlamak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[1])["until_date"])}__** süresine kadar banı var.""")
                    else:message.reply("Birini banlayabilmek için yönetici olmanız lazım.")

                elif zaman(mesaj2[2]) == "hata" and len(mesaj2[2]) == 9 and zaman(mesaj2[1]) != "hata":
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[2])
                        except:message.reply(f"Bu grupta {mesaj2[2]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj2[2])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj2[2])["status"] not in yetkiler:
                            client.kick_chat_member(message.chat.id, mesaj2[2], int(time.time() + zaman(mesaj2[1])))
                            if client.get_chat_member(message.chat.id, mesaj2[2])["user"]["username"]:
                                message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["username"]}[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["id"]}] isimli kullanıcı {mesaj2[2]} banlandı.""")
                            else:
                                message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["first_name"]}](tg://user?id={mesaj2[2]}[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["id"]}] isimli kullanıcı banlandı.""")
                        else:message.reply("Banlamak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[2])["until_date"])}__** süresine kadar banı var.""")
                    else:message.reply("Birini banlayabilmek için yönetici olmanız lazım.")

                else:
                    message.reply("Lütfen /ban komutunu banlayacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")

    else:message.reply("Burası bir özel sohbet. Özel sohbette seni banlayamam.")
