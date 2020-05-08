from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from chrome_ayarlar.chrome_options import chrome_options
import urllib.request
import os
import random


@Client.on_message(Filters.command(["instagram"], ["/", "."]))
def instagram(client, message):
    bekle = message.reply("Bekleyin...")
    metin = message.text

    hesap_isim = metin.split()
    hesap_isim_duzen = " ".join(hesap_isim[1:])

    if len(hesap_isim) <= 1:
        bekle.edit("Lütfen bir hesap ismi giriniz")
    
    else:
        br = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        #pc için br'yi aşağıdaki şekilde değiştiriniz.
        #br1 = webdriver.Chrome(executable_path="chromedriver_yolu")

        br.get(f"https://www.instagram.com/{hesap_isim_duzen}/?hl=tr")

        wait = WebDriverWait(br, 20)

        pp = br.find_elements_by_tag_name("img")

        if len(pp) == 0:
            bekle.edit(f"**{hesap_isim_duzen}** isimli bir hesap bulunmamaktadır")

        else:
            liste = []
            for i in pp:
                liste.append(i.get_attribute("src"))

            random_sayi = random.randint(1, 100000)

            liste = liste[0]
            urllib.request.urlretrieve(liste, f"pp{random_sayi}.png")

            client.send_photo(message.chat.id, f"pp{random_sayi}.png")

            os.remove(f"pp{random_sayi}.png")

            gonderi = wait.until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/a/span')))

            takipci = wait.until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')))

            takip = wait.until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')))

            mesaj1 = "**{}** isimli hesabın:\n\nGönderi sayısı: **{}**\nTakipçi sayısı: **{}**\nTakip sayısı: **{}**".format(hesap_isim_duzen, gonderi.text, takipci.text, takip.text)
            bekle.edit(mesaj1)
