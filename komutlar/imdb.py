from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
import requests
from bs4 import BeautifulSoup


@Client.on_message(Filters.command(["imdb"], ["/", "."]))
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

    bekle.edit(imdb_sonuc, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Grubumuza Katılın", url="https://t.me/joinchat/PNPv9RJrHf8F0KlPCaC4-Q")]
        ]))
