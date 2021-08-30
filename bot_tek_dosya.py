# Bu bot @izcipy tarafından I-COB için yazılmıştır. İstediğiniz gibi kullanabilirsiniz.
# Tek dosya halinde sıkıntı çıkabilir. Çıkarsa ICOB_BOT.py'i çalıştırınız.

from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions
from googletrans import Translator
import requests 
from bs4 import BeautifulSoup
from google_search_client.search_client import GoogleSearchClient
import ast
import datetime
import pytz
from pytube import YouTube
import time


ICOB_BOT = Client(
    api_id="7319490",          #https://my.telegram.org/apps den alabilirsiniz
    api_hash ="3987ed5fcb72635ca4da8c5e93ec7493",       #https://my.telegram.org/apps den alabilirsiniz
    session_name = "kenw",  #Burayı sallayabilirsiniz :D               
    bot_token = "1996020741:AAEHuYNcHjmlURScRqlvLKLtihWhOqW0-ps",     #botfather dan alabilirsiniz.
    plugins=dict(root="komutlar")
)


@ICOB_BOT.on_message(Filters.command(["start"], ["/", "."]))
def basla_mesaj(client, message):
    message.reply("Hoş geldin! \n/yardim komutuyla neler yapabildiğimi görebilirsin.")

#############################

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
🤖 /sahur
🤖 /cevir
🤖 /ban
🤖 /unban
🤖 /mute
🤖 /unmute
🤖 /notlar
🤖 /not
"""

    merhaba.edit(mesaj)

#############################

@ICOB_BOT.on_message(Filters.command(["ping"]))
def ping(client, message):
  message.reply("Ben çalışıyorum merak etme")

#############################

@ICOB_BOT.on_message(Filters.new_chat_members)
def hosgeldin(client, message):
    butonlar = [[InlineKeyboardButton("🎉 Grubumuza Katılın", url="https://t.me/icobteam"),
                 InlineKeyboardButton("📝 Kodlarım", url="https://github.com/izci-py/ICOB_bot")],
                 [InlineKeyboardButton("📰 Instagram", url="https://www.instagram.com/i.cobvision/?hl=tr")]
                 ]
                
    kullanici = [f"[{i.first_name}](tg://user?id={i.id})" for i in message.new_chat_members]
    mesaj = f"""Merhaba {"".join(kullanici)}, **{message.chat.title}** grubuna hoşgeldin. Seni aramızda görmekten çok mutlu olduk. 😊"""
    message.reply(mesaj, reply_markup=InlineKeyboardMarkup(butonlar))
    
#############################

@ICOB_BOT.on_message(Filters.command(["admin"]))
def admin(client, message):
    baskan = ""
    admin = ""
    bekle = message.reply("Adminler bulunuyor...")
    for uye in client.iter_chat_members(message.chat.id):
        if uye.user.is_bot == False:
            if uye.status == "creator":
                if uye.user.username:baskan += f"👮‍♂️  @{uye.user.username}\n"
                else:baskan += f"👮‍♂️  [{uye.user.first_name}](tg://user?id={uye.user.id})\n"
            if uye.status == "administrator":
                if uye.user.username:admin += f"👮‍♂️  @{uye.user.username}\n"
                else:admin += f"👮‍♂️  [{uye.user.first_name}](tg://user?id={uye.user.id})\n"
            else:pass
        else:pass
    bekle.edit(f"**__Yöneticilerimiz__** ;\n{baskan}{admin}")

#############################

@ICOB_BOT.on_message(Filters.command(["bildir"]))
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

#############################

LANGUAGES = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 
'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 
'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 
'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 
'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 
'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}

@ICOB_BOT.on_message(Filters.command(["cevir"]))
def cevir(client, message):
    metin = message.text

    dil = metin.split()[1]

    cev = Translator()

    if dil in LANGUAGES:    
        cevir_metin = cev.translate(" ".join(metin.split()[2:]), dest=dil)
        message.reply(f"""👉Metin Dili : **__{cevir_metin.src}__**\n👉Çevirilen Dil : **__{cevir_metin.dest}__**\n\n👉Metin : **__{cevir_metin.text}__**""")

    else:   
        cevir_metin = cev.translate(" ".join(metin.split()[1:]), dest="en")
        message.reply(f"""👉Metin Dili : **__{cevir_metin.src}__**\n👉Çevirilen Dil : **__{cevir_metin.dest}__**\n\n👉Metin : **__{cevir_metin.text}__**""")
        
#############################

@ICOB_BOT.on_message(Filters.command(["doviz"], ["/", "."]))
def doviz(client, message):
    bekle = message.reply("Bekleyin...")

    r = requests.get("https://altin.in/fiyat/gram-altin")

    soup = BeautifulSoup(r.content, "html.parser")

    dolar = soup.find("h2", attrs={"id":"dfiy"})

    euro = soup.find("h2", attrs={"id":"efiy"})

    sterlin = soup.find("h2", attrs={"id":"sfiy"})

    #altin_alis = soup.find("li", attrs={"title":"Gram Altın - Alış"})

    altin_satis = soup.find("li", attrs={"title":"Gram Altın - Satış"})

    bilgi = f"💰Dolar: **{dolar.text}**\n💰Euro: **{euro.text}**\n💰Sterlin: **{sterlin.text}**\n💰Altın: **{altin_satis.text}**"

    bekle.edit(bilgi)

#############################

@ICOB_BOT.on_message(Filters.command(['google'], ['.', '/']))
def google_search(client, message):
    bekle = message.reply("Araştırılıyor...")
    text = message.text
    if len(text.split()) == 1:
        message.edit("Lütfen araştırmak istediğiniz kelimeyi giriniz")
        return
    else:
        query = " ".join(text.split()[1:])
        msg = "Araştırılan Kelime : {}\n\n".format(query)
        res = GoogleSearchClient()
        results = res.search(query).to_json()
        if results:
            i = 1
            for result in ast.literal_eval(results):
                msg += f"🔍 [{result['title']}]({result['url']})\n\n"
                i += 1
                if i == 10:
                    break

            try:
                bekle.edit(msg, disable_web_page_preview=True, parse_mode="Markdown")
            except Exception as e:
                print(e)

#############################

@ICOB_BOT.on_message(Filters.command(["iftar", "iftar@icob_bot"]))
def iftar(client, message):
    sozluk = {
        'Artvin': 1, 'Aydın': 2, 'Balıkesir': 3, 'Bartın': 4, 'Batman': 5, 'Bayburt': 6,
        'Bilecik': 7, 'Bingöl': 8,'Bitlis': 9, 'Bolu': 10, 'Burdur': 11, 'Bursa': 12,
        'Çanakkale': 13, 'Çankırı': 14, 'Çorum': 15, 'Denizli': 16, 'Diyarbakır': 17,
        'Düzce': 18, 'Edirne': 19, 'Elazığ': 20, 'Erzincan': 21, 'Erzurum': 22, 'Eskişehir': 23,
        'Gaziantep': 24, 'Giresun': 25, 'Gümüşhane': 26, 'Hakkari': 27, 'Hatay': 28, 'Iğdır': 29,
        'Isparta': 30, 'İstanbul': 31, 'Istanbul': 31, 'İzmir': 32, 'Kocaeli': 33, 'Kahramanmaraş': 34, 
        'Karabük': 35, 'Karaman': 36, 'Kars': 37, 'Kastamonu': 38, 'Kayseri': 39, 'Kırıkkale': 40, 
        'Kırklareli': 41, 'Kırşehir': 42, 'Kilis': 43, 'Konya': 44, 'Kütahya': 45, 'Malatya': 46, 
        'Manisa': 47, 'Mardin': 48, 'Mersin': 49, 'Muğla': 50, 'Muş': 51, 'Nevşehir': 52, 'Niğde': 53, 
        'Ordu': 54, 'Osmaniye': 55, 'Rize': 56, 'Samsun': 57, 'Siirt': 58, 'Sinop': 59, 'Sivas': 60,
        'Şanlıurfa': 61, 'Şırnak': 62, 'Tekirdağ': 63, 'Tokat': 64, 'Trabzon': 65, 'Tunceli': 66, 
        'Uşak': 67, 'Van': 68, 'Yalova': 69, 'Yozgat': 70, 'Zonguldak': 71, 'Adana': 72, 'Sakarya': 73, 
        'Adıyaman': 74, 'Afyon': 75, 'Ağrı': 76,'Aksaray': 77, 'Amasya': 78, 'Ankara': 79, 'Antalya': 80, 'Ardahan': 81
    }

    
    if len(message.text.split()) == 1:
        message.reply("""Lütfen komutu "**__/iftar il_ismi__**" şeklinde giriniz.""")
        quit()
    
    elif len(message.text.split()) == 2:
        if message.text.split()[1].title() in sozluk:
            r = requests.get(f"https://www.fazilettakvimi.com/api/imsakiye/index/{sozluk[message.text.split()[1].title()]}")
            sayfa = r.json()

            ramazan_gun = sayfa["ramazanin_kaci"]

            aksam = sayfa["vakitler"][ramazan_gun - 1]["aksam"]
            saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")

            aksam_dk = int(aksam.split(":")[0]) * 60 + int(aksam.split(":")[1])
            saat_dk = int(saat.split(":")[0]) * 60 + int(saat.split(":")[1])

            iftar = aksam_dk - saat_dk
            iftar = f"{iftar // 60}:{iftar % 60}"

            if "-" in str(iftar):
                iftar = f"""Bugünkü iftar vakti **__{str(iftar).split(":")[0].replace("-", "")}__** saat **__{str(iftar).split(":")[1]}__** dakika geçti.\n**__Hayırlı İftarlar Dileriz.😊__**.\n\nSonraki iftar vaktine **__{24 + int(str(iftar).split(":")[0])}__** saat **__{60 - int(str(iftar).split(":")[1])}__** dakika var."""
                
            else:
                iftar = f"""Sonraki iftar vaktine **__{str(iftar).split(":")[0]}__** saat **__{str(iftar).split(":")[1]}__** dakika kaldı. 😊"""
            
            mesaj = f"**__{message.text.split()[1].title()}__** şehrinde ;\n"
            mesaj += iftar
            message.reply(mesaj)

        else:message.reply("Böyle bir il yok")
    else:message.reply("""Lütfen komutu "**__/iftar il_ismi__**" şeklinde giriniz.""")

#############################

@ICOB_BOT.on_message(Filters.command(["sahur", "sahur@icob_bot"]))
def sahur(client, message):
    sozluk = {
        'Artvin': 1, 'Aydın': 2, 'Balıkesir': 3, 'Bartın': 4, 'Batman': 5, 'Bayburt': 6,
        'Bilecik': 7, 'Bingöl': 8,'Bitlis': 9, 'Bolu': 10, 'Burdur': 11, 'Bursa': 12,
        'Çanakkale': 13, 'Çankırı': 14, 'Çorum': 15, 'Denizli': 16, 'Diyarbakır': 17,
        'Düzce': 18, 'Edirne': 19, 'Elazığ': 20, 'Erzincan': 21, 'Erzurum': 22, 'Eskişehir': 23,
        'Gaziantep': 24, 'Giresun': 25, 'Gümüşhane': 26, 'Hakkari': 27, 'Hatay': 28, 'Iğdır': 29,
        'Isparta': 30, 'İstanbul': 31, 'Istanbul': 31, 'İzmir': 32, 'Kocaeli': 33, 'Kahramanmaraş': 34, 
        'Karabük': 35, 'Karaman': 36, 'Kars': 37, 'Kastamonu': 38, 'Kayseri': 39, 'Kırıkkale': 40, 
        'Kırklareli': 41, 'Kırşehir': 42, 'Kilis': 43, 'Konya': 44, 'Kütahya': 45, 'Malatya': 46, 
        'Manisa': 47, 'Mardin': 48, 'Mersin': 49, 'Muğla': 50, 'Muş': 51, 'Nevşehir': 52, 'Niğde': 53, 
        'Ordu': 54, 'Osmaniye': 55, 'Rize': 56, 'Samsun': 57, 'Siirt': 58, 'Sinop': 59, 'Sivas': 60,
        'Şanlıurfa': 61, 'Şırnak': 62, 'Tekirdağ': 63, 'Tokat': 64, 'Trabzon': 65, 'Tunceli': 66, 
        'Uşak': 67, 'Van': 68, 'Yalova': 69, 'Yozgat': 70, 'Zonguldak': 71, 'Adana': 72, 'Sakarya': 73, 
        'Adıyaman': 74, 'Afyon': 75, 'Ağrı': 76,'Aksaray': 77, 'Amasya': 78, 'Ankara': 79, 'Antalya': 80, 'Ardahan': 81
    }

    
    if len(message.text.split()) == 1:
        message.reply("""Lütfen komutu "**__/sahur il_ismi__**" şeklinde giriniz. """)
        quit()
    
    elif len(message.text.split()) == 2:
        if message.text.split()[1].title() in sozluk:
            r = requests.get(f"https://www.fazilettakvimi.com/api/imsakiye/index/{sozluk[message.text.split()[1].title()]}")
            sayfa = r.json()

            ramazan_gun = sayfa["ramazanin_kaci"]

            sabah = sayfa["vakitler"][ramazan_gun - 1]["sabah"]
            saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")

            sabah_dk = int(sabah.split(":")[0]) * 60 + int(sabah.split(":")[1])
            saat_dk = int(saat.split(":")[0]) * 60 + int(saat.split(":")[1])

            sahur = sabah_dk - saat_dk
            sahur = f"{sahur // 60}:{sahur % 60}"

            if "-" in str(sahur):
                sahur = f"""Bugünkü sahur vakti **__{str(sahur).split(":")[0].replace("-", "")}__** saat **__{str(sahur).split(":")[1]}__** dakika geçti.\n**__Hayırlı Sahurlar Dileriz.😊__**.\n\nSonraki sahur vaktine **__{24 + int(str(sahur).split(":")[0])}__** saat **__{60 - int(str(sahur).split(":")[1])}__** dakika var."""
            
            else:
                sahur = f"""Sonraki sahur vaktine **__{str(sahur).split(":")[0]}__** saat **__{str(sahur).split(":")[1]}__** dakika kaldı. 😊"""
            
            mesaj = f"**__{message.text.split()[1].title()}__** şehrinde ;\n"
            mesaj += sahur
            message.reply(mesaj)

        else:message.reply("Böyle bir il yok")
    else:message.reply("""Lütfen komutu "**__/sahur il_ismi__**" şeklinde giriniz.""")

#############################

@ICOB_BOT.on_message(Filters.command(["imdb"], ["/", "."]))
def imdb(client, message):
    bekle = message.reply("Bekleyin...")
    imdb_sonuc = "IMDB en iyi filmler: \n"
    r = requests.get("https://www.alem.com.tr/sinema/imdb-puani-yuksek-filmler-930211")

    soup = BeautifulSoup(r.content, "html.parser")

    a = soup.find_all("p")

    for i in a[2:60]:
        if bool(i) == False:
            pass
        else:
            imdb_sonuc += f"{i.text}\n"

    bekle.edit(imdb_sonuc)

#############################

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

@ICOB_BOT.on_message(Filters.command(["kullanici"], ["/", "."]))
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

#############################

@ICOB_BOT.on_message(Filters.command(["tdk"], ["/", "."], case_sensitive=True))
def tdk(client, message):
    bekle = message.reply("Kelime aranıyor...")
    kelime = message.text.split()
    kelime_duzen = " ".join(kelime[1:])
    if len(kelime) <= 1:
        bekle.edit("Lütfen bir kelime giriniz")
    else:
        r = requests.get(f"http://sozluk.gov.tr/gts?ara={kelime_duzen}")

        kelime_anlamlari = r.json()

        if "error" in kelime_anlamlari:
            bekle.edit("Kelime https://sozluk.gov.tr/ sitesinde bulunamadı")
        else:
            mesaj = f"📚 **{kelime_duzen}** Kelimesinin Anlamları:\n\n"
            a = kelime_anlamlari[0]["anlamlarListe"]
            for i in a:
                mesaj += f"👉 {i['anlam']} \n"

            bekle.edit(mesaj)
            
#############################
#YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()

@ICOB_BOT.on_message(Filters.command(["youtube"], ["/", "."]))
def youtube(client, message):
    bekle = message.reply("Bekleyin...")
    link = message.text.split()
    if len(link) == 1:
        bekle.edit("Lütfen bir YouTube Video linki giriniz")

    else:
        link_duzen = " ".join(link[1:])
        video = YouTube(link_duzen).streams.get_highest_resolution().download()
        client.send_video(message.chat.id, video)
        bekle.edit("Videonuz indirildi")

#############################

not_bilgi = {"yongalar":{"foto":"AgADBAADNLQxG3gLqFEHwm48StDieUd8ZiJdAAMBAAMCAAN5AANkQAIAARYE", "yazı":"""Yongalar Yonga kelimesinin ilk kez duyuyorsanız kelimenin Japonca olduğunu düşünebilirsiniz. Ben ilk duyduğumda böyle düşünmüştüm. Şimdi gelin bu kelimenin şu an ve gelecekte bizi ne kadar ilgilendirdiğini konuşalım. Yongalar tasarımı ve kurulumu çok uzun süren cihazlar. Bu cihazlar yapay zeka algoritmalarını daha hızlı ve etkili bir şekilde gerçekleştirmeye yarıyor. Şirketler bu cihazlara dev yatırımlar yapıyor. Bununla birlikte pek çok araştırmacı da yongalar üzerinde ilerleme kaydetmek için çaba sarf ediyor.Makine öğrenme algoritmalarının hızlı gelişimine yeni yonga tasarımlarının ayak uydurduğunu söylemek hayli zor. Çünkü yeni bir yonga tasarlamak yıllar alabiliyor. Bu problemin çözümü için Google ın derin öğrenme ve yapay zeka araştırma grubu olan Google Brain araştırmacılarından Anna Godie ve Azalia Mirhoseini, "yapay zeka kendine ayak uyduracak yongasını kendisi tasarlasın" anlayışıyla bir model geliştirdiler. Bu modelin temel amacı yonga tasarımının o uzun süresini ortadan kaldırmak ve yonga ile donanım arasındaki uyumu daha iyi sağlamak. Uyumun daha iyi sağlanmasına bağlı olarak sistemin de güçleneceğini düşünüyorlar. Tasarım süreci hedefteki gibi kısaltılabilirse yonga ile yapay zeka gelişimi arasında zaman uyumu sağlanabilir. Ekip bu çalışmada yonga tasarımlarında "yerleşim" olarak adlandırılan aşamayı geliştirdikleri yapay zeka sayesinde bir gün gibi kısa bir sürede gerçekleştirmeyi hedefledi. Normalde bu aşama uzman kişiler ve yüksek teknolojilerle bile haftalarca zaman alabiliyor. Peki yongaları bizim hayatımızda bu kadar önemli yapan ve şirketleri üzerinde pek çok araştırma yapmaya itecek kadar önemli kılan ne? Bildiğiniz gibi yapay zeka hayatımızda çok büyük bir yere sahip. Kullandığımız (yeni nesil) ; akıllı telefonlar, sesli asistanlar, buzdolapları, otomobiller gibi cihazlarda yapay zekaya rastlamak artık şaşırılacak bir şey olmaktan çıktı. Ve bu denli önemli olan yapay zekadaki gelişmeler yonga tasarımlarındaki ilerlemeler ile sıkı bir bağlantı içinde. Bundan dolayı yongalar üzerindeki çalışmaların yeni nesil yonga üretimini kolaylaştıracağı ve böylece yapay zeka alanındaki ilerlemeye iyi bir ivme kazandırılacağı düşünülüyor."""},
"neuralink":{"foto":"AgADBAADM7QxG3gLqFEhdBG6vb2JPRPKYyNdAAMBAAMCAAN5AAMkZQACFgQ", "yazı":"""Merhaba arkadaşlar, bugün sizlere çılgın projeleriyle tanıdığımız Elon Musk'ın insan beynine çip yerleştirme projesini anlatacağım. Elon Musk bu projesini bir şirket altında topladı ve ismi Neuralink. Peki nedir bu Neuralink? Neuralink 2016 yılından beri insan beynini bilgisayar arayüzüne bağlayan teknolojiler üzerine çalışan bir şirket. Hatta bu projelerinde oldukça ilerlediler ve bu sene insanlar üzerinde de çalışmayı hedefliyorlar. Peki bu teknoloji nasıl çalışacak? Bu teknoloji beynimize saçımızın 10 da biri kadar ince olan teller bağlayarak beynimizin içindeki elektrotlardan veri alıp bunu bluetooth yardımıyla bilgisayar arayüzüne göndermeyi hedefliyor. Bunun yanında dışarıdan beynimize veri çekmemizi de sağlayacak. Mesela artık dil öğrenmek için günler aylar harcamaya Ayrıca bu teknolojiyi beynimizin yanında bir yapay zekada da kullanabiliyor olacağız. Bir de bu teknoloji sayesinde insandan insana veri aktarımı daha kolay olacak. Şöyle ki kurduğumuz bir hayali yahut aklımızdaki bir düşünceyi karşı tarafa göndererek onun da bu düşünceyi okumasını ya da hayali izlemesini sağlayabileceğiz. Belki bir gün bizler de bu teknolojiyi kullanabiliriz, kullanacağımız zamanlarda da görüşmek üzere."""},
"uzay_çöpleri":{"foto":"AgADBAADNbQxG3gLqFGxv678ETdMBHentBsABAEAAwIAA3kAA098BgABFgQ", "yazı":"""Sputnik 1, 1957 yılında uzaya gönderilen ilk yapay uyduydu, aynı zamanda Dünya'dan gönderilen ilk uzay aracı. O yıldan beri uzaya çok sayıda araç gönderildi.Bu araçlardan bir kısmının enerjisi bitti,bir kısmı bozuldu,yörüngesinden  çıktı ya da başka nedenlerle artık işe yaramaz hâle geldi.Uzayda yanlışlıkla  çarpışanlar ya da yok edilenler oldu! Sonuç olarak pek çok parça uzaya saçıldı.Parçaların bazıları Dünya'nın atmosferine girip yandı.Bazıları ise kütleçekim kuvvetinin etkisiyle Dünya'nın çevresinde dolanmaya başladı. İşte Dünya'nın çevresinde dolaşanlar uzay çöpü olarak kabul ediliyor.Uzay çöpleri, uzay aracı parçalarıyla bunlardan dökülen küçük boya tanecikleri gibi irili ufaklı milyonlarca nesneden oluşuyor. Çoğu uzay çöpü saatte yaklaşık 30 bin kilometre hızla yani çok yüksek bir hızla dolanıyor.Dünya'nın çevresinde bir futbol topundan daha büyük olan 20 bin kadar nesne dolanıyor. Bu noktada uzay çöplerinin bu kadar fazla olmasına neden olan iki önemli olaydan da bahsetmeliyiz.Bunlardan ilki 2007 yılında bir uzay aracının yok edilmesi.Diğeri ise 2009 yılında iki uzay aracının yanlışlıkla çarpışması.İşte bu iki olaydan ortaya çıkan parçalar hâlâ Dünya'nın çevresinde dolanmakta."Peki uzay çöplerinin ne zararı var? Neden bu konuyla ilgileniliyor?"diye düşünebilirsiniz. Şöyle açıklayalım: Büyük boyutlardaki nesneler uzaya gönderilen insanlı ya da insansız araçlara çarpabilir ve onlara ciddi şekilde zarar verebilir.Daha küçük boyutlardaki katı roket yakıtı ya da boya parçası gibi nesnelerse uzay aracının pencerelerine,uyduların güneş panellerine zarar verebilir.Uzay çöplerini azaltmak, yok etmek gibi çalışmalar yapılıyor. Bilim insanları uzaya giden araçlarla büyük çöplerin çarpışmasını engelleyebiliyor.Ancak izlenemeyecek kadar küçük boyuttaki çöplerin uzay araçlarına verebileceği zararları önlemenin şimdilik bir yolu yok."""},
"terleyen_botlar":{"foto":"AgADBAADNrQxG3gLqFHo_bihwCS4CFEyyyJdAAMBAAMCAAN5AANtxgEAARYE", "yazı":"""Robotların "terleyerek" Kendini Soğutması: Bir çoğunuzun da bildigi üzere bilgisayarlarda ve arabalarda soğutucular var ve eğer soğutucular çalışmazsa cihaz arızalanır veya hata verir. Robotikte de soğutucu olarak fan kullanılmakta. Ancak yeni bir teknoloji ile bu fanların yerini "hidrojeller" alabilir. Yeni teknik, makinelerin hareketlerinden ve mekanizmanın ya da sistemin kontrolünden sorumlu aktüatör (tahrik düzeneği) isimli bileşenlerde depolanan soğutma sıvısını "terleyerek" atmasını sağlıyor. Aktüatörler, parmağa benzeyen ve hidrojelden imal edilen akışkan bir yapıya sahip. Üzerinde yüksek miktarda su tutabilen hidrojeller ısı deposu görevi görüyor. Parmaklar iki bölümden oluşuyor; alt tabaka ve üst tabaka. Alt tabakada su akışı için iç kanallar, üst kanalda mikro gözenekler bulunmakta. Bu mikro gözenekler 30°C altında kapalı oluyor. Sıcaklık yükseldiğindeyse üst katman genleşerek gözenekleri açıyor ve böylece alt tabakadaki basınçlı sıvının bu gözeneklerden dışarıya terlemesini sağlıyor. Yapılan bir testte bu terleyen aktüatörler normal fandan üflenen hava ile soğutmaya göre 6 kat daha hızlı soğutuyor. Buraya kadar her şey güzel gibi gözüküyor ama bir sorun var. Araştırmacılara göre terleme verimliliği robotların hareket kabiliyetini geçici bir süre sınırlandırabilir ve hâlâ uzun işlemler sırasında kaybolan suyu yerine koymak için bir yol bulunması gerekiyor. (Aktüatörlerin yanına küçük küçük depolar koyulabileceğini düşündüm ama araştırmacılar benden önce düşünmüştür bile 😄)Her geçen gün gelişen teknoloji ile bu robotlar bizlere benzemeye başladı.🤔 Siz bu konu hakkında ne düşünüyorsunuz?"""},
"güvenli_internet_kullanımı":{"foto":"AgADBAADN7QxG3gLqFGNwAg6UW7RUgoCaCJdAAMBAAMCAAN5AAOCMwIAARYE", "yazı":"""Bundan birkaç sene önce teknolojinin hayatımızda bu kadar önemli bir yer tutacağını tahmin etmek oldukça güçtü. Fakat günümüzde bu durumu hemen hemen her alanda fark etmiş ve fark etmekle kalmayıp kanıksamış bulunmaktayız. Belge ve veri transferi, Sosyal medya, internet bankacılığı, makine öğrenmesi, endüstri 4.0, son günlerde öğrencilerin eğitimi için kullanılan uzaktan eğitim sistemleri ve daha niceleri… Tüm bu sitemler ve programlar internet ve teknolojinin gelişmesi ile hayatımızda yer edinmeye başladılar. Bu durum beraberinde avantajlar ve dezavantajlar getirdi. Peki ya kimlik bilgilerimizin gizliliğinden sorumlu olan sosyal medya şirketlerine ne kadar güvenmeliyiz? Mesela 2018 yılında Facebook kural ihlalinden dolayı cezaya çarptırıldı. Bir başka örnek ise; geçtiğimiz senelerde hackerlar iCloudu hackleyip ünlülerin fotoğraflarını çalmıştı bunun sonucunda Apple’a karşı güvensizlik doğdu. Peki hackerlar bu verilerle ne yapıyor? İlk olarak akıllara şantaj gelse de birçok şey için kullanılabilir. Bakın, internet korsanlarının bazı kötü amaçlar için başvuracağı ilk şey diğer insanların internette var olan özel bilgileridir. Bunlar kişiye özel herhangi bir fotoğraf ya da yazılı bilgi olabilir. Biz bu tip bilgilerin bütününe big data diyoruz. “Peki Big data nedir?” Ne işe yarar?” Sorularına verilecek en iyi cevap: İnternetin hayatımıza girmesiyle, paylaşılan, yazılıp çizilen; görseller, metinler, fotoğraflar, video ve ses kayıtları gibi aklımıza gelebilecek her türlü veri bütününe verilen addır. Örneğin; Domuz gribi salgınının olduğu yıl Google big datayı kullanarak salgının matematiksel modelini çıkarıp salgının yayılma evresi hakkında önemli bulgular elde ederek bu bulguların salgının yayılmasını önlemekte kullanılmasına vesile oldu. Ancak Big data sürekli olarak olumlu yönde kullanılmayabiliyor. Big data, internet korsanlarının uğrak noktası haline gelmiş bulunmakta. Hackerların; bir kişi, kurum, kuruluş hakkında detaylı bilgi edindikleri yer olan big data, elde edilen bu bilgileri kötü amaçları için kullanmalarında vesile olur. Sonuç olarak internetin faydaları saymakla bitmez fakat şu devirde babanıza bile güvenmeyeceksiniz 😀."""},
"çarpışan_gökadalar":{"foto":"AgADBAADOLQxG3gLqFFsdIIBtwuPzG9QZSNdAAMBAAMCAAN5AAPKYwACFgQ", "yazı":"""Çarpışan Anten Gökadalar Bugün sizlerle NGC 4039 ve NGC 4038 adlı iki gökadanın ( galaksinin ) birleşmesini inceleyeceğiz . Bizden 45 - 60 ışık yılı uzaklığında olan bu iki galaksi tahminen 1 milyar yıl önce fazlaca yaklaşarak birleşmeye başladı ve zamanla da iç içe girdiler . Bu olay sonucu galaksilerin bünyelerindeki gazlar ve yıldızlar saçılmaya başladı ve ortaya muazzam bir “anten”görüntüsü çıktı . Ama tabii ki bu birleşme ve iç içe geçme o kadar yavaş gerçekleşti ki saçılan yıldızlar bundan etkilenmedi . Peki bu galaksiler gelecekte ne duruma gelecek ? Astronomlara göre : 1 - 2 milyar yıl daha bu geçişler devam edecek ve sonra iki galaksi de kütle çekimsel denge aşamasına geçerek tek ve dev bir sarmal galaksi haline gelecek ! Bu birleşimin evrene faydası var mı ? Tabii ki var ! Galaksi birleşmelerinin en önemli faydası çok yoğun ve şiddetli bir yıldız oluşumunu tetiklemeleridir . Galaksilerin Kaotik birleşme döneminde her çeşit yıldız oluşumuna rastlarız . Önemli miktarda 1 - 15 milyon yıl yaşayabilen kısa ömürlü dev yıldızlar da oluşur . Bu dev yıldızlar önemlidir çünkü süpernova geçirerek yok olurlar ve bu süpernova sonucunda etrafa saçtıkları maddeler yıldızlarası gazı ağır elementler bakımından zenginleştirir . Bu zenginleşme sonucu bazı bulutsular yıldız oluşturabilmesi için tetiklenir ve tıpkı bizim Güneş’imiz gibi daha küçük fakat uzun ömürlü yıldız oluşumu meydana gelir . Ve bu oluşan yıldızlar da Dünya’mız gibi karasal gezegenlerin oluşumunu kolaylaştırır . Keşke insan ömrü yetseydi de bu tek ve dev galaksiyi gözlemleyebilseydik . Kim bilir , belki de 1-2 milyar yıl sonra bu birleşme sayesinde üzerinde canlıların var olduğu ve yaşayabildikleri birçok gezegen oluşacak.. Sizler için başta NGC 4039 ve NGC 4038 birleşiminin olmak üzere gönderiye birkaç galaksi çarpışmasının fotoğrafını ekledim , yana kaydırarak inceleyebilirsiniz 😄 Bir sonraki yazıma kadar beklemede kalın 🤙🏻"""},
"beyin_dalgaları":{"foto":"AgADBAADObQxG3gLqFGGt27ZIJNzwcpCYiNdAAMBAAMCAAN5AAOVYwACFgQ", "yazı":"""Daha önceki yazımızda bahsettiğimiz beyin dalgalarıyla ilgili şu an yapılan çalışmalara ve gelecekle ilgili beklentilere bir bakalım: Beyin dalgalarıyla ilgili yapılan çalışmalarda frekansların kontrol edilmesiyle bazı basit aktivitelerin zihinsel olarak  gerçekleştirilebildiği görülmüştür. Örneğin felçli bir hastaya elektrotlar bağlanarak alfabedeki harfler sırasıyla gösteriliyor. Hastanın harflere verdiği tepkiler elektrotlar sayesinde ölçülerek bir cümle oluşturulabiliyor. Evet, bu durumda doğal olarak hastanın bir cümle oluşturması çok uzun zaman alıyor. Buna benzer çalışmalar maymunların el veya kol hareketleri beyin dalgalarından bilgisayarlara oradan da robotlara aktarılarak yapılıyor ama beyinde aynı anda birçok dalga yayıldığı için basit hareketlerin dışına çıkmak istendiğinde çalışmalar da pek tabii zorlaşıyor. Ama gelecekte belki de dalgaların kontrolüyle felçli hastalar birtakım günlük işlerini robotlarla yerine getirebilecek, alzheimer hastalığına yine beyin dalgalarının kontrolü sayesinde çözüm bulunacak. Henüz bununla ilgili bir çalışma olmasa da bence gelecekte beyin dalgaları, şu anda fizyolojik reaksiyonlara göre çalışan yalan makinelerinin çalışma prensibinde yer alabilir. Hatta beyin dalgalarıyla ilgili çalışmaların başarılı sonuçlar vermesi hâlinde insan zihninin okunması gibi zararlı olabilecek durumlar da ortaya çıkabilir. Sizce gelecekte beyin dalgaları hangi alanlarda karşımıza çıkar?"""},
"lityum-metal_piller":{"foto":"AgADBAADOrQxG3gLqFFN-3CYL4DGe7AF_CJdAAMBAAMCAAN5AAPeyQEAARYE", "yazı":"""Lityum-Metal Piller\n\nŞarj edilebilir piller; telefonlar, bilgisayarlar, Bluetooth kulaklıklar gibi bir çok teknolojik cihaz için hayati bir önem taşıyor. Hayatımızın her alanında kullandığımız teknolojik cihazlar için bu kadar önem arz eden bir mataryelin şarj süresi, insan sağlığına zararı, enerji kapasitesi gibi özellikleri tabii ki bizi pek yakından ilgilendiriyor. Bu yüzden bu alanda sürekli çalışmalar yapılıyor. Günümüzde kullanılan son teknoloji lityum-iyon piller yüz altmış yıllık bir geçmişi olan kurşun-asit pillere oranla altı kat fazla enerji depolayabiliyor. Bunun yanında lityum-iyon pillerden daha fazla enerji depolayan piller de bulunmakta. Lityum-metal piller en iyi teknoloji ile üretilen lityum-iyon pillerden iki kattan daha fazla enerji depolama kapasitesine sahip. Lityum-metal pillerin bu artısından dolayı yaygın kullanımının önündeki engeller bilim insanları tarafından kaldırılmaya çalışılıyor. Peki nedir bu engeller? Lityum-metal pillerin dolum süresini bu engellerin başlıca örneği olarak yazsak hiç hata etmiş sayılmayız. Bu piller dolum süresinden kaynaklanan sorunlar sebebiyle şimdiye kadar laboratuvar ortamından ileriye taşınamadı. Son 50 yılda lityum-metal piller üzerinde çalışmalar yapılıp bazı gelişmeler sağlansa da bu gelişmeler lityum-iyon pillerin yerine geçmelerini sağlayacak düzeyde olmadı. Bir süredir California Üniversitesi San Diego'da bir grup araştırmacı lityum-metal pillerin önündeki engelleri kaldırmada önemli çalışmalar yapıyor. Pillerin içine yerleştirdikleri çok küçük bir cihaz problemleri ortadan kaldırıyor. Bu cihaz pilin bir parçası olarak pile entegre ediliyor ve anot ile katot arasındaki elektrolitin iyon dağılımını ultrasonik dalgalar yayarak düzenliyor. Kulağa hoş gelen bir çalışma değil mi sizce de? Kim bilir belki de önümüzdeki yıllarda lityum-iyon pillerden lityum-metal pillere doğru olacak büyük bir dönüşüm bizi bekliyordur?"""},
"starlink":{"foto":"AgADBAADO7QxG3gLqFH6uf9P0uhY_7KsySJdAAMBAAMCAAN5AATHAQABFgQ", "yazı":"""Merhabalar, bugün 28 Nisan 2020. Peki bu neden önemli? Dün yani 27 Nisan'da ülkemizin hem Marmara hem Ege denizine kıyısı olan güzel ilimiz Balıkesir'de akşam saatlerinde gökyüzüne baksaydınız eğer, karşınızda çoğu kişiyi heyecanladıracak bir şeyler görecektiniz. Günümüzde uzay yarışlarının lideri SpaceX'in,  tamamlandığında on iki bin uyduya ulaşacak Starlink projesinin birinci kısmı kapsamında 22 Nisan'da fırlatmış olduğu 60 uyduluk orduyu karşınızda daha doğrusu tepenizde görecektiniz. Nesnelerin interneti hakkındaki yazımızda kısaca #Starlink Projesinden bahsetmiştik, baktık geçtiğimiz günlerde @barisozcan da Starlink hakkında video çekmiş o zaman artık biz de yazalım dedik. Bugün gelin, Elon Musk'un artık alışılageldik çılgınlıklarından biri olan projeyi biraz daha yakından tanıyalım.\nStarlink 2015 yılında Musk tarafından duyuruldu. Uzun süren test ve hazırlık aşamalarından sonra ilk 60 uyduluk takım, tüm Dünya'ya en yüksek hızlı ve çok düşük maliyetli interneti sağlamak amacıyla 2019 Mayıs ayında uzaya fırlatıldı. Ee 60 uydunun kime ne faydası var diyebilirsiniz, haklısınız Elon da böyle düşünmüş olsa gerek; 2019 Kasım ayından itibaren her ay 60 uydu fırlatılmaya başladı. Bu uydular @SpaceX'in tekrar kullanılabilen Falcon 9 roketiyle fırlatıldığı için maliyeti çok ciddi anlamda düşürüyor. 60 uyduluk bir takımın yörüngeye gönderilmesi için 70-80 Milyon Dolar civarında bir bütçe gerekiyor, bu rakam normal şartlarda her ay belki de daha sık fırlatılacak bu takımlar için yüksek bir maliyet gibi gözükse de önümüzdeki yıllarda tamamen veri ve veri aktarımına dayalı bir ekonomi oluşacağını ve bu ekonominin yüksek hızlı internete ihtiyaç duyacağını düşünürsek bu maliyetler kimseyi etkilemeyecektir.\nBu proje fikrini Elon Musk ortaya atsa da kapitalizm yine paraya bakıyor. Amazon'un CEO'su Jeff Bezos, Musk'un ardından ağabeyini taklit eden bir çocuk misali 2019 yılında aynı amacı taşıyan Project Kuiper'ı duyurdu. Burada odaklanmamız gereken konu şu ki veri bizim yeni petrolümüz ve artık bunun çevresinde ilerleyeceğiz. Teknolojinin bize verdiği en önemli imkan, yarışacağımız insanların nerede olduklarını görmemizdir. Görüşmek üzere!"""},
"yeni_nesil_playstation":{"foto":"AgADBAADPLQxG3gLqFHROAbE2HTJ4Sf2ZCJdAAMBAAMCAAN5AANxNwIAARYE", "yazı":"""Japon teknoloji devi Sony, fuarların teker teker iptal olmaya başlamasının ardından(COVID-19 sebebiyle) yeni nesil konsolu PlayStation 5 hakkında YouTube üzerinden açıklamalar yaptı. Sony’nin önde gelen isimlerinden biri olan mühendis Mark Cerny, konferansta sözü ilk alan isim oldu. PlayStation tarihinden bahseden Cerny, PlayStation 4 ve sonrasında yaşanan değişikliklerden de bahsetti. PlayStation 4 ile birlikte üç yeni temel prensibe göre hareket etmeye başladıklarını söyleyen Cerny, evrim ve devrimi dengelediklerini dile getirdi. Bununla birlikte sürekli yeni özellikler eklediklerini belirten mühendis, yeni konsola alışma sürecinin daha hızlı olacağını söyledi. Konferansta PlayStation 4’lerdeki HDD’lerden SSD’ye geçildiği ve yeni GPU’ların da beklendiği üzere çok daha hızlı ve güçlü olacağı belirtildi. Ek olarak PS5'te ses için özel donanım da kullanılacak ve PS5 bir önceki jenerasyondan çok daha hızlı olacak. Esas SSD seçim nedeni ise hız değil, oyun yapımcılarına serbestlik vermek. Böylece oyuncuların da daha rahat hareket edebilmesi sağlanacak, yamalar daha hızlı inecek. PS5, 16 GB GDDR6 RAM ile gelecek. Oyunlar ve yayınlar 100 kat daha hızlı olacak. Yeni konsolda PS4 ve PS4 Pro oyunları legacy modunda mevcut olacak, PS5 oyunları ise native olarak çalışacak. Konsolda Ray Tracing desteği olacağı zaten biliniyordu ancak kullanım kapsamı bilinmiyordu. Bu özellik sadece küresel ışıklandırma için değil, gölgelendirme, ses ve yansıma gibi amaçlarla da kullanılacak. Peki yeni nesil playstation’ın özellikleri nasıl olacak:\n* İşlemci: 8x Zen 2 çekirdek - 3,5 GHz\n* GPU: 10,28 TFLOP, 36 CU 2,23 GHz\n* GPU mimarisi: Özel RDNA 2\n* Bellek: 16 GB GDDR6 / 256 bit\n* Bellek bant genişliği: 448 GB/sn\n* Dahili depolama: 825 GB SSD * IO: 5,55 GB/sn (Ham) 8-9 GB/sn (sıkıştırılmış)\n* Artırılabilir hafıza: NVMe SSD Slotu\n* Harici depolama: USB HDD desteği\n* Optik sürücü: 4K UHD Blu-ray sürücü (KAYNAK=WEBTEKNO)  Fiyata bakacak olursak durum pek de iç açıcı değil: PS5 fiyatı 6.989 Danimarka kronu! (yaklaşık 1000 dolar)\nOkuduğunuz için teşekkürler. Daha fazlası için beklemede kalın. 🤞🏻"""},
"elektrikli_otomobillerde_pil":{"foto":"AgADBAADQbQxG3gLqFHHHoIgi6F4H0hW8SJdAAMBAAMCAAN5AANfYwEAARYE", "yazı":"""Elektrikli Otomobillerde Pil🔋\nÖnümüzdeki yıllarda piyasadaki fosil yakıtlı otomobillerin yerini yüksek olasılıkla elektrikli otomobiller alacak gibi duruyor. Ve bugünki yazımız geleceğimizin bir parçası olan elektrikli otomobillerin en önemli bileşenlerden biri olan piller hakkında olacak. Elektrikli otomobillerde ağırlıklı olarak lityum-iyon piller kullanılıyor. Lityum-iyon pillerde kullanılan malzemeler üreticiden üreticiye değişse de bu piller genel olarak %60 Nikel, %20 Kobalt, %20 Manganez içeriyor. Fakat bu oranlar Kobaltın sürekli fiyatının artması sebebiyle önümüzdeki yıllarda değişecek gibi duruyor. Elektrikli otomobillerin pilleri ağırlıklı olarak Asya ülkelerinde üretiliyor. Üreticilere örnek verecek olursak Panasonic, LG, Samsung diyebiliriz. Önemli bir elektrikli otomobil üreticisi olan Tesla pil için Panasonic ile anlaşmış durumda. Ancak bunun yeterli olmadığını düşünen firma Gigafactory adını verdiği devasa fabrikalarda kendi pilini de üretmekten geri kalmıyor. Bu fabrikalarda ürettiği pillerin avantajı daha ucuz ve hızlı üretiliyor olması.\nElektrikli otomobillerde piller zemine döşeniyor. Bu sayede aracın bagajı daralmamış oluyor. Bunun yanında pillerin ortalama 500 kg ağırlığında olduğunu düşünürsek zemine döşenmeleri aracın, ağırlık merkezini aşağı çekilmesine ve yol tutuş kabiliyetinin artmasına sebep oluyor. Ve bu da elektrikli otomobillerin fosil yakıtlı araçlara oranla daha dengeli bir sürüş deneyimi sağlamasına imkan veriyor. Tabii ki böyle avantajlarının yanı sıra günümüz teknolojileri ile hala çözülememiş olan dezavantajları da bulunmakta. Bunlardan birisi pillerin hızlı şarj edilemiyor olması. Pillerin hızlı şarj edilebilmesi için kısa zamanda yüksek enerji sunan 'hızlı şarj istasyonları' kurulmasına ihtiyaç duyuluyor. Fakat bu da sorunun tamamen ortadan kalkmasını sağlamıyor çünkü pillerin şarj olurken ısınmaması için yazılımlar aracılığıyla dikkatlice izlenmesi ve ona göre enerji akışının ayarlanması gerekiyor. Diğer bir dezavantaj ise pillerin kullandıkça kapasite kaybına uğraması. Örneğin 250.000 km sonra pil kapasitesi %90'a düşüyor. Peki sizce önümüzdeki yıllarda pil teknolojisi nasıl değişecek?"""},
"dünyanın_en_değerli_şirketi":{"foto":"AgADBAADQrQxG3gLqFGoewgqFB7GXGJiJdAAMBAAMCAAN5AAMRyAEAARYE", "yazı":"""Geçtiğimiz günlerde @apple düşük bütçeler odaklı yeni nesil iPhone SE'yi duyurdu. #Covid-19 sebebiyle alışık olduğumuz o heybetli lansmanlardan birini yapamasa da Apple bizi şaşırtmıyor ve yıllardır kullandığı tasarımı ve donanımı bir kez daha bizlere sunuyor. Yeni nesil #iPhoneSE bana, bir telefonun düşündürebilceklerinden çok daha fazla şey düşündürdü. Apple'ın son yıllarda elinde tuttuğu tasarımları muhafaza ettiğini ve ısrarla yeni bir tasarım yapmadığını hepimiz net şekilde görebiliyoruz.Rakipleri Huawei, Samsung, Xiaomi gibi artık dev diyebileyceğimiz şirketlerin satış rakamları, son yıllarda yaptıkları harika tasarımlar ve çığır açıcı teknolojilerle çokça ivme kazandı. \nBunları göz önünde bulundurunca 1976'dan bu yana, insanların gündelik hayatlarını kolaylaştırmayı hedefleyen ve yeni nesil teknolojiler üreten bir şirketten yeni tasarımlar, teknolojiler ve farklı bir estetik algı beklemek pek hayalci olmaz.Fakat Apple'ın Steve Jobs'ın ölümünden sonra yaşadığı vizyon değişikliklerini pek çok insan fark edemese de şirketin ürünlerinde yaptığı radikal değişiklikler bu durumu belli ediyor. Steve Jobs'un son döneminde iPhone 4'lerde 2 renk seçeneği vardı. Jobs insanlara istediklerini seçme hakkını vermenin Apple'ın vizyonuna aykrı olduğunu düşünüyordu. Jobs'un çekilmesiyle iPhone 6 modellerinden itibaren telefonlarda bol bol renk ve seçenek gördük. Burada değinmek istediğim nokta; hayran olduğumuz, yenilikçi ve vizyonlarına bağlı bir Apple ne yazık ki artık yok.\nUluslarası bazı teknoloji gazetelerinin araştırmalarına göre şu an güncel model olan iPhone 11 Pro Max'in 1199$ açılış fiyatıyla Apple'a malzeme maliyeti 490.50$. Tabii ki %100'lük net bir kârdan bahsedemeyiz zira maliyetin üzerine işçilik, reklam, dağıtım gibi kalemler de eklenecektir ama Xiaomi'nin ürünlerinden %5 kâr ettiği bu sektörde Apple'ın bizlere hayranı olduğumuz ürünleri satarak oldukça fazla kâr ettiğini bilmek hepimizin hakkı. Apple'ın 2019 yılında 60 milyon Air Pods sattığını ve Apple Watch ürününden 5.2 milyar dolar gelir elde ettiğini düşündüğümüzde, ülkemizde hâlâ tarım alanındaki yatırımları desteklememiz gerektiği aşikâr. Bugün kısaca Apple'ın neden Apple olduğunu anlatmak istedim."""},
"beyaz_cüce_çifti":{"foto":"AgADBAADQ7QxG3gLqFGldlRFqB6V8rqaAAEjXQADAQADAgADeQADzcYBAAEWBA", "yazı":"""Beyaz cüceler, düşük kütleli yıldızların ölümünden geriye kalan , büyük oranda helyumdan oluşmuş yoğun ve ağır yıldız çekirdekleridir . Çapları neredeyse Dünya’nınkiyle aynıdır. Peki neden bu sıralar uzay bilimcilerin göz bebeği haline geldiler? Yakın zamanda Harvard & Smithsonian Astrofizik merkezindeki bilim insanları, J2322+0509 adını verdikleri birbirinden bağımsız 2 helyum çekirdeğe sahip ve kısa yörünge periyotları olan bir beyaz cüce çifti keşfettiler . Aslında bu durum çok da şaşırılacak bir şey değildi . Burada gerçekten inanılmaz olan şey : ilk defa kara delik ve nötron yıldızı çarpışmasından başka bir oluşumun Kütle Çekim Dalgası ( Uzay Zaman Dalgalanması ) yaymasıydı ! Bu keşif uzay bilimcilerin önünü fazlasıyla açacak belki de uzay araştırmalarında bir dönüm noktası olacak niteliktedir. Teoriler evrende bu tarz birçok beyaz cüce çifti olduğu kanaatinde . Bilim insanları J2322+0509 sisteminin araştırmak için zorlu olduğunu fark ettiler ve şimdilik kritik bilgileri toplamaya odaklandılar. Optik ışık eğrisi ve fotometrik sinyaller işe yaramadı çünkü çiftin ne bir optik ışık eğrisi ne de fotometrik sinyali vardı. Ancak spektroskopik çalışmalar beyaz cüce çiftinin yörünge hareketlerini bilim adamlarına sundu . Yıldız çiftinin yörüngesel periyodunun 20 dk olduğu keşfedildi ve bu da beyaz cüce çiftimizi yörüngesel periyodu en kısa yıldız çifti sıralamasında ilk 3’e soktu . J2322+0509’un başka bir ilginç yanı da yaydığı kütle çekim enerjisinden dolayı kendi yörüngesini bozması ve 6-7 yıl içerisinde birleşip daha kuvvetli bir enerji yayacak yıldız haline gelecek olması. Oklahoma Üniversitesi’nden Dr. Mükremin Kılıç ; J2322+0509’un 2034 yılında faaliyete geçmesi düşünülen LISA kütle çekim gözlemevinde doğrulama yapmak için kullanılacağını söyledi : “LISA’nın faaliyete geçtikten sonra teleskoplarını onlara döndürerek birkaç hafta içerisinde bu yıldızları görebileceğini biliyoruz. Bugün elimizde bildiğimiz az sayıda LISA kaynağı bulunmakta ve bu yeni çift yıldız sınıflandırma prototipinin bulunması bizi hiç kimsenin tahmin edemeyeceği bir yerin ilerisine götürecek.” Bir sonraki haftada başka bir yazıda görüşmek üzere ! Hoşçakalın."""},
"beyin_dalgaları":{"foto":"AgADBAADRLQxG3gLqFFEUhiWOlKg3AxCYiNdAAMBAAMCAAN5AAPVYgACFgQ", "yazı":"""Beyin dalgaları 🧠\nBeyin dalgaları optimum düzeyde çalıştığında beynimiz ve tabii aktivitelerimiz normal düzeyde işler. Beynimizde kendine özgü özellik ve frekansları olan beş dalgadan bahsedebiliriz:\n1-Delta(0.1-3 Hz): En düşük frekansa sahip dalgadır. Derin ve rüyasız uyku anlarında görülür. Bu dalga türü bebek ve çocuklarda daha etkindir. Bizler bu durumu yaşlandıkça uyku kalitemizin azalmasında gözlemleyebiliriz. Delta dalgaları arttığı zaman odaklanma ve dikkat becerimiz kısıtlanır.\n2-Teta(4-8 Hz): Bu dalga türü daha çok hayal gücü ve düşünme ile ilgilidir. Sağlıklı bir seviyede yaratıcılık, duygusal bağlantı ve sezgi düzeylerini artırır. Aksi takdirde stres, depresif bozukluk, anksiyeteye yol açabilir.\n3-Alfa(8-12 Hz): Alfa dalgaları daha çok kendimizi rahat ve sakin hissetmemizi sağlar. Yani huzur ve dinlenme hâlinde ortaya çıkıyor diyebiliriz. Tabii ipin ucu kaçtığında fazlasıyla rahat hatta enerjisiz hissetmemize yol açar.\n4-Beta(13-30 Hz): Beta dalgaları daha çok konsantrasyon ve buna bağlı olarak işlerimizi dikkatle yürütmemizde önemlidir. Bu dalgaların salınımı azaldığında depresif bir hâle bürünebiliriz.\n5-Gama(30-100 Hz): Gelelim uzmanlar tarafından beyinle ilgili işlevi tespit edilemediği için bir süre beyin dalgaları kategorisinde olamayan gamaya. Gama frekansı en yüksek olan dalgadır. Bu dalganın bilişsel işlevimizle olan ilgisi şöyledir: en yoğun odaklanma anlarımızda ya da tamamen mutlu hissettiğimizde arka planda gama vardır. Yani gama zihin kapasitemizi tam anlamıyla kullanabilmemizi sağlar. Yüksek duyu algımızda; bir şeyleri daha iyi hatırlamamızda; kokuları, tatları daha yoğun hissetmemizde etkilidir. Bunun sebebi gamanın frekansının çok yüksek olmasıdır. Frekans yüksek olduğu için nöronlar arasındaki bağlantı daha iyi ve hızlı sağlanmaktadır. Peki bu dalganın az ya da çok olması neyi değiştirir? Eğer gama daha çok etkinse yüksek IQ ve algılama düzeyinde önemli bir etkiye sahip olur. Bir sonraki yazıda görüşmek üzere 🤙🏻🤙🏻"""},
"radyoaktivite":{"foto":"AgADBAADRbQxG3gLqFHMOed1Z2o8t5ofAiNdAAMBAAMCAAN5AAPDwwEAARYE", "yazı":"""Hepimiz radyasyon hakkında pek çok şey duyuyoruz ama çok az insan gerçekten ne olduğunu biliyor. Radyasyon her tarafımızdadır ve birçok şekil ve biçimde gelir, doğal veya yapay olabilir. Doğal radyasyonlar güneşten gelen radyasyonu, aynı zamanda topraktaki ve yeraltı kimyasallarındaki radyoaktif minerallerin yaydığı radyasyonu da içerir. Yapay radyasyon, cep telefonları, televizyonlar, mikrodalgalar ve sadece birkaç kaynağı isimlendirmek için üretilir. Bazı radyasyon iyidir, bazısı kötü. Öyleyse nasıl olduğunu görelim!\nHikaye 1895 yılında fizikçi Wilhelm Röntgen’in X-ışınlarını keşfettiği zaman başladı. Bir yıl sonra Henri Becquerel, X-ışınlarının özelliklerini incelemek için potasyum uranil sülfat gibi doğal flüoresan mineralleri kullanıyordu ve bu süreçte radyoaktiviteyi keşfetti. Ancak en önemli katkı kocasıyla birlikte çalışan, radyoaktivite anlayışımızı büyük ölçüde genişleten Marie Curie’den geldi. Keşiflerinden dolayı Nobel ödülü kazanan ilk kadındı. 1898’de radyoaktif element radyumunu keşfetti. Fakat radyoaktivite nedir? Atom çekirdeğindeki “kararsız” enerji salınımıdır (radyasyon). Radyasyon emisyonu çekirdeğin daha kararlı bir enerji durumuna geçmesine yardımcı olur. Birkaç çeşit radyasyon vardır: alfa, beta, gama, vs. Radyoaktif enerji nükleer reaktörlerde toplanır ve toplumumuzu güçlendirmek için kullanılır. Nükleer santraller düzenli olarak enerji üretmek için uranyum kullanır. Radyoaktivitenin başka endüstriyel uygulamaları da vardır: malzemelerin analizi, endüstriyel radyografi ve daha fazlası. Bazıları radyasyonun tehlikeli olduğunu düşünür, bu çoğu durumda doğrudur. Ancak bazı radyasyon türlerinin bizim için iyi olduğunu unutmayın. Örneğin güneşten kaynaklanan bir tür doğal enerji olan ultraviyole ışınımı (UV olarak da bilinir), D vitamini üretimini teşvik eder. Bu nedenle, kendinizi biraz güneş ışığına maruz bırakmak faydalıdır ancak uzun süre maruz kalmak için güneş kremi gibi ürünleri kullanmayı unutmayın. Güneşten gelen fazla radyasyon cildimize ulaştığında tehlikeli hale gelir. Sonuç olarak her şeyin azı da fazlası da zararlı. Radyasyonunuz eksik olmasın! Ama gene de evden çıkmayın!"""},
"elektrik_üreten_iplik":{"foto":"AgADBAADRrQxG3gLqFEZV0fay5gBawjTIBsABAEAAwIAA3kAA0_aBwABFgQ", "yazı":"""Twistron Günümüzde nanoteknoloji birçok alanda kullanılmakta. Bunlardan birisi de Twistron:\nTeksas Universitesi ve Güney Kore Hanyang Üniversitesi bilim insanları, esnetildiğinde veya büküldüğünde elektirk üretebilien bir iplik geliştirdi. Twistron, jel kaplı karbon nanotüplerden yapılmış bükümlü bir elyaftır. Ayrıca elektrik üretebilmesi için herhangi bir pil ya da aygıta ihtiyaç duymuyor.\nTwistron'un çalışma prensibinden kısaca bahsedelim:\nİplik bükülerek içindeki karbon nanotüplerin hacmi azaltılmış oluyor. İplikler bir araya gelince enerjileri artıyor. İplikçiklerdeki enerji miktarı arttığı için elektrik üretiliyor.\nBu çalışmalara öncülük eden, Teksas Üniversitesi'nden Carter Haines iplikler hakkında " Oldukça kolay kullanıma sahip bir parça ipliğiniz var. Uzatıyorsunuz ve elektrik geliyor." diyor. Yani bir örnekle açıklayalım. Düşük enerjili elektronik aletleri giydiğimiz kıyafet ile çalıştırabiliriz. Tabii bu iplikleri her kıyafete uygulamak ne kadar mümkün bilemeyiz. Çünkü üretim şu an ucuz değil.\nAyrıca önceki yazılarımızdan olan" Nesnelerin İnterneti" konusunda da pek çok yerde işe yarayacağı düşünülüyor. 31 mg'lık bir iplik ile 100 metreye 2 kb'lık bir veri iletilelebiliyor. Bu iplikler kıyafetlerimizde kullanıldıkça kablolardan bi nebze de olsa uzaklaşacağız diye düşünüyorum. Sizce de öyle olur mu? Düşünsenize siz spor yaparken telefonunuz cebinizde şarj oluyor. Harika bir şey!.\nYazımı okuduğunuz için teşekkürler."""},
"uzay_sondası":{"foto":"AgADBAADR7QxG3gLqFH7rFUZWnBKqp6jtBsABAEAAwIAA3gAAyx1BgABFgQ", "yazı":"""Henüz bir insanı uzayın derinliklerine götürebilecek bir teknolojiye sahip olmasak da bugüne kadar uzayın gizemini çözmek ve onu keşfetmek için pek çok araç uzaya gönderildi.İçinde astronot olmayan ancak gelişmiş aygıtlarla donatılmış bu araçlara uzay sondası deniyor. Uzay sondaları yeryüzündeki bilim insanları tarafından yönetilip yönlendirilerek uzayda dolaşıyor ve bilgi topluyor. Uzay sondalarının görevi uzaydan yeryüzünü incelemektir yani uzak gezegenlerle , yıldızlarla , asteroitlerle ya da galaksilerle ilgili bilgi toplamaktır . Bir gezegene inerek örnek toplayabilir, onun çevresindeki yörüngesinde hareket edebilir ya da uzaydaki çok uzak yerlere gidebilirler. Elde ettikleri bilgileri Dünya'ya ya da bir uzay aracına iletirler. Bunu genellikle radyo dalgaları ile iletirler ve güç kaynakları bitene kadar görevlerine devam ederler. İlk uzay sondalarının güç kaynakları,oldukça sınırlı süre çalışmalarına izin veriyordu.Ancak yeni nesil sondaların çoğunun Güneş'ten enerji elde edebilen ya da nükleer enerjiyle çalışan sistemler var.Bu gelişmeler sayesinde uzay sondalarının görev süreleri oldukça uzadı. Sputnik 1 adındaki ilk sonda Sovyetler Birliği tarafından 1957'de uzaya gönderilmişti.Bu tarih uzay çağının başlangıcı olarak görülüyor.Sputnik 1 üç hafta boyunca Dünya'nın çevresindeki alçak yörüngede dolanarak bilgi topladı.Bilgiler Dünya'ya iletti.Enerjisi bitince 2 ay daha atmosferde kaldı.Sonra da atmosfere girerek yandı.Daha sonraları uzaya bir sürü sonda gönderildi.Voyager 1 ve Voyager 2 olarak adlandırılan ikiz uzay sondaları en ünlü olanlardır.Ünleri uzayda en uzun süredir çalışır durumda olmasından kaynaklanıyor.1977'de fırlatıldılar ve görevlerine hala devam ediyorlar."""},
"teknotik_silahlı_saldırı":{"foto":"AgADBAADSrQxG3gLqFGiyViiKUV-hMiteiNdAAMBAAMCAAN4AAMSOwEAARYE", "yazı":"""Bilinçli olarak deprem, tsunami, aşırı sıcaklar tektonik silahlı saldırı olarak nitelendiriliyor. Depremin silah olarak kullanılması fikri bazı ülkelerce kabul edilmese de bu teori hala tartışılıyor. Sırp asıllı ünlü Amerikalı mucit Nikola Tesla'nın temellerini kurmuş olduğu bir teknoloji. Sonrasında bunu geliştirmek de Amerika'ya kalmış. Günümüzde HAARP; ABD Kara Kuvvetleri, Deniz Kuvvetleri ve Alaska Üniversitesi tarafından ortak yürütülen bir çalışma. İçinde yaşadığımız zamanın en üstün "HARP" teknolojisi olarak da görebileceğimiz bu teknoloji, elektromanyetik sinyallerle çok büyük enerjileri kontrol etme mantığı üzerine kurulu. Türkçe karşılığı Yüksek Frekans Aktif Güneşsel Araştırma Programı olan bu sistem; yüksek enerjiler kullanarak aktif ve güçlü radyo dalgaları oluşturmakta.1997 yılında projenin son safhası tamamlandığında, 3 milyar wattlık bir güçten fazla enerjiyi atmosferin üst katmanlarına yaymak için dizayn edilmiş güçlü bir verici inşa edilmişti.Proje dünyanın en büyük "iyonosfer ısıtıcısını" içeriyordu ve iyonosferin ısıtılması yoluyla VLF yani "çok düşük frekans" dalgaları üretilmekteydi. Bu amaçla" yüksek frekans bazlı bir radyo vericisi" kurulmuş ve 72 fit yüksekliğinde 180 kule inşa edilmişti. Kısaca Tesla, atmosfere bir manyetik dalga göndermiş ve bunun çok daha güçlü bir enerji olarak döndüğünü görmüştür. Fakat Tesla bunu insanlığın iyiliği için kullanmak istemiştir, 40 km'den 100 ampulü kablosuz yakması ve elektiriğe meydan okuması, büyük şirketleri tedirgin etmiştir ve ortaya çıkmasına izin verilmemiştir. HAARP şu an Rusya ve Amerika'nın elinde büyük bir güçtür. En önemli becerileri:\n-Hava koşullarını yönetmek\n-Deprem oluşturmak\n-insan beynini etkilemek\n-Dünyanın diğer ucundaki cihazları etkisiz hale getirmektir."""},
"dünyaya_dönüş":{"foto":"AgADBAADS7QxG3gLqFHJx9wg3XDcocDFzyJdAAMBAAMCAAN4AAO6xgEAARYE", "yazı":"""Uluslararası Uzay İstasyonu Dünya'nın yörüngesine yerleştirilmiş bir uydu.Astronotlar,soyuz adı verilen uzay aracıyla bu uzay istasyonuna gidebiliyor.Burada bir süre kalıp çeşitli deney ve gözlem yapıyorlar.Görevlerini tamamladıktan sonra Dünya'ya dönüşleri ise gidişleri kadar macera dolu oluyor. Soyuz kapsülü yörünge modülü,iniş modülü de denen yeniden giriş modülü ve servis modülü olmak üzere üç bölümden oluşur.Soyuz kapsülünün en üstünde yer alan yörünge modülü uluslararası Uzay İstasyonu'na bağlanan modüldür.Ortada yer alan yeniden giris modülü ise Soyuz Kapsülünün dönüşte atmosfer tabakalarını geçerek yeryüzüne ulaşan tek parçasıdır.Astronotlar hem gidiş hem dönüş yolculuğunda bu modülde bulunur.En alt modül ise servis modülüdür. İlk olarak Soyuz Kapsülü istasyondan ayrılır.Kapsül ayrıldıktan ve istasyondan yeterince uzaklaştıktan sonra çok kısa bir süreliğine geri itiş motorları ateşlenir.Böylece iki uzay aracı birbirinden iyice uzaklaşır.Ardından Soyuz Kapsülü Dünya'nın cevresinde sabit bir yörüngede yaklaşık iki buçuk saat boyunca dolanır.Bu sırada modüldeki astronotlar yeniden atmosfere giriş için tüm kontrolleri yapar ve uzay aracının ana motorları ateşlenir.Yaklaşık yarım saat sonra atmosfere girmeden hemen önce,yeniden giriş modülü yörünge ve servid modülleri atmosferde yanar.Yeniden giriş modülleri ise atmosferin yoğun katmanlarına girerek yeryüzüne yaklaşmaya devam eder.Bu sırada görev kontrol merkezi ile iletişim kurabilmek için telsiz de devreye girer.Bu sırada uzay aracı atmosfere girmiş olduğundan kütle çekim kuvveti nedeniyle çok yüksek bir hiza ulaşır.Yeniden giriş modülü atmosferden geçerken aşırı basınca ve sıcaklığa maruz kalır.Öyle ku uzay aracının çevresinde yaklaşık 2000℃ dereceyi bulan bir gaz bulutu olur. Yeniden giriş modülü birkaç dakika boyunca bu yüksek hızla Dünya'ya yaklaşmaya devam eder.Atmosfer katmanlarını geçtikten sonra,yeryüzünden yaklaşık 8,5 kilometre yükseklikte,pilotun komutuyla,modüldeki dev paraşütler açılır.Daha sonra da modül daha önceden belirlenen alana iniş yapar.Kapsülün istasyondan ayrılırması ile başlayıp yeniden iniş modülünün yeryüzüne inmesine kadar süren dönüş yolculuğu 3,5 saat kadar sürer."""},
"çip_üzerinde_organlar":{"foto":"AgADBAADTrQxG3gLqFHxts0Z9WjD5wxa1CJdAAMBAAMCAAN5AAPvwwEAARYE", "yazı":"""Çip Üzerinde Organlar\nYeni ilaçlar üretmek hem çok maliyetli hem de uzun süren bir süreç. Bu ilaçların yapılmasının yanı sıra Ar-Ge çalışmalarına da milyarlarca dolar yatırılıyor. Ayrıca yeni bulunan bir ilaç onaydan geçemez ise piyasaya sürülemiyor. Bu da tahmin edeceğiniz üzere zarar etmek demek. Her şeye bi' çare bulan(!) teknoloji bunun da çaresini buldu tabii ki. Wyss Enstitüsü "çip üzerinde organ" adını verdikleri çipler geliştirdi. Bu çipler insana verilecek ilacın güvenilir olup olmadığını, ne kadar sürede etki edecegini, işe yarayıp yaramadığını tespit edebilecek. Böylece hem daha kısa sürede sonuç elde edilecek hem masraflar azalacak hem de hayvanlar üzerinde deneyler azalacak. Peki nasıl çalışıyor bu çip organlar? Her ne kadar bilgisayar parçasına  benzeseler de onlar birer yapay organ. Her organ için farklı bir çalışma sistemi bulunmakta. Akciğer örneğine bakacak olursak: Baş parmak büyüklüğündeki çipin içinde 3 adet akışkan sıvı kanalı var. Merkezde ise bir por yani esnek bir zar var. Zarın üzerine akciğer hücreleri (akciğer çipi olduğu için akciğer hücresi, dilerseniz başka hücreler de koyulabiliyor) koyuluyor. Onların altında kılcal hücreler yani kan hücreleri var. Daha sonra çipe zarı esneten ve kasan mekanik kuvvetler uygulanıyor. Bu sayede hücreler, solunum sırasında oluşan mekanik kuvvetleri vücudumuzda gibi yaşayabiliyorlar. Tepe kanalından hava akışına, alt kanaldan ise besin içerikli sıvı akışına sahipler.\nNe işe yararlar?\nYine akciğer örneğinden gidelim. Mesela çipteki akciğer hücresine bakteri gönderdiğimizi düşünelim. Kan kanalına da akyuvarlar gönderelim. Akyuvarlar zardan geçerek bakterileri yutacaktır. İşte bunun gibi deneylerle ilaçlar bulunabilmekte.\nYazımda da dediğim gibi bu çipler bilgisayar parçasına benzemekte ve bildiğiniz üzere günümüzde robotlar da gelişmektedir. Bu konuyu araştırırken aklıma bir soru geldi: Robotlara bu yapay organları takarak yapay insanlar, veya ameliyatlar yapılabilir mi? Peki siz ne dersiniz, yapılabilir mi?\nYazımı okuduğunuz için teşekkür ederim."""},
"nesnelerin_interneti":{"foto":"AgADBAADb7QxG3gLqFGhjJ_5IrB5FqZY8SJdAAMBAAMCAAN5AAOhXwEAARYE", "yazı":"""Bugün uzun zamandır bildiğimiz ama önemi her geçen gün artan nesnelerin internetini tanıyacağız. Nesnelerin interneti yani daha popüler ismiyle internet of things. Peki nedir bu IOT? IOT fiziksel nesnelerin birbirleriyle ya da başka sistemlerle iletişime geçerek veri paylaşımı yapmasıyla akıllı bir ağ yaratan sistemlerdir. Nesnelerin interneti uzun yıllardır bilinmesine rağmen hala çoğumuzun hayatında net şekilde etkisini göremiyoruz. Aslında bu sistem hayatımızı arka planda kuvvetli şekilde etkileyecek Endüstri 4.0, otonom sürüş ve akıllı şehirler gibi çığır açan teknolojierin temelini oluşturuyor. Nesnelerin internetinin hayatlarımızı doğrudan etkilemesi için akıllı nesnelere ihtiyacımız var. Günlük hayattan bir örnek vermemiz gerekirse 2019 sonunda hepimizin heyecanla takip ettiği yerli otomobilimiz TOGG'un tanıtım filmlerinin birinde şu tarz bir örnek gösterilmişti:\ntomobiliniz ile evinize doğru yol alırken otomobil sesli asistanınıza eve gittiğinizi, eve ulaştığınızda oturma odasının sıcaklığının 21°C olmasını istediğinizi söylerseniz; otomobil asistanınız yapay zekası sayesinde, nesnelerin internetini kullanarak evinizdeki akıllı sisteme bir bilgilendirme yapacak ve eve ulaşma sürenizi hesaplayıp eve ulaştığınız zaman oturma odanızın sıcaklığını akıllı ısıtma sistemlerini kullanarak 21°C'a ayarlayacaktır. İşte bu örnek gibi hayatımızı oldukça kolaylaştıracak ve bizleri teknolojinin doruklarına ulaştıracak bu ekosistemler nesnelerin internetine dayanıyor.\nPeki sadece akıllı cihazlar bu ekosistemi oluşturmak için yeterli mi? Sanki bir şeylere daha ihtiyacımız var değil mi? Mesela internet İşte burada karşımıza bütün heybetiyle, Elon Musk'ın tüm Dünya'ya ücretsiz internet sağlama projesi olan Starlink çıkıyor. Starlink SpaceX'in Dünya yörüngesine binlerce uydu göndererek Dünya'nın her yerine internet ulaştırma projesidir. Bu uzun vadeli plan nesnelerin interneti için olağanüstü bir basamak olacaktır. Space X'in bu projede tekrar tekrar kullanılabilen Falcon 9 roketleri kullanması da maliyeti çok ciddi oranda düşürüyor. Eğer isterseniz Starlink projesini daha geniş şekilde başka bir yazıda ele alabilriz.Teşekkürler."""},
"elektrikli_arabaların_tarihi":{"foto":"AgADBAADcLQxG3gLqFHmA1OO4EaNMpCo5iJdAAMBAAMCAAN5AAPCyQEAARYE", "yazı":"""Elektrikli Otomobillerin Tarihi\nElektrikli otomobiller ile fosil yakıtlı otomobiller arasındaki savaş aslında yüz yıl önceye dayanıyor. İlk otomobiller 1800'lerin ortalarında üretilmeye başlansa da seri üretime 20. yüzyılda geçildi. 1900 yılında ABD'de satılan 4200 otomobilden 1681'i buharlı, 1575'i elektrikli, 936'sı içten yanmalıydı. Fakat bundan tam 17 yıl sonra durum tam tersine dönmüştü. Trafikte 50.000 elektrikli otomobil bulunmasına karşın 3,5 milyon içten yanmalı otomobil bulunuyordu. Buharlılar ise çoktan tarih olmuştu. Peki insanlar neden elektrikli otomobil yerine içten yanmalı otomobilleri tercih ediyordu?\n1900'lü yıllarda elektrikli otomobiller günlük ulaşım ihtiyacını en iyi şekilde karşılıyordu. Hem güçlü hem de diğer otomobillere göre frenlemesi daha iyiydi. Yüksek torku sayesinde ağır yükleri kolayca taşıyabiliyordu. Ama gel gelelim bu araçların günümüzde bile sorun olmayı sürdüren menzil sıkıntısı vardı. Yaklaşık 60 km'lik bir menzile sahipti. Bu menzil şehir içinde yeterli olsa da içten yanmalı otomobiller şehirler arası yolculuklar yapmaya başlayınca işin seyri değişti. Şehir dışında elektrik hatları yaygın değildi ve araçları şarj etmek büyük bir problem oluyordu. Kurşun asitli aküler (elektrikli otomobillerde kullanılan tekrar şarj edilme özelliği olan aküler) pahalıydı. Üstelik bu akülerin kullanım ömrü de uzun değildi. Ayrıca elektrik motorları da pek küçük değildi.\nTüm bu sorunlar neticesinde elektrikli otomobiller günlük hayattan silindi ve yüz yıl boyunca neredeyse gündeme gelemedi. İşin ilginç yanı ise elektrikli otomobilleri günlük hayattan silen ve tarihe gömen sorunların bir kısmı bugün bile tam olarak çözülebilmiş değil.\nKim bilir belki de bizim önümüzdeki yüz yıl boyunca da elektrikli otomobiller içten yanmalı otomobilleri tarihe gömecek hamleler yapacak?"""},
"G-kuvveti":{"foto":"AgADBAADcbQxG3gLqFGxDFS40uAcFRBFlCJdAAMBAAMCAAN5AANILwMAARYE", "yazı":"""G-KUVVETİ\nG kuvveti daha çok astronot ve pilot eğitimlerinde karşımıza çıksa da, fiziksel bir ifade olan bu kuvvet hayatımızın her anında bulunmaktadır. G Kuvveti, adını kütle çekimi anlamına gelen “gravitational” kelimesinden alır. Bir kütleye belirli bir durumda etki eden hızlanma olarak tanımlanır ve akselerometre ile ölçülür. Daha basit bir ifadeyle, çaycının içerisinde çayların olduğu bir tepsiyi düşürmeden çevirmesi, G kuvveti sayesinde olur. Yani bir cismin herhangi bir yönde, kendisine uygulanan bir kuvvet sayesinde hızlanarak veya yavaşlayarak “ağırlık” değeri üretmesidir diyebiliriz. her gün kullandığımız asansörlerde, bulunduğumuz kattan aşağı ya da yukarı hareketlerde vücudumuz bu kuvvete maruz kalır. Pilotlar ve astronotlar, eğitim sırasında 9G kuvvetine kadar deneyimler. Bunun sebebi ise anı basınç değişimlerine karşı pilotu hazırlamaktır. Örneğin bir pilot sert bir manevra sırasında, 9 G kuvvetine kadar hissedebilir. Bu durumda pilot kendi ağırlığını 9 kat fazla hisseder. Buna pozitif G denir. Basıncın etkisiyle kan, beyinden aşağıya doğru hareket eder. Buna bağlı oksijen yetersizliği, görme kaybına ve daha ileri aşamalarda ise bayılmalara neden olur. Bu durumun yaşanmaması için pilotlar özel olarak üretilmiş G-Suit adı verilen elbiseler giyerler. Negatif G ise pozitif G’nin tam tersidir. Bu esnada kan yukarı doğru hareket etmeye başlar ve ağırlığınız azalır. Bunun yanında bir de 0 G kuvveti vardır. 0 G etkisinde yer çekimi sizin için artık geçerli değildir. Normal hayatımızda da G-kuvvetine mağruz kalırız fakat bu kuvvet 1 G-kuvvetine eşittir,herhangi bir basınç hissine kapılmayız. Peki g kuvveti testi nedir? G kuvveti serbest hareket eden bir nesnenin maruz kaldığı "kütleçekimsel olmayan" kuvvetlerin vektörel toplamıdır. Kütleçekiminden kaynaklanmayan hızlanmalara "gerçek ivme" denir ve g kuvveti hesaplanırken sadece bunlar kullanılır. g kuvveti arttıkça nesne üzerindeki gerilim artar. Formülü ise :Ağırlık = kütle x (- g-kuvveti )’dir."""},
"akıllı_giyilebilir_güç":{"foto":"AgADBAADcrQxG3gLqFGH2zKdqO7FVAABLwUjXQADAQADAgADeQAD3F4BAAEWBA", "yazı":"""Biyonik zırh ilk olarak Crytek firmasının yaptığı Crysis oyununda ele alınmıştı. Şimdi ise gelişen teknoloji ile gerçeğe dönüşmesinde engel kalmıyor. .Bildiğimiz üzere dünyada film ve oyun sektöründeki ütopik icatların gerçekleşmesi insanları heyecanlandırıyor. Bu icatların genelde savaş standartında icatlar olması üzücü olsa da yakın geleceği daha heyecanlı kılıyor.\nBu zırh kolay giyilebilen, esnek bir tulum gibi olduğundan ve üzerindeki gelişmiş sensörler ve hidrolik sıvıyı hareket ettirebilen küçük elektrik motorları sayesinde ağır yükleri kolay taşıyabiliyor, hatta kendi ağırlığını bile olduğundan az hissederek daha rahat edebiliyor. Askerlerin kıyafet şeklinde giyebileceği bu zırh ; onlara daha hızlı koşma, daha yükseğe zıplama imkanlarını da veriyor. Bu teknolojiye ise '' Intelligent Wearable Strenght '' yani Akıllı Giyilebilir Güç deniyor.\nBuna benzer teknolojiler, öncelikle cephe hattında görev yaparken ağır yükler taşımak zorunda kalan askerlerin işlerini kolaylaştırmak için geliştiriliyor.\nHenüz resmi tanımı olmasa da ileride gerçeğe dönüşmesi olası olan biyonik zırhlar hakkında mühendisler durmadan çalışırken tam olarak ne zaman gerçeğe döneceği de merak konusu..."""},
"yapay_zeka":{"foto":"AgADBAADc7QxG3gLqFHms0u4IpWHaCureiNdAAMBAAMCAAN5AAMDQAEAARYE", "yazı":"""Yapay Zeka Nedir? . Yapay zeka bilgisayarın veya bilgisayar kontrolündeki bir robotun çeşitli faaliyetleri zeki canlılara benzer şekilde yerine getirebilme kabiliyetidir. Yapay zeka çalışmaları genellikle insanın düşünme yöntemlerini analiz ederek ,bunların benzeri yapay yönergeleri geliştirmesine yöneliktir. Yani bilgisayarın ,insanlar tarafından gerçekleştirilen görevleri yerine getirmesini sağlar. Yapay zeka bilgisayarların insanlar gibi düşünmesini sağlar. Zekâ ve akıl gerektiren sorunlar artık bilgisayarlar yardımıyla etkili bir şekilde çözülebilir.\n. Yapay zeka sistemleri bir şeyler gözlemlemekte ve daha sonra önceden belirlenmiş parametreler temelinde onu tanımaya çalışmaktadır. Dolayısıyla belirli bir duruma göre yapay zeka sistemleri sorunu çözmek için görev yapmakta ve buna tepki vermektedir. İdealist olarak yaklaşıldığında tamamen insana özgü,hissetme ,davranışları öngörme ,karar verme gibi şeyleri gerçekleştirebilen yapay zeka ürünleri, genel olarak robot adıyla adlandırılır.\n. Peki gelecekte böyle bir varlık insanoğlunu yok edebilir mi ? Bakalım gelecekte neler olacak. Elimizde bununla ilgili sadece birkaç teori var. Kimileri için bazı kurgu filmlerindeki gibi insanları kontrol eden robotların ortaya çıkması ihtimali varken,kimileri içinse robotların gelecekte insanlara hizmet etmesi ya da zor işleri gerçekleştirebilmesi durumları söz konusu. Gelecekte her ne olursa olsun yapay zeka günümüzde o kadar çok sektörün işini kolaylaştırıyor ki . Tarım ,sanayi,sağlık, medya,yazılım geliştirme, teknoloji, çağrı merkezleri, eğitim,otomotiv... Daha saymakla bitmez. Peki gelelim merak edilen şu soruya.\n. Belki de bizim sonumuzu getirecek olan bu yapay zekayı neden yapıyoruz? Bu teknolojiyi yapma amacımız insanın evreni ve doğayı anlama çabasında kendisine yardımcı olabilecek, belki de kendisinden daha zeki, insan ötesi varlıklar meydana getirme düşünün ürünüdür. Peki biz bizden daha zeki bir varlık yapabilir miyiz?? Kulağa pek de mantıklı gelmiyor sanki. Sizce??"""},
"5G-yeni_iletişim_ağı":{"foto":"AgADBAADc7QxG3gLqFHms0u4IpWHaCureiNdAAMBAAMCAAN5AAMDQAEAARYE", "yazı":"""5G Teknolojisi Nedir?\n5G, şuanda kullandığımız 4G LTE ağlarının büyük bir evrimidir. Bildiğiniz üzere son yıllarda büyük veriler ve nesnelerin interneti gibi yenilikler teknolojiyle birlikte ortaya çıkmakta. Bunların gereği olarak da 5G teknolojisi doğmaktadır. 5G'nin asıl amacı çok daha hızlı internet sağlamak ve kesintisiz bağlantı kurmaktır. - Eminim siz de internet dolayısıyla bağlantı sıkıntısı yaşamışsınızdır-. Ayrıca bahsetmiş olduğumuz bu çılgın 5G teknolojisinin bir önemli özelliği ise çok geniş kapsamlı olması. Yazımızın ilerleyen bölümlerinde bu kapsama alanından bahsedeceğim.\nÇalışma prensibi: Temel çalışma prensibi diğer ağlardaki gibi radyo dalgaları ile veri dağıtımı şeklinde. Ancak 5G teknolojisinde 4G'de kullanılan LTE yerine OFDM adında yeni bir şifreleme kullanılacak.\n5G Teknolojisi'nin yararları ve kullanım alanları: Malum teknoloji dünyada çok gelişti ve birçok şeyi değiştirdi. Yeni 5G teknolojisi ile de birçok şeyin değişeceği düşünülüyor. Örnek verecek olursak, 5G vericilerinin çok küçük olması nedeniyle şehirlerdeki baz istasyonları yerine küçük modeme benzer cihazlar kullanılması ön görülüyor. Kullanım alanlarına gelirsek, 5G sadece hızlı veri alıp vermeye yaramayacak. Hayatımızın nerdeyse her alanında etkili olacak ve otomasyon gibi birçok alanın gelişmesinde çok etkili olacaktır. Tahmin edebileceğiniz üzere evlerde ve ofislerde olacak 5G ve Wİ-Fİ ile bi' rekabet oluşturacak. Bunun dışında şu anda dünyada birçok iş geliştirme merkezlerinde sağlık alanında deneme amaçlı kullanılmaktadır. Mesela kuvözdeki bir bebekten daha çok veri almaya çalışılmakta, felçli kişilerin rehabilitasyonu gibi alanlarda kullanımı gibi...\nBunun dışında, otonom sürüşte de etkisi olacaktır. Biliyorsunuzdur ki Tesla gibi araçlarda otonom sürüş desteği var. Böylece araç kendi ilerleyebilmektedir. Ancak 5G teknolojisi, diğer araçlar ile iletişim halinde olacak yani daha güvenli ve sağlıklı bir trafik sağlanacaktır.\n. Bugünlük yazımız burda bitiyor. Okuduğunuz için teşekkür ediyor, bir başka yazıda görüşmeyi umuyoruz."""},
"ses_dalgalarının_yayılımı":{"foto":"AgADBAADdbQxG3gLqFGN1XG0WvUMfHiqeiNdAAMBAAMCAAN5AAPQOwEAARYE", "yazı":"""Ses dalgası nedir?🔊\nSes dalgaları uzunlamasına yayılan dalgalardır. Gittikleri yöne doğru titreşirler ve bir engele çarptıklarında geri sekerler. Biz buna “ses yankısı” diyoruz. Ses dalgasının şeklini osiloskop ile görebiliriz. Dalganın şekli üretilen sesin çeşidi hakkında birçok ipucu içerir.\nSes dalgalarının frekansı hertz (hz) cinsinden ölçülür. İnsanlar sadece 20 ile 20.000 hz arası sesleri duyabilir. Daha yüksek frekansları kulağımız algılayamaz. Ultrason adı verilen bu yüksek frekanslı sesler bazı hayvanlar tarafından duyulabilir, ayrıca Tıp alanında da kullanılırlar. Ultrason dalgaları birbirinden farklı yoğunluktaki iki nesne arasındaki sınıra geldiğinde bir kısmı geri yansır. Dalgaların yansıması için geçen zamanı ölçerek bu aradaki mesafenin ne kadar olduğu hesaplanabilir. Rahimdeki bebeklerin ultrason görüntüleri bu teknikle elde ediliyor.👶 Hava, sıvı veya katı nesnelerin içinde titreşerek ilerleyen ses dalgaları beynimiz tarafından elektrik sinyallerine dönüştürülür. Ses dalgasının şekli sesin yüksekliğini ve inceliğini belirler.\nBir ses dalgasının hızı içinden geçtiği ortama bağlıdır. Havada saniyede yaklaşık 340 metre hızla ilerler. Sudaki hızı bunun 4 katıdır. Bazı katı maddelerde ise bundan da hızlı yol alır. Yine de ışık kadar hızlı değildir. Işık havada saniyede 300.000.000 metre hızla ilerler. Bu yüzden uzaklardaki bir sesin kaynağını önce görür. Sesin daha sonra işitirsiniz. Bir nesne ses hızından daha hızlı hareket ederse, çıkardığı ses dalgalarını tek bir şok dalgası halinde kaynaşmaya zorlar. Buna sonik patlama denir. Ses hızından hızlı giden uçakların çıkardığı sesler, balon patlaması veya kamçı şaklaması sonik patlamaya örnektir. ✈️\nSes dalgalarının özelliklerine gelirsek;\n-Ses dalgasındaki iki eş nokta arasındaki mesafeye “Dalga Boyu” deriz. -Ses dalgasının maksimum yüksekliğe çıktığı zamana “genlik” deriz.\n-Saniyede üretilen ses dalgası sayısına “Frekans” deriz. -Dalga boyu be kadar kısaysa sesin frekansı o kadar yüksektir ve ses o kadar incedir. Biz buna “incelik” diyoruz.\n-Ses dalgasının genliği ne kadar fazlaysa, ses o kadar yüksek duyulur. Buna da “yükseklik” denir."""},
"ses_dalgası_ile_görüntü_elde_etme":{"foto":"AgADBAADdrQxG3gLqFEPjGmqI7EnaVaoAyNdAAMBAAMCAAN5AANHYwEAARYE", "yazı":"""Büyük Okyanus, Hint Okyanusu, Atlas Okyanusu, Akdeniz, Karadeniz ve daha pek çokları... 🌊 Gezegenimizin büyük bir bölümü denizlerle kaplı. Bu denizlerin ortalama derinliği 3700 metre ⬇️ Bazı bölgelerde ise bu derinlik 11 kilometreye kadar yaklaşıyor. Peki bu okyanuslar ve denizler nasıl keşfediliyor dersiniz?\nSonar "Sound Navigation and Ranging" ifadesinin kısaltılmışı olan,ses dalgalarıyla bir cismin uzaklığını boyutunu ve diğer verileri hakkında bilgi almak için kullanılan aletin adıdır. Sonar sistem ilk olarak denizaltı için üretilmiştir⚓️. Ses dalgalarının su altında yayılma özelliğinden faydalanarak, su altında/su üstünde gezmeyi, mesafe aralığı hesaplamayı, haberleşmeyi ve diğer cisimler hakkında bilgi edinmeyi sağlayan bir tekniktir. Sonarı, yunuslar iletişim için ; yarasalar ise yön bulmada kullanır. Sonar sistem aktif ve pasif olmak üzere ikiye ayrılır: Pasif sonar,gemiler tarafından yapılan sesi dinlemektedir; Aktif sonar atış sesleri yayar ve yankıları dinler. Peki sonarlar nasıl çalışır? Bir sonar cihazı sudan aşağıya doğru ses dalgaları gönderi ⬇️ Bu ses dalgaları balık, bitki örtüsü veya zemindeki nesnelere çarptığında yüzeye geri yansır. Sonar cihazı ses dalgalarının aşağı inmesi, bir nesneye vurması ve sonra geri dönmesiyle ne kadar sürede bunun gerçekleştiğini hesaplar. Yarasalar ve yunusların kullandığı ekolasyon özelliklerine benzerdir. Bu ölçülen süre cihazın yansıttığı nesnenin derinliğinin ölçümünü sağlar. Ayrıca geri dönen titreşimin gücünü ölçer. Nesnelerin boyutu, yapısı ne kadar sert ise geri dönüş titreşim darbesi de o kadar güçlü olur. Sonarlar cismin derinliğini, sertliğini belirleyebiliyor. Peki cismin şeklini de belirleyebiliyor mu? Tabii ki de evet. Geri dönen bir titreşim algılandığında, bir diğeri gönderilir. Ses dalgaları suda 1 mil hızla hareket edebildiğinden, sonarlar saniyede birden fazla titreşim gönderebilir. Geri dönen ses titreşimleri elektrik sinyaline dönüştürülür ve daha sonra görüntülenir⚡️Böylelikle dip derinliğini, yapısını ve nesneleri görüntülemiş oluruz."""},
"dünyaya_benzeyen_gezegenler":{"foto":"AgADBAADd7QxG3gLqFEeouCo0qxSKYd0PCRdAAMBAAMCAAN5AANxZgACFgQ", "yazı":"""Selamlar 👋🏻, bugün size Dünya’mıza fazlasıyla benzeyen bazı gezegenleri ve başka bir gezegende yaşanma olasılıklarını anlatacağım. 🌏Yakın tarihte sürekli gündemde olan bir konu Dünya’dan başka bir gezegende yaşamak. Peki neden yaşayamıyoruz? 🤔\nAslında bunun birçok nedeni var ve başlıca nedenlerinden biri de yeterli araştırma teknolojimizin olmaması🚀. Bir diğer nedense: Çoğu gezegende oksijen problemi olması ve bazı gezegenlerde oksijen olsa bile yüzeyleri tamamen okyanus, buzul gibi oluşumlarla kaplanmış halde olduğundan dolayı - tıpkı Dünya’nın ilk evrelerinde olduğu gibi- bu tip gezegenlerde yaşamak imkansız hale geliyor.\nŞimdi size Dünya’mıza benzeyen 2 gezegenden bahsedeceğim ;\n1-)Kepler-186f\nYana kaydırdığımızda gördüğümüz ilk resimdeki bu gezegen çoğu astronom için dönüm noktası niteliği taşır. 2014’te keşfedilmiştir. Dünya’ya en çok benzeyen gezegendir ve 500 ışık yılı uzağımızda bulunur. 💫Gezegende 1 yıl 130 Dünya gününe tekabül eder ve gezegenin çapı Dünya’nınkinin 1.1 katıdır. Gezegende yaşayamamızın sebebi ise atmosferinde oluşan bazı sorunlardır.\n2-)Kepler-22b\nGüneş sistemi dışında bulunan ve yaşam için uygun gezegensel konuma sahip ilk gezegendir kendisi. Gezegenin yıldızı Güneş’e çok benzer ve yörüngesi de neredeyse Dünya’nınkiyle aynıdır. 1 yıl 290 Dünya gününe tekabül eder. Dünya’dan 2.4 kat büyüktür. Aslında kocaman bir Dünya hayal etmek oldukça keyifli gibi fakat bilim insanları bu kadar büyük olmasından dolayı gezegenin okyanuslarla kaplı olabileceğinden korkuyor 🌊. Ve bizden 600 ışık yılı uzakta olduğu için daha önce bahsettiğim teknolojik nedenlerden dolayı şu anda detaylı araştırma yapmak pek de mümkün değil gibi görünüyor.. Ama kim bilir belki gelecek sürprizlerle doludur ⚡️\nBir dahaki yazımda görüşmek üzere , sağlıcakla kalın 🤙🏻."""},
"yapay_genel_zeka":{"foto":"AgADBAADeLQxG3gLqFHUHyWihqfI-76ItxsABAEAAwIAA3kAA1B6BgABFgQ", "yazı":"""Yapay genel zeka(AGI), bir insanın yapabileceği herhangi bir zihinsel görevi başarıyla gerçekleştirebilecek bir makinenin zekasıdır. Bilimkurgu ve fütürolojide de ortak bir konu olan AGI şu anda üzerinde çalışılan bazı yapay zeka araştırmalarının amacıdır. 🤖🧠Peki gelecekte gündemi fazlaca meşgul edeceğini düşündüğüm AGI'nin diğer yapay zekalardan farkı nedir?\nAraştırmacıların belirlediği kriterler: planlama, doğal dilde iletişim kurma, nesneleri taşıma ve kullanma, tehlikeyi tespit ve müdahale etme, strateji belirleme, belirsizlik anında karar verme, otonomi, hayal kurma olarak sayılabilir. Yani anladığım kadarıyla duygular dışında (hatta hayal kurma bu kısma biraz girse de) insanî özelliklerin AGI'de toplanması amaçlanıyor.\nPek çok insan gelecekte yapay zekaların başımıza bela açacağını düşünüyor. Bana soracak olursanız yapay zekalar hiçbir zaman duygulara, inançlara dolayısıyla ahlâki değerlere sahip olamayacak. Yani bu projenin duygusal kısmı hiç gerçekleşemeyecek. Belki de insanları korkutan şey duyguları olmayan bir şeyin bize bir hayli zarar verebileceği düşüncesidir. Ama biz sezgilerimiz, hislerimiz, ruhumuz ve sanatımız olduğu için onlardan her daim farklı olacağız. Bu yüzden insanlığa zarar verecek olsalar bile hiçbir zaman topyekün bir yıkım olacağını düşünmüyorum.\nPeki ya sizin bu hakkındaki düşünceleriniz neler?"""},
"LIBRA-Facebook'un_kripto_parası":{"foto":"AgADBAADebQxG3gLqFFQnZCzXj8mOucgAiNdAAMBAAMCAAN5AAMhyAEAARYE", "yazı":"""Bugün son zamanlarda adını çok duymaya başladığımız kripto paraları ve Facebook'un bu yıl kullanıma açmayı planladığı sanal parası Libra'yı tanıyacağız. Facebook Haziran 2019'da uzun zamandır planladığı sanal parası Libra'yı duyurdu Peki Libra nedir, Facebook neden kendi parasını çıkarıyor?🤔 Libra Bitcoin, gibi bir kripto para, aralarındaki temel fark şu Bitcoin'i kimin oluşturduğu bilinmiyor ama Libra doğrudan Facebook tarafından oluşturulan ve başta facebook uygulamaları üzerinden olmak üzere uluslararası, her hangi bir komisyon almadan ve güvenilir şekilde para transferi yapmayı amaçlayan bir sanal döviz. Ayrıca Libra ile Spotify, Uber gibi sanal ödemeler de yapılacak. Son yıllarda adı her türlü skandalla anılmış Facebook gibi güven oranı oldukça düşük bir şirketten bunları duymak gerçekten ilginç. Artık Libra'nın ne olduğunu biliyoruz. Peki sizce Facebook sadece güvenilir para transferi yapmak için mi bir para çıkarıyor? Tarihte de örneğini defalarca gördüğümüz gibi devletlerin kendi paralarına sahip olması bağımsızlık semboldür. Peki artık devir değişti,devletler yerine şirketler bağımsızlıklarını ilan edip, hiçbir kanuna ve ahlaki değere bağlı kalmadan kendi imparatorluklarını kuracaklar dersem ne düşünürsünüz ?Facebook dünya çapında 2.7 Milyar kullanıcıya sahip. Bu sayı herhangi bir din veya devletle karşılaştırılamayacak düzeyde !Libra'nın ilk tanıtımında bu paranın Amerikan hükümetine bağlı olmadığını ve bu parayı kontrol edecek, kararlar alacak, İsviçre Cenevre'de bir birlik kurulduğunu açıkladı. Libra Association adı verilen, bu her şeyden bağımsız derneğe, 10 Milyon dolar ücret ödeyerek dahil olabiliyorsunuz ve Libra hakkında alınacak kararlarda oy hakkına sahip oluyorsunuz.\nFacebook tanıtımdan sonra Amerika'da beklemediği kadar çok eleştiri aldı ve Mark Zuckerberg bu kripto paranın Amerika'nın dünya ekonomisinde ağırlığını sürdürmek için kritik bir etken olabileceğini söyledi. Sanırım eleştirilerden dolayı biraz geri adım attı diyebiliriz😅\nLibra'nın 2020 yılı içerisinde kullanıma girmesi bekleniyordu ancak Covid-19 sonrası tüm şirketler gibi Facebook'ta planlarını değiştirecekir.\nPeki siz bu olay hakkında ne düşünüyorsunuz?"""},
"yazılım_öğrenmek_istiyorum":{"yazı":"""Yazılım öğrenmek istiyorum\nÖncelikle şuradan başlıyım. Bazı insanları görüyorum kod yazmayı kısa surede öğreneceklerini zannediyorlar. İlk html ile başlarım sonra css, javascript, php, python falan derken ilerler giderim. Nasıl kulağa hoş geliyor değil mi? Bu dilleri kısa surede öğrenebilmek. Ama yok öyle dünya. İsterseniz internette programlama dillerinin ne kadar kütüphaneye sahip olduğuna bir bakin derim. Bu dillerin hepsini aynı anda öğrenmeniz mümkün değil. Sizin moralinizi bozmak istemem fakat bir dilde uzmanlaşmanın basit olmadığını anlayın. Öğrenmek istiyorsanız zamanınızı harcayacaksınız. Gün gelecek bir hata için saatlerce düşüneceksiniz. Şu hatayı çözünce yatacağım deyip geceleri uykusuz da kalacaksınız belki. Belki de ufak bir hata için saatlerinizi harcayıp çözünce sevinmek yerine hayal kırıklığına uğrayacaksınız. Kendinizi bir ise yaramaz hissedeceksiniz. Ama sunu bilin ki asla pes etmezseniz kazanan hep siz olacaksınız. Kimse kolay olacağını söylemedi. Birazda öğrenme aşamasında ne yapmanız gerekir ondan bahsedeyim. Öğrenirken uygulamalı öğrenin. Nasıl yapıldığını okuyun ve yapmaya çalışın, işin mantığını kavrayın, algoritmayı anlamaya çalışın. Sürekli kod yazın, alıştırma yapın, kendi projelerinizi üretin. Ve asla şunu yapmayın, kopyala-yapıştır. Bu size sadece küçük projeleri yapmış gibi gösterir. İşin mantığını kavratmaz. Her alanda iyi olacağım diye çalışmayın. İlk önce bir dilde uzmanlaşın, sonra diğer dilleri öğrenin. Emin olun bir dili çok iyi öğrenirseniz diğer dilleri öğrenirken hiçbir sorun yaşamazsınız. Çünkü algoritma mantığı her dilde aynıdır, sadece fonksiyon isimleri değişir. Şunu da aklınızdan çıkarmayın. Kimse size her şeyi öğretmeyecek. Bazı şeyleri kendiniz öğrenmek zorundasınız. Araştırmayı hatalara çözüm bulmayı bir program yazarken o algoritmayı kurmayı bunları kendiniz öğrenmek zorundasınız. Çünkü o öğrendiğiniz kişi her zaman sizin hatalarınızı çözmeyecek. Bunu siz yapacaksınız. İnternette de bir sorunu hemen çözmeyi beklemeyin. Araştıracaksınız her sayfadan bir bilgi öğreneceksiniz. Ama şunu unutmayın, bir bilgiyi size sizden başkası öğretemez."""},
"genel_görelilik":{"foto":"AgADBAADirQxG3gLqFFalXrLOkSHmjZRlyJdAAMBAAMCAAN5AANLLQMAARYE", "yazı":"""Görelilik kuramı 1/2\nEinstein ilk olarak 1905'te "bilim yasalarının her gözlemci için aynı olması gerektiği" fikrini öne sürdü. Bu basit fikrin muhteşem sonuçları arasında meşhur E = mc² (E enerji, m kütle ve c ışık hızı) denkleminde kütle ile enerjinin denkliği dolayısıyla hiçbir şeyin ışık hızından daha hızlı olamayacağı teorisi de vardır. Nasıl mı? Kütle ve enerji denkliğiyle bir cisim hareket ettikçe enerjisi kütlesine eklenir. Yani cisim zaman geçtikçe hızlanmakta zorlanır. Cisim ışık hızına yaklaştıkça kütlesine eklenen enerji de katlanarak artacağından bu döngü böyle gider ve bir süre sonra cismin sonsuz enerji üretmesi mümkün olamayacağından hiçbir cisim ışık hızından daha hızlı hareket edemez. Göreliliğin bir başka sonucu ise şöyledir: Uzayda farklı gözlemciler bulunduğunu düşünelim. Bir noktadan ışık sinyali gönderdiğimizde gözlemciler uzay mutlak olmadığı için ışığın ne kadar yol aldığı konusunda ortak bir yargıya varamazlar. Ama fiziksel yasaların kesinliği sebebiyle gözlemciler ışığın hızı konusunda kesin bir tutumda olacaklar. Işığın katettiği mesafenin geçen zaman çarpı ışık hızı olduğu düşünülürse gözlemciler zaman konusunda da ortak bir noktada buluşamayacaklar. Yani görelilik kuramı mutlak zaman fikrini ortadan kaldırır!. Özel görelilik denen bu teoride bir eksik vardı. Bu kuram Newton'un kütleçekim yasasına uymuyordu. Çünkü kütleçekime göre aralarında çekim kuvveti olan iki nesneden biri hareket ettirildiğinde diğer nesnenin sonsuz hızda hareket etmesi gerekiyordu. Oysaki özel göreliliğe göre bu mümkün değildi. Einstein yıllarca bu uyumsuzluk üzerine çalıştı. Nihayet 1915'te genel görelilik kuramını ortaya koydu: Uzayzaman içerisindeki kütle ve enerji dağıtıldığı için bükülmüştür. Yani Dünya gibi cisimler esasında kütleçekim sebebiyle eğik bir yörüngede değil, eğik bir uzayda düz yola en yakın şeyi -jeodeziği- takip ederler. Bu kurama göre cisimler dört boyutlu uzayda -uzayzaman- düz çizgileri takip etseler de bu bizlere üç boyutlu uzayımızda eğik görünür. Buna benzer bir durum dağlık alanda uçağın izlenmesinde görülebilir. Uçak düz bir çizgiyi takip etse de biz yerdeki gölgesini eğik görürüz.""", "yazı1":"""Görelilik kuramı 2/2\nÖnceki gönderide bahsettiğim uzayzamanım bükülmesi durumu elbette ışık için de geçerli. Işık ışınları da uzayda jeodezikleri takip ederler. Dolayısıyla genel görelilik ışığın kütleçekimsel alanlar tarafından bükülmesi gerektiğini öngörür. Bu durumu gözlemlemek için yapılan çalışma Güneş'in yakınından geçen bir yıldızın dünya üzerindeki birine küçük bir sapma sebebiyle farklı görünmesini konu alır. Elbette bu gözlemi yapabilmemiz için Dünya'nın hareket hâlinde olması -yıldızın farklı konumlardaki görünümünü gözlemlemek için- ve Güneş'ten gelen ışığın bir tutulmayla engellenmesi -yıldızı gözlemlemek için- gerekir.\nGelelim meşhur zaman kaymasına. Genel göreliliğe göre zamanın dünya gibi çok büyük cisimlerin yakınında yavaşlıyor olması gerektiğiydi. Bunun sebebi ışığın enerjisi ile frekansı arasında bir ilişki olmasıdır: enerji büyükse frekans da büyüktür. Işık dünyanın merkezinden yukarıya doğru hareket ettikçe enerjisini kaybeder dolayısıyla frekansı da azalır. Frekansın azalması iki dalga tepesi arasındaki zamanın uzunluğunun artacağı anlamına gelir. Yani yukarıda bulunan biri için zaman daha hızlı geçer diyebiliriz. Bu durum 1962'de bir su kulesinin tepesinde ve tabanında bulunun iki saat aracılığıyla test edildi. Sonuç görelilikle tam uygunluk gösterdi. Bu öngörünün günlük hayattaki etkisine bakacak olursak günümüzde uydulardan gelen sinyallerle çalışan navigasyon sistemlerini örnek verebiliriz. Zira bu öngörü ihmal edilirse navigasyonla ölçülen konum kilometrelerce farkla yanlış olabilecektir. Tabii bir de klasik ikizler paradoksu var: ikizlerden biri uzaya gider diğeriyse dünyada kalır. Uzaydaki kardeş geri döndüğünde kardeşinin kendisinden daha yaşlı olduğunu görür. Ancak söz konusu olay zamanın mutlak olmadığını düşündüğümüzde paradoks niteliği taşımaz. Çünkü göreliliğe göre zaman mutlak değildir yani ortam ve harekete göre değişkenlik gösterebilir. Zamanın göreliliğini düşününce aklıma ilk olarak gördüğümüz rüyalar geldi. Dakikalarca anlattığımız ve çok uzun sürdüğünü sandığımız rüyalar yalnızca birkaç saniye sürer. Zamanın göreliliği sizce bu gibi durumlarda da etkin midir?"""},
"kuantum_bilgisayar":{"foto":"AgADBAAD6rIxG55lsFFJeEqSHmMxLAO4fSNdAAMBAAMCAAN5AAPrRAEAARYE", "yazı":"""Bugünkü yazımız kendilerine henüz uygun sıfatı bulamadığım kuantum bilgisayarlar hakkında. Bizler 1953 yılında tanıtılan ilk bilgisayardan bu yana her zaman bilgisayarların donanımlarını küçültmeye ve hızlandırmaya çalıştık. günümüz teknolojisinin sınırlarını zorlayan ve şu anda sahip olduğumuz en üst düzey süper bilgisayarlara ulaştk. Ama hala hayal edebileceğimiz çok daha hızlı sistemler var. İşte kuantum bilgisayarlar burda bizi karşılıyor. Kuantum bilgisayarların çalışma mantığı kuantum fiziğine dayanır. Şu anda kullandığımız ve biraz daha kullanmaya devam edeceğimiz bilgisayarlar 0 ve 1 şifreleme mantığıyla çalışırlar. Bilgisayarlarımızdaki her devre 0 ise elektrik yok,1 ise elektrik var yani açık ve kapalı olarak çalışır ve bu şekide devrelerde depo edilir. Bu sistemde depo edilen her bir veriye bit diyoruz. Kuantum bilgisayarlarda ise Qubitler vardır ve bunlar aynı anda hem 0 hem 1 değerine sahip olabilir. Bu da demek oluyor ki bu yaratıklar aynı anda 2 veriyi birden işleyebiliyorlar. Ee peki bizene bundan? Elimizde 0 ve 1 iki bit olduğunu düşünelim. Bu iki bit 0 ve 1 olmak üzere 2 kombinasyona sahip olabilir. Ama Kuantum bilgisayarların taşıdığı 2 Qubit veri. 2 üzeri 2 şeklinde 11 00 10 01 olmak üzere 4 farklı kombinasyona sahip olabilir. Ve bu güç inanılmaz şekilde katlanarak artar. O zaman hemen kuantum bilgisayarlara geçelim derseniz eğer, maalesef bu hemen mümkün olmayacak çünkü bu sistemlerde verileri depolamak çok zor. Yani bir bilgiyi sabit şekilde elde tutamıyoruz. Ama yine de gelecekte bunu başaracağız. Bilimsel olarak imkansız değil.Tekrar güç ve hız konusuna gelirsek;\nSizlere bu sistemlerin gücünü anlatan ufak bir örnek vereyim. Google kuantum bilgisayarlar hakkında derin araştırmalar ve yatırımlar yapmış 2014'te Kaliforniya Santa Barbara'da kuantum bilgisayar alanında çalışacak bir takım ve laboratuvar kurmuştur. Dile kolay yaklaşık 5 yıllık devrim niteliğindeki çalışmaların sonunda; hazır olun! Günümüzdeki o dev şirketlerin,devletlerin kullandığı, milyonlarca dolarlık süper bilgisayarlarda 10.000 yılda işlenip hesaplanacak verinin, bir Kuantım bilgisayar ile 3 dakika 20 saniyede hesaplanabileceğine ulaşmıştır. Bu korkunç hızlı sistem şifreleme mantığını tamamıyla değiştirecek ve bizleri bambaşka dünyalara götürecektir. Bu sistemler yalnızca çok hızlı bilgisayarlar değil, bilime dair bambaşka kapılar açacak ve evrene dair çılgın sorularımızı cevaplamaya imkan sağlayacaktır. Elimizden geldiğinde bu çılgın sistemleri anlatmaya çalıştık. Ama kolay bir şekilde anlatmak oldukça güç.\nOkuduğunuz için teşekkürler."""},
"block_chain":{"foto":"AgADBAAD67IxG55lsFHVwbhKEj3bULRAfyNdAAMBAAMCAAN5AAPIQwEAARYE", "yazı":"""Merhabalar bugünkü yazımız geleceğimizin temellerini oluşturacak #Blockchain yani blok zinciri teknolojisi hakkında. Blok zinciri aslında verilerin %100 güvenlikle şifrelendiği ve kayıtların birbirine bağlanmasıyla oluşturduğu sonsuz zincirin ismidir ama sadece verilerin depolandığı ya da alışıldık şekilde şifrelendiği bir sistem olarak düşünemeyiz. Blok zinciri teknolojisi şu an da kullandığımız tek merkezli veri sistemlerinin aksine tek bir merkeze bağlı olmadan çalışan bir sistemdir. Peki bu nasıl oluyor? Blok zinciri sisteminde veriler tek bir merkezde depolanmak yerine önceki kayıtlarla zincir ekleme mantığıyla birbirlerine bağlanıyor ve dünyanın her yerinden çeşitli merkezlerde kayıt altına alınıyor. Böylece sisteme bir kez kaydedilmiş bir veri yani zincire eklenen  kayıt bir daha değiştirilemiyor çünkü aynı anda dünyadaki pek çok merkezde kayıt altına alınmış oluyor. Peki bu deftere yazılan işlemleri nasıl gerçekleştireceğiz? Çok basit bir örnekle, bu sistemle birisine para göndermek istediğinizde karşı tarafla aranızda hiç bir aracı olmadan işleminizi gerçekleştiriyorsunuz. Öncelikle 256 hanelik kullanıcı adı mantığında bir anahtarınız oluyor ve bu, işlemin kim tarafından kime gerçekleştirildiğini belirliyor, bir de sizin işlemi onaylamak için kullanacağınız 256 hanelik bir kişisel hesap şifreniz var. Bunların eşleşmesi durumunda dünyanın her yerinde arada hiç bir aracı olmadan karşı tarafa istediğiniz her şeyi %100 güvenli şekilde gönderebilirsiniz. Evet bugün belki de bankaların sonunu getirecek, gelecekte online seçimler yapmamızı sağlayacak, her sektöre damga vuracak bu sistemi kısaca anlattık.\nHoşça kalın veriyle kalın"""}
}

#"":{"foto":"", "yazı":""""""},
#@Client.on_message(Filters.photo)
# def photo(client, message):
#    message.reply(message.photo.file_id)

@ICOB_BOT.on_message(Filters.command(["notlar"], case_sensitive=True))
def notlar(client, message):
    mesaj = "🤖 **Bende olan notlar ** ;\n\n"
    for i,x in not_bilgi.items():
        mesaj += f" 👉  `{i}`\n"
    mesaj += """\nNotları şu şekilde çağırınız : "**/not not_adı**" """
    message.reply(mesaj)


@ICOB_BOT.on_message(Filters.command(["not"], case_sensitive=True))
def not_cagir(client, message):
    text = message.text
    if len(text.split()) == 1:
        message.reply("Lütfen bir not ismi giriniz. Notlara ulaşmak için : **/notlar**")
    elif len(text.split()) == 2:
        if text.split()[1] in not_bilgi:
            try:client.send_photo(message.chat.id, not_bilgi[text.split()[1]]["foto"])
            except KeyError:pass
            try:client.send_message(message.chat.id, not_bilgi[text.split()[1]]["yazı"])
            except KeyError:pass
            try:client.send_message(message.chat.id, not_bilgi[text.split()[1]]["yazı1"])
            except KeyError:pass
        else:
            message.reply("Not bulunamadı. Notlara ulaşmak için : **/notlar**")

    else:message.reply("""Lütfen komutu "**__/not not_adı__**" şeklinde giriniz.\nNotlara ulaşmak için : **/notlar** """)

#############################

from datetime import datetime

from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup, errors
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

@ICOB_BOT.on_message(Filters.command(["ban", "ban@icob_bot"]))
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
                        try:client.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, 0)
                        except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini banlayabilmem için ütfen beni yönetici yapın");quit()
                        if message.reply_to_message.from_user.username:
                            message.reply(f"@{message.reply_to_message.from_user.username}[`{message.reply_to_message.from_user.id}`] banlandı.", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
                        else:
                            message.reply(f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})[{message.reply_to_message.from_user.id}] banlandı", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
                    elif len(sure) > 2:
                        message.reply("""Lütfen komutu "**__/ban 5dk/1gün/10saat__**" şeklinde giriniz. """) 
                    else:
                        if zaman(sure[1]) == "hata":
                            message.reply("""Lütfen komutu "**__/ban 5dk/1gün/10saat__**" şeklinde giriniz. """) 
                        else:
                            try:client.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, int(time.time() + zaman(sure[1])))
                            except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini banlayabilmem için ütfen beni yönetici yapın");quit()
                            if message.reply_to_message.from_user.username:
                                message.reply(f"@{message.reply_to_message.from_user.username}[`{message.reply_to_message.from_user.id}`] {sure[1]} süreyle banlandı.", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
                            else:
                                message.reply(f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})[`{message.reply_to_message.from_user.id}`] {zaman(sure[1])} süreyle banlandı", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
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
                        try:client.kick_chat_member(message.chat.id, mesaj1[1])
                        except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini banlayabilmem için ütfen beni yönetici yapın");quit()
                        message.reply(f"""{mesaj1[1]}[`{client.get_chat_member(message.chat.id, mesaj1[1])["user"]["id"]}`] banlandı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
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
                                try:client.kick_chat_member(message.chat.id, mesaj1[1], int(time.time() + zaman(mesaj1[2])))
                                except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini banlayabilmem için ütfen beni yönetici yapın");quit()
                                message.reply(f"""{mesaj1[1]}[`{client.get_chat_member(message.chat.id, mesaj1[1])["user"]["id"]}`] isimli kullanıcı {mesaj1[2]} süreyle banlandı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
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
                                try:client.kick_chat_member(message.chat.id, mesaj1[2], int(time.time() + zaman(mesaj1[1])))
                                except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini banlayabilmem için ütfen beni yönetici yapın");quit()
                                message.reply(f"""{mesaj1[2]}[`{client.get_chat_member(message.chat.id, mesaj1[1])["user"]["id"]}`] isimli kullanıcı {mesaj1[1]} süreyle banlandı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))                    
                        #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[2])["until_date"])}__** süresine kadar banı var.""")
            else:message.reply("""Lütfen komutu "**__/ban @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")

        else:
            mesaj2 = mesaj.split()
            if len(mesaj2) == 1:
                message.reply("Lütfen /ban komutunu banlayacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")

            elif len(mesaj2) == 2:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[1])
                        except:message.reply(f"Bu grupta {mesaj2[1]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj2[1])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj2[1])["status"] not in yetkiler:
                            try:client.kick_chat_member(message.chat.id, mesaj2[1])
                            except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini banlayabilmem için ütfen beni yönetici yapın");quit()
                            if client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]:
                                message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]}[`{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}`] isimli kullanıcı banlandı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
                            else:
                                message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["first_name"]}](tg://user?id={mesaj2[1]})[`{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}`] isimli kullanıcı banlandı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
                        else:message.reply("Banlamak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[1])["until_date"])}__** süresine kadar banı var.""")
                    else:message.reply("Birini banlayabilmek için yönetici olmanız lazım.")
                #else:message.reply("Lütfen /ban komutunu banlayacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")
                

            elif len(mesaj2) == 3:
                if zaman(mesaj2[1]) == "hata" and zaman(mesaj2[2]) != "hata":
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[1])
                        except:message.reply(f"Bu grupta {mesaj2[1]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj2[1])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj2[1])["status"] not in yetkiler:
                            try:client.kick_chat_member(message.chat.id, mesaj2[1], int(time.time() + zaman(mesaj2[2])))
                            except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini banlayabilmem için ütfen beni yönetici yapın");quit()
                            if client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]:
                                message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]}[`{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}`] isimli kullanıcı {mesaj2[2]} süreyle banlandı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
                            else:
                                message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["first_name"]}](tg://user?id={mesaj2[1]})[`{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}`] isimli kullanıcı banlandı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
                        else:message.reply("Banlamak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[1])["until_date"])}__** süresine kadar banı var.""")
                    else:message.reply("Birini banlayabilmek için yönetici olmanız lazım.")

                elif zaman(mesaj2[2]) == "hata" and zaman(mesaj2[1]) != "hata":
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[2])
                        except:message.reply(f"Bu grupta {mesaj2[2]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj2[2])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj2[2])["status"] not in yetkiler:
                            try:client.kick_chat_member(message.chat.id, mesaj2[2], int(time.time() + zaman(mesaj2[1])))
                            except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini banlayabilmem için ütfen beni yönetici yapın");quit()
                            if client.get_chat_member(message.chat.id, mesaj2[2])["user"]["username"]:
                                message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["username"]}[`{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["id"]}`] isimli kullanıcı {mesaj2[2]} banlandı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
                            else:
                                message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["first_name"]}](tg://user?id={mesaj2[2]})[`{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["id"]}`] isimli kullanıcı banlandı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Banı kaldırmak için Tıkla", callback_data=b"ban_kalk")]
                                ]))
                        else:message.reply("Banlamak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Banlamak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[2])["until_date"])}__** süresine kadar banı var.""")
                    else:message.reply("Birini banlayabilmek için yönetici olmanız lazım.")

                else:
                    message.reply("Lütfen /ban komutunu banlayacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")

    else:message.reply("Burası bir özel sohbet. Özel sohbette seni banlayamam.")



@ICOB_BOT.on_callback_query(Filters.callback_data("ban_kalk"))
def ban_kalk(client, cq):
    yetkiler = ("creator", "administrator")
    b = cq.message.text; b = b.replace("[", " "); b = b.replace("]", " "); b = b.split()[1]
    try:client.get_chat_member(cq.message.chat.id, b)
    except:cq.answer("Kullanıcı gruptan çıkmış. 🤗", show_alert=True);quit()
    if client.get_chat_member(cq.message.chat.id, cq.from_user.id)["status"] in yetkiler:
        if client.get_chat_member(cq.message.chat.id, b)["until_date"]:
            try:
                client.unban_chat_member(cq.message.chat.id, b)
                client.edit_message_text(cq.message.chat.id, cq.message.message_id, f"{cq.message.text}\n\n**__~Kullanıcının banı kaldırdı.__**", parse_mode="Markdown")
                client.send_message(cq.message.chat.id, f"{cq.message.text.split()[0]} kullanıcının banı kaldırıldı.")
            except:cq.answer("Kullanıcının banı kaldırılamadı.", show_alert=True)
        else:cq.answer("Kullnıcının zaten banı yok. 🤗",  show_alert=True)
    else:cq.answer("Birisinin banını kaldırabilmen için 🤴Yönetici olman gerekir.",  show_alert=True)  

#############################

@ICOB_BOT.on_message(Filters.command(["unban"]))
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

#############################

from datetime import datetime
from pyrogram import Client, Filters, ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup
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

@ICOB_BOT.on_message(Filters.command(["mute", "mute@icob_bot"]))
def mute(client, message):
    mesaj = message.text
    yetkiler = ("creator", "administrator")
    if message.chat.type != "private":
        if message.reply_to_message:
            sure = message.text.split()
            if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                try:client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                except:message.reply("Maalesef yanıtladığınız mesajı atan kullanıcı grubtan çıkmış.");quit()
                #if client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["until_date"] == None:
                if client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["status"] not in yetkiler:
                    if len(sure) == 1:
                        try:client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(), 0)
                        except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini sessize alabilmem için ütfen beni yönetici yapın");quit()
                        if message.reply_to_message.from_user.username:
                            message.reply(f"@{message.reply_to_message.from_user.username}[{message.reply_to_message.from_user.id}] sessize alındı.", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                        else:
                            message.reply(f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})[{message.reply_to_message.from_user.id}] sessize alındı.", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                    elif len(sure) > 2:    
                        message.reply("""Lütfen komutu "**__/mute 5dk/1gün/10saat__**" şeklinde giriniz. """) 
                
                    else:
                        if zaman(sure[1]) == False:
                            message.reply("""Lütfen komutu "**__/mute 5dk/1gün/10saat__**" şeklinde giriniz. """) 
                        else:
                            try:client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(), int(time.time() + zaman(sure[1])))
                            except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini sessize alabilmem için ütfen beni yönetici yapın");quit()
                            if message.reply_to_message.from_user.username:
                                message.reply(f"@{message.reply_to_message.from_user.username}[{message.reply_to_message.from_user.id}] {sure[1]} süreyle sessize alındı.", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                            else:
                                message.reply(f"[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})[{message.reply_to_message.from_user.id}] {zaman(sure[1])} süreyle sessize alındı.", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                else:message.reply("Sessize almak istediğiniz kişi yönetici.")
                #else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)["until_date"])}__** süresine kadar sessizde.""")
            else:message.reply("Birisini sessize almak için yönetici olman gerekir.")
        elif "@" in mesaj:    
            mesaj1 = mesaj.split()
            if len(mesaj1) == 2:    
                if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                    try:client.get_chat_member(message.chat.id, mesaj1[1])
                    except:message.reply(f"Bu grupta {mesaj1[1]} isimli bir kullanıcı bulunamadı.");quit()
        #            if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"] == None:
                    if client.get_chat_member(message.chat.id, mesaj1[1])["status"] not in yetkiler:
                        try:client.restrict_chat_member(message.chat.id, mesaj1[1], ChatPermissions())
                        except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini sessize alabilmem için ütfen beni yönetici yapın");quit()
                        message.reply(f"""{mesaj1[1]}[{client.get_chat_member(message.chat.id, mesaj1[1])["user"]["id"]}] sessize alındı.""", reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                        ]))
                    else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                    #else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[1])["until_date"])}__** süresine kadar sessizde.""")
                else:message.reply("Birini sessize almak için yönetici olmanız lazım.")

            elif len(mesaj1) == 3:
                if "@" in mesaj1[1]:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj1[1])
                        except:message.reply(f"Bu grupta {mesaj1[1]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj1[1])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj1[1])["status"] not in yetkiler:
                            if zaman(mesaj1[2]) == False:
                                message.reply("""Lütfen komutu "**__/mute @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")
                            else:
                                try:client.restrict_chat_member(message.chat.id, mesaj1[1], ChatPermissions(), int(time.time() + zaman(mesaj1[2])))
                                except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini sessize alabilmem için ütfen beni yönetici yapın");quit()
                                message.reply(f"""{mesaj1[1]}[{client.get_chat_member(message.chat.id, mesaj1[1])["user"]["id"]}] isimli kullanıcı {mesaj1[2]} süreyle sessize alındı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                        else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[1])["until_date"])}__** süresine kadar sessizde""")
                    else:message.reply("Birini sessize almak için yönetici olmanız lazım.")
                elif "@" in mesaj1[2]:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj1[2])
                        except:message.reply(f"Bu grupta {mesaj1[2]} isimli bir kullanıcı bulunamadı.");quit()
            #            if client.get_chat_member(message.chat.id, mesaj1[2])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj1[2])["status"] not in yetkiler:
                            if zaman(mesaj1[1]) == False:
                                message.reply("""Lütfen komutu "**__/mute @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")
                            else:    
                                try:client.restrict_chat_member(message.chat.id, mesaj1[2], ChatPermissions(), int(time.time() + zaman(mesaj1[1])))
                                except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini sessize alabilmem için ütfen beni yönetici yapın");quit()
                                message.reply(f"""{mesaj1[2]}[{client.get_chat_member(message.chat.id, mesaj1[2])["user"]["id"]}] isimli kullanıcı {mesaj1[1]} süreyle sessize alındı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))                    
                        #else:message.reply(f"""Sessize almak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj1[2])["until_date"])}__** süresine kadar sessizde.""")
            else:message.reply("""Lütfen komutu "**__/mute @kullanıcı_ismi 5dk/1gün/10saat __**" şeklinde giriniz.""")

        else:
            mesaj2 = mesaj.split()
            if len(mesaj2) == 1:
                message.reply("Lütfen /mute komutunu sessize alacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")

            elif len(mesaj2) == 2:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[1])
                        except:message.reply(f"Bu grupta {mesaj2[1]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj2[1])["until_date"] == None:    
                        if client.get_chat_member(message.chat.id, mesaj2[1])["status"] not in yetkiler:
                            try:client.restrict_chat_member(message.chat.id, mesaj2[1], ChatPermissions())
                            except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini sessize alabilmem için ütfen beni yönetici yapın");quit()
                            if client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]:
                                message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı sessize alındı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                            else:
                                message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["first_name"]}](tg://user?id={mesaj2[1]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı sessize alındı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                        else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[1])["until_date"])}__** süresine kadar sessizde""")
                    else:message.reply("Birini sessize almak için yönetici olmanız lazım.")
                #else:message.reply("Lütfen /mute komutunu sessize almak kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")
                

            elif len(mesaj2) == 3:
                if zaman(mesaj2[1]) == False and zaman(mesaj2[2]) != False:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[1])
                        except:message.reply(f"Bu grupta {mesaj2[1]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj2[1])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj2[1])["status"] not in yetkiler:
                            try:client.restrict_chat_member(message.chat.id, mesaj2[1], ChatPermissions(), int(time.time() + zaman(mesaj2[2])))
                            except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini sessize alabilmem için ütfen beni yönetici yapın");quit()
                            if client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]:
                                message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["username"]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı {mesaj2[2]} süreyle sessize alındı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                            else:
                                message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["first_name"]}](tg://user?id={mesaj2[1]}[{client.get_chat_member(message.chat.id, mesaj2[1])["user"]["id"]}] isimli kullanıcı sessize alındı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                        else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Sessize almak istediğiniz kişinin zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[1])["until_date"])}__** süresine kadar sessizde.""")
                    else:message.reply("Birini Sessize almak için yönetici olmanız lazım.")

                elif zaman(mesaj2[2]) == False and zaman(mesaj2[1]) != False:
                    if client.get_chat_member(message.chat.id, message.from_user.id)["status"] in yetkiler:
                        try:client.get_chat_member(message.chat.id, mesaj2[2])
                        except:message.reply(f"Bu grupta {mesaj2[2]} isimli bir kullanıcı bulunamadı.");quit()
                        #if client.get_chat_member(message.chat.id, mesaj2[2])["until_date"] == None:
                        if client.get_chat_member(message.chat.id, mesaj2[2])["status"] not in yetkiler:
                            try:client.restrict_chat_member(message.chat.id, mesaj2[2], ChatPermissions(), int(time.time() + zaman(mesaj2[1])))
                            except errors.exceptions.bad_request_400.ChatAdminRequired:message.reply("Birisini sessize alabilmem için ütfen beni yönetici yapın");quit()
                            if client.get_chat_member(message.chat.id, mesaj2[2])["user"]["username"]:
                                message.reply(f"""@{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["username"]}[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["id"]}] isimli kullanıcı {mesaj2[2]} sessize alındı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                            else:
                                message.reply(f"""[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["first_name"]}](tg://user?id={mesaj2[2]}[{client.get_chat_member(message.chat.id, mesaj2[2])["user"]["id"]}] isimli kullanıcı sessize alındı.""", reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton(text="✅ Sesini açmak için Tıkla", callback_data=b"mute_kalk")]
                                ]))
                        else:message.reply("Sessize almak istediğiniz kişi bir yönetici.")
                        #else:message.reply(f"""Sessize almak istediğiniz kişi zaten **__{datetime.utcfromtimestamp(client.get_chat_member(message.chat.id, mesaj2[2])["until_date"])}__** süresine kadar sessizde.""")
                    else:message.reply("Birini Sessize almak için yönetici olmanız lazım.")

                else:
                    message.reply("Lütfen /mute komutunu sessize alacağınız kişinin mesajını yanıtlayarak veya kişinin ID'sini ya da kullanıcı adını girerek kullanınız.")

    else:message.reply("Burası bir özel sohbet. Özel sohbette seni sessize alamam.")

@ICOB_BOT.on_callback_query(Filters.callback_data("mute_kalk"))
def mute_kalk(client, cq):
    yetkiler = ("creator", "administrator")
    b = cq.message.text; b = b.replace("[", " "); b = b.replace("]", " "); b = b.split()[1]
    try:client.get_chat_member(cq.message.chat.id, b)
    except:cq.answer("Kullanıcı gruptan çıkmış. 🤗", show_alert=True);quit()
    if client.get_chat_member(cq.message.chat.id, cq.from_user.id)["status"] in yetkiler:
        if client.get_chat_member(cq.message.chat.id, b)["until_date"]:
            try:
                client.restrict_chat_member(cq.message.chat.id, b, ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_stickers=True,
                            can_send_animations=True,
                            can_send_games=True,
                            can_use_inline_bots=True,
                            can_invite_users=True,
                            can_add_web_page_previews=True,
                            can_send_polls=True,
                            can_pin_messages=True,
                            can_change_info=True))
                client.edit_message_text(cq.message.chat.id, cq.message.message_id, f"{cq.message.text}\n\n**__~Kullanıcının sesi açıldı.__**", parse_mode="Markdown")
                client.send_message(cq.message.chat.id, f"{cq.message.text.split()[0]} kullanıcının banı kaldırıldı.")
            except:cq.answer("Kullanıcının sesi açılamadı.", show_alert=True)
        else:cq.answer("Kullnıcının sesi zaten açık. 🤗",  show_alert=True)
    else:cq.answer("Birisinin banını kaldırabilmen için 🤴Yönetici olman gerekir.",  show_alert=True)


#############################

@ICOB_BOT.on_message(Filters.command(["unmute"]))
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
                #else:message.reply("/unmute komutunu mesaj yanıtlayarak veye kullanıcının id/username bilgilerini girerek kullanınız.")
            else:message.reply("/unmute komutunu mesaj yanıtlayarak veye kullanıcının id/username bilgilerini girerek kullanınız.")
    else:message.reply("Burası özel sohbet.")

#############################

ICOB_BOT.run()
