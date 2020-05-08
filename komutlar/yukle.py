from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chrome_ayarlar.chrome_options import chrome_options
from pyrogram import Client, Filters
import os


def yukle1(dosya, aciklama, mesaj, message, client):
    br1 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    #pc nizde çalıştıracaksanız br1'i aşağıdaki şekilde değiştiriniz.
    #br1 = webdriver.Chrome(executable_path="chromedriver_yolu")
    br1.get("https://dosya.co/")

    wait = WebDriverWait(br1, 100)

    yukle_buton = br1.find_element_by_id("my_file_element")

    #yukle_buton.click()
    yukle_buton.send_keys(dosya)

    #açıklamaclass = "fdescr"
    #herkeseaçık = "pub_file_0"
    #sonyukle = "btn_blue blue-linear"
    aciklama_yer = wait.until(EC.element_to_be_clickable((
        By.CLASS_NAME, "fdescr")))
    aciklama_yer.send_keys(str(aciklama))

    son_yukle = br1.find_element_by_xpath('//*[@id="upload_controls"]/tbody/tr[4]/td[2]/input')
    son_yukle.click()

    link = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="ic0-"]')))
    dosya_indirme_link = f"[Dosya İndirme Linki]({link.text})"

    sil_link = wait.until(EC.element_to_be_clickable((
        By.XPATH, '/html/body/div[2]/table/tbody/tr[3]/td/div/ul/li[4]/a')))
    sil_link.click()

    sil_link_text = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="ic3-"]')))
    dosya_silme_link = f"[Dosyayı silme linki]({sil_link_text.text})"

    if len(aciklama) == 0:
        mesaj.edit(f"""Dosyanız aşağıdaki linke başarıyla yüklenmiştir : \n\n📂 {dosya_indirme_link}\n\nDosyayı silme linki @{message.from_user.username} kullanıcıya özelden atılmıştır.""", disable_web_page_preview=True, parse_mode="Markdown")
        client.send_message(message.from_user.id, f"Dosyanızı silmek için aşağıdaki linke giriniz : \n🗑 {dosya_silme_link}", disable_web_page_preview=True, parse_mode="Markdown")

    elif len(aciklama) > 0:
        mesaj.edit(f"""Dosyanız "**__{aciklama}__**" açıklamasıyla aşağıdaki linke başarıyla yüklenmiştir : \n\n📂 {dosya_indirme_link}\n\nDosyayı silme linki @{message.from_user.username} kullanıcıya özelden atılmıştır.""", disable_web_page_preview=True, parse_mode="Markdown")
        client.send_message(message.from_user.id, f"Dosyanızı silmek için aşağıdaki linke giriniz : \n🗑 {dosya_silme_link}", disable_web_page_preview=True, parse_mode="Markdown")

@Client.on_message(Filters.command(["yukle"], ["/", "."]))
def yukle(client, message):
    bekle = message.reply("Bekleyin...")
    if message.reply_to_message:
        if message.reply_to_message.media:
            dosya = client.download_media(message.reply_to_message)
            yukle1(dosya, " ".join(message.text.split()[1:]), bekle, message, client)
        else:
            bekle.edit("Yanıtladığınız mesaj bir dosya değil. Lütfen bir dosya yanıtlayınız.")
    else:
        bekle.edit("Lütfen yüklemek istediğiniz dosyayı yanıtlayarak /yukle komutunu uygulayınız")
