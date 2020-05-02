from pyrogram import Client, Filters


def grub_fonk(grub, message, client):
    try:
        grub_bilgi = client.get_chat(grub)
    except:
        message.reply("Maalesef, böyle bir grub bulunamadı.")
        quit()

    try:foto_id = grub_bilgi["photo"]["big_file_id"]
    except TypeError:foto_id = None

    kisitlama = grub_bilgi["is_restricted"]
    if kisitlama:
        kisitlama = "Evet**"
        kisitlama += f"""
👉 Kısıtlama Platformu : **{grub_bilgi["restrictions"]["platform"]}**
👉 Kısıtlama Nedeni : **{grub_bilgi["restrictions"]["reason"]}**
👉 Kısıtlama Metni : **{grub_bilgi["restrictions"]["text"]}"""
    else:
        kisitlama = "Hayır"

    mesaj = f"""👥 @{grub_bilgi["username"]} isimli grubun ;\n"""
    mesaj += f"""
👉 ID : **{grub_bilgi["id"]}**
👉 Başlık : **{grub_bilgi["title"]}**
👉 Grub Türü : **{grub_bilgi["type"]}**
👉 Üye Sayısı : **{grub_bilgi["members_count"]}**
👉 Fotoğraf ID : **{foto_id}**
👉 Kısıtlama : **{kisitlama}**
👉 Açıklama : **{grub_bilgi["description"]}**
👉 Kullanıcı Adı : @**{grub_bilgi["username"]}**
👉 Davet Linki : **{grub_bilgi["invite_link"]}**
"""
    message.reply(mesaj, disable_web_page_preview=True)


@Client.on_message(Filters.command(["grub"], ["/", "."]))
def grub(client, message):
    bilgi = message.text.split()
    if message.chat.type == "private":
        if len(bilgi) == 1 or len(bilgi) > 2:
            message.reply("""Lütfen komutu "**__/grub grub_ismi/id__**" şeklinde giriniz. """)

        else:
            grub_fonk(bilgi[1], message, client)

    elif message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "channel":
        if len(bilgi) == 1:
            grub_fonk(message.chat.id, message, client)

        elif len(bilgi) == 2:
            grub_fonk(bilgi[1], message, client)          

        else:
            message.reply("""Lütfen komutu "**__/grub grub_ismi/id__**" şeklinde giriniz. """)
