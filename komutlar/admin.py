from pyrogram import Client, Filters


@Client.on_message(Filters.command(["admin"]))
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

