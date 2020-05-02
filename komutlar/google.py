from pyrogram import Filters, Client
from google_search_client.search_client import GoogleSearchClient
import ast


@Client.on_message(Filters.command(['google'], ['.', '/']))
def google_search(client, message):
    bekle = message.reply("Araştırılıyor...")
    text = message.text
    if len(text.split()) == 1:
        message.edit("Lütfen araştırmak istediğiniz kelimeyi giriniz")
        return
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
