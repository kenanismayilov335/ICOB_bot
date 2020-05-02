from pyrogram import Client, Filters
from datetime import datetime


def kullanici_fonk(grup, kullanici, message, client):
        try:
            kullanici_bilgi = client.get_chat_member(grup, kullanici)
        except:
            message.reply(f"""Maalesef, böyle bir kullanıcı bulunamadı.""")
            quit()

        try:kisitlama = datetime.utcfromtimestamp(kullanici_bilgi["until_date"])
        except TypeError: kisitlama = "None"

        try:lakab = kullanici_bilgi["title"]
        except TypeError:lakab = "None"

        try:katilma_zamani = datetime.utcfromtimestamp(kullanici_bilgi["joined_date"])
        except TypeError:katilma_zamani = f"Kullanıcı Grup Kurucusu"

        try:davet = f"""@{kullanici_bilgi["invited_by"]["username"]}"""
        except TypeError: davet = "None"

        try:yonetici_yapan_kullanici = f"""@{kullanici_bilgi["promoted_by"]["username"]}"""
        except TypeError: yonetici_yapan_kullanici = "None"

        try:kisitla_at_kullanici = f"""@{kullanici_bilgi["restricted_by"]["username"]}"""
        except TypeError:kisitla_at_kullanici = "None"
        
        bot_mu = kullanici_bilgi["user"]["is_bot"]
        if bot_mu:
            bot_mu = "Evet"
        elif bot_mu == False:
            bot_mu = "Hayır"

        son_gorulme = kullanici_bilgi["user"]["status"]
        if son_gorulme == "online" : son_gorulme = "Çevrimiçi"
        elif son_gorulme == "offline" :
            son_gorulme = f"""Çevrimdışı**\nSon Çevrimiçi : **{kullanici_bilgi["user"]["last_online_date"]}"""
        elif son_gorulme == "recently" : son_gorulme = "Son Zamanlarda/Gizli"
        elif son_gorulme == "Within_week" : son_gorulme = "Hafta içinde"
        elif son_gorulme == "Within_month" : son_gorulme = "Ay içinde"
        elif son_gorulme == "Long_time_ago" : son_gorulme = "Uzun Zamandır"
        elif son_gorulme == None : son_gorulme = "Kullanıcı BOT"
        
        #online = Çevrimiçi
        #offline = Çevrimdışı
        #recently = Son zamanlarda
        #Within_week = Hafta içinde
        #Within_month = Ay içinde
        #Long_time_ago = Uzun zamandır
        #None = Kullanıcı BOT

        dil = kullanici_bilgi["user"]["language_code"]
        if dil:
            pass
        elif dil == None:
            dil = "Kullanıcı BOT"

        numara = kullanici_bilgi["user"]["phone_number"]
        if numara:
            pass
        elif numara == None:
            numara = "Gizli/BOT"

        mesaj = f"""👤 @{kullanici_bilgi["user"]["username"]} isimli kullanıcının ; \n"""
        mesaj += f"""
👉 ID : {kullanici_bilgi["user"]["id"]}
👉 Adı : {kullanici_bilgi["user"]["first_name"]}
👉 Soyadı : {kullanici_bilgi["user"]["last_name"]}
👉 Grub Yetkisi : **{kullanici_bilgi["status"]}**
👉 Kısıtlama : **{kisitlama}**
👉 Grub Lakabı : **{lakab}**
👉 Katılma Zamanı : **{katilma_zamani}**
👉 Davet Eden Kullanıcı : **{davet}**
👉 Yönetici Yapan Kullanıcı : **{yonetici_yapan_kullanici}**
👉 Kısıtlayan veya Atan Kullanıcı : **{kisitla_at_kullanici}**
👉 Kullanıcı Bot mu : **{bot_mu}**
👉 Son Görülme : **{son_gorulme}**
👉 Kullanıcının dili : **{dil}**
👉 Telefon Numarası : **{numara}**
"""
        message.reply(mesaj)

@Client.on_message(Filters.command(["kullanici"], ["/", "."]))
def kullanici(client, message):
    bilgi = message.text.split()

    if message.chat.type == "private":
        if len(bilgi) <= 2 or len(bilgi) > 3:
            message.reply("""Lütfen komutu **__"/kullanici  sohbet_id/isim  kullanıcı_id/isim"__** şeklinde giriniz. """)

        else:
            kullanici_fonk(bilgi[1], bilgi[2], message, client)
    #elif message.chat.type == ["group", "supergroup", "channel"]: 

    elif message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "channel":
        if len(bilgi) == 3:
            kullanici_fonk(bilgi[1], bilgi[2], message, client)

        elif len(bilgi) == 2:
            kullanici_fonk(message.chat.id, bilgi[1], message, client)

        else:
            message.reply("""Lütfen komutu **__"/kullanici  sohbet_id/isim  kullanıcı_id/isim"__** şeklinde giriniz. """)

