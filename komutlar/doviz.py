from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
import requests 
from bs4 import BeautifulSoup


@Client.on_message(Filters.command(["doviz"], ["/", "."]))
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

    bekle.edit(bilgi, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Grubumuza Katılın", url="https://t.me/joinchat/PNPv9RJrHf8F0KlPCaC4-Q")]
        ]))