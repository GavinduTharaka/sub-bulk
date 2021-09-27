import requests, bs4, time, os
from colorama import Fore, init
from bs4 import BeautifulSoup as bSoup
import telebot
channel_username = "@uchksdhgckuds"
Download_from = ""
TOKEN = "2041643747:AAHR4SIb68XwULgASf1RfU-BQocjNDsCx7k"
bot = telebot.TeleBot(TOKEN)
import urllib.parse

def urlencode(str):
  return urllib.parse.quote(str)


def urldecode(str):
  return urllib.parse.unquote(str)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    try:
        global channel_username
        count = 0
        sphrase = 1
        for sphrase in range(901):
            url1 = "https://www.baiscopelk.com/category/සිංහල-උපසිරැසි/චිත්%e2%80%8dරපටි/page/" + str(sphrase) + "/"
            r1 = requests.get(url1)
            print(r1)

            if r1.status_code != 200:
                print("Make sure you have internet !")
                time.sleep(8)
                exit()

            dat = r1.text
            data = dat[int(dat.find('</span> Home</a><span ')):999999]

            page_soup = bSoup(data, "html.parser")

            html = page_soup.find_all("div", {"class": "post-thumbnail"})
            imgsrcList = []
            ahrefList = []
            linkl = []
            links = []
            i = 0

            for x in range(len(html)):
                if "mega-menu-link" in str(html[x]) or "rel=\"bookmark\"" in str(html[x]) or "ttip" in str(html[x]):
                    pass
                else:
                    htmldata = str(html[x])
                    page_soup1 = bSoup(htmldata, "html.parser")
                    hreflink = page_soup1.findAll('a')  # [0]['href'] #page_soup.find('MADE BY GH0STH4CK3R')
                    if len(hreflink) != 0:
                        i += 1
                        links.append(hreflink[0]['href'])

            print("\nDisplaying", i, "Results\n\n")
            for y in range(len(links)):
                link = str(links[y]).replace('https://www.baiscopelk.com/', '')
                link = link.replace('/', ' ')
                linkl.append(link)
                link = link.replace('-', ' ')
                print("[", y + 1, "]  ", urldecode(link), "\n")
            # print(ahrefList[0])

            print()
            for j in range(y):
                n = j + 1
                print("\nYou choosed >> ", linkl[n - 1])
                url2 = links[n - 1]
                r2 = requests.get(url2)
                data2 = r2.text
                page_soup2 = bSoup(data2, "html.parser")
                html2 = page_soup2.find_all("a", {"style": "color: #ff3300;"})
                page_soup2 = bSoup(data2, "html.parser")
                ziplink = html2[0]['href']
                html2 = page_soup2.find_all("a", {"style": "color: #ff3300;"})
                url3 = ziplink  # "https://www.baiscopelk.com/Downloads/scooby-doo-the-sword-and-the-scoob-2021-1-zip/ (C) Copyright (R) GH0$TH4CKR"
                r3 = requests.get(url3)
                if r3.status_code == 200:
                    sv = urldecode(linkl[n - 1]) + ".zip"
                    file = open(sv, "wb")
                    file.write(r3.content)
                    file.close()
                    print("File download success !")
                    doc = open(sv, 'rb')
                    caption = str(sv)
                    bot.send_document(channel_username, doc, caption=caption)
                    print(sv, "Send file")
                    count = count + 1
                    doc.close()
                    try:
                        os.remove(sv)
                        print("Downloaded File Removed")
                    except:
                        print("File Was removed")
                    act = 0
                else:
                    print("Something went wrong !  Error code ", r3.status_code)
                    fE = open("errors.txt", "a")
                    fE.write("Error code " + str(r3.status_code) + "\n")
                    fE.close()
                    bot.send_message(user_id, "Something went wrong !\nError code " + str(
                        r3.status_code) + "\n")
            bot.send_message(user_id, "Dounloaded Count : " + str(count))
    except Exception as e:
        bot.send_message(user_id, "Error : " + str(e))
bot.polling()
