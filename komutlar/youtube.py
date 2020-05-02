from pyrogram import Client, Filters
from pytube import YouTube
import os

#YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()

@Client.on_message(Filters.command(["youtube"], ["/", "."]))
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
        os.remove(video)
