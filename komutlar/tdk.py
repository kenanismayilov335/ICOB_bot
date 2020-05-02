from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
import requests


@Client.on_message(Filters.command(["tdk"], ["/", "."], case_sensitive=True))
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
            
