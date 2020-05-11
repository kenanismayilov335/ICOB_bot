from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(Filters.new_chat_members)
def hosgeldin(client, message):
    butonlar = [[InlineKeyboardButton("🎉 Grubumuza Katılın", url="https://t.me/icobteam"),
                 InlineKeyboardButton("📝 Kodlarım", url="https://github.com/izci-py/ICOB_bot")],
                 [InlineKeyboardButton("📰 Instagram", url="https://www.instagram.com/i.cobvision/?hl=tr")]
                 ]
                
    kullanici = [f"[{i.first_name}](tg://user?id={i.id})" for i in message.new_chat_members]
    mesaj = f"""Merhaba {"".join(kullanici)}, **{message.chat.title}** grubuna hoşgeldin. Seni aramızda görmekten çok mutlu olduk. 😊"""
    message.reply(mesaj, reply_markup=InlineKeyboardMarkup(butonlar))
