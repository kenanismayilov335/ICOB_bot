from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
from pyrogram import Client, Filters
from chrome_ayarlar.chrome_options import chrome_options


@Client.on_message(Filters.command(["pinterest"], ["/", "."]))
def pinterest(client, message):
    bekle = message.reply("Bekleyin...")

    metin = message.text.split()
    if len(metin) == 1:
        bekle.edit("""Lütfen komutu "__ --/pinterest-- --kelime-- __" şeklinde giriniz. """)

    else:
        driver = "chromedriver.exe"

        br3 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        br3.get("https://tr.pinterest.com/login")

        wait = WebDriverWait(br3, 300)

        user_input = wait.until(EC.element_to_be_clickable((
            By.XPATH,'//*[@id="email"]')))
        user_input.send_keys("ramazanizci1638@gmail.com")

        sifre_input = wait.until(EC.element_to_be_clickable((
            By.XPATH,'//*[@id="password"]')))
        sifre_input.send_keys('<print("pa55\/\/0rd")/>')

        oturum2_button = wait.until(EC.element_to_be_clickable((
            By.XPATH ,"""//*[@id="__PWS_ROOT__"]/div[1]/div/div/
            div[3]/div/div/div[3]/form/div[5]/button""")))
        oturum2_button.click()

        ara = wait.until(EC.element_to_be_clickable((
            By.XPATH , '//*[@id="searchBoxContainer"]/div/div/div[2]/input')))
        ara.send_keys(metin[1:-1])
        ara.send_keys(Keys.ENTER)


        resimler = wait.until(EC.presence_of_all_elements_located((
            By.TAG_NAME, "img"
        )))

        linkler = []

        
        if len(linkler) < 20:
            br3.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            a = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
            for img in a:

                if img.get_attribute("src") in linkler:
                    pass
                else:
                    linkler.append(img.get_attribute("src"))

        elif len(linkler) == 20:
            pass

        sayac = 0
        for i in linkler:
            sayac += 1
            a = urllib.request.urlretrieve(i, f"resim{sayac}.png")
            print(a)
            client.send_photo(message.chat.id, a[0])
            os.remove(a[0])
            
            
         
