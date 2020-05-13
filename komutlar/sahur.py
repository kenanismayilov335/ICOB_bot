from pyrogram import Client, Filters
import requests
import datetime
import pytz


@Client.on_message(Filters.command(["sahur", "sahur@icob_bot"]))
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
