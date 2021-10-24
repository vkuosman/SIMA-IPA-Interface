import requests
import os
from datetime import datetime, time
from pygooglenews import GoogleNews
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import wikipediaapi

gn = GoogleNews(country = 'UK')

current_time = datetime.now()

location = os.path.dirname(os.path.abspath(__file__))

# Might not be needed in the future. Consider removing if not used anymore.
infoArray = []
with open(location + '/default_entries.txt') as infoFile:
    for line in infoFile:
        infoArray.append(line)

global_label = " "
global_input = " "
global_key = " "

# Setting up optional search engine webscraping in case of null Wikipedia results.
original_url = infoArray[3]
# Possibly change to PhantonJS later
chrome_browser = webdriver.Chrome()
chrome_browser.get(original_url)

def fire():
    requests.post("https://maker.ifttt.com/trigger/LightRed2/with/key/" + global_key)
    global_label.config(text="- Activate fireplace scene -")
    return "Selvä, aktivoidaan valojen takka-tila."

def reminder():
    response = {"value1":"Hello world!", "value2":"", "value3":""}
    requests.post("https://maker.ifttt.com/trigger/PythonCalendar/with/key/" + global_key, data = response)
    global_label.config(text="- Set a calendar note-")
    return  "Okei, muistutus luotu Google kalenteriin."

def light():
    requests.post("https://maker.ifttt.com/trigger/LightWhite/with/key/" + global_key)
    global_label.config(text="- Set the lights to daylight -")
    return "Toki, laitetaan valot päälle."

def toggle():
    requests.post("https://maker.ifttt.com/trigger/LightOff/with/key/" + global_key)
    global_label.config(text="- Toggle the lightswitch -")
    return "Selvä, painakaamme katkaisinta."
    
def music():
    requests.post("https://maker.ifttt.com/trigger/PythonMusic/with/key/" + global_key)
    global_label.config(text="- Play music -")
    return "Selvä, soitetaan musiikkia."

def feeling():
    global_label.config(text="- Asking how the bot is feeling -\n\nMinulla menee oikein hyvin!\nEntäs sinä?")
    return "Minulla menee oikein hyvin. Entäs sinä?"

def feeling_me():
    global_label.config(text="- Telling the bot how you are doing -\n\nHyvä kuulla!")
    return "Hyvä kuulla"

def time_ask():
    time_string = str(current_time)
    text_output = "- Asking what the time is -\n\nKello on tällä hetkellä:\n" + time_string
    global_label.config(text=text_output)
    return "Kello on tällä hetkellä" + time_string

def meaning_ask():
    global_label.config(text="- Asking for an answer to life, universe and everything -\n\nTäytyypä miettiä tuota.\nPalataan asiaan täsmälleen 7.5 miljoonan vuoden päästä.")
    return "Täytyypä miettiä tuota. Palataan asiaan täsmälleen 7,5 miljoonan vuoden päästä."

def news_default():
    text_output = "- Asking about news -\n\nToki! Tässä päivän uutisia Google News -palvelusta:\n"
    search = gn.top_news()
    news_items = search['entries']
    i = 0
    while i < 6:
        text_output = text_output + "\n\n" + str(news_items[i].title)
        i += 1
    global_label.config(text= text_output)
    return "Toki! Tässä päivän uutisia Google News -palvelusta"

def name_ask():
    global_label.config(text="- Asking the name of the bot -\n\nMinun nimeni on SIMA.\nSuomenkielinen Inhimillinen Mietiskelevä Assistentti")
    return "Minun nimeni on SIMA. Suomenkielinen Inhimillinen Mietiskelevä Assistentti"

def red_light():
    requests.post("https://maker.ifttt.com/trigger/LightRed/with/key/" + global_key)
    global_label.config(text="- Set the lights to red -")
    return "Selvä, asetetaan valot punaisiksi"

def blue_light():
    requests.post("https://maker.ifttt.com/trigger/LightBlue/with/key/" + global_key)
    global_label.config(text="- Set the lights to blue -")
    return "Selvä, asetetaan valot sinisiksi"

def green_light():
    requests.post("https://maker.ifttt.com/trigger/LightGreen/with/key/" + global_key)
    global_label.config(text="- Set the lights to green -")
    return "Selvä, asetetaan valot vihreiksi"

def violet_light():
    requests.post("https://maker.ifttt.com/trigger/LightViolet/with/key/" + global_key)
    global_label.config(text="- Set the lights to violet -")
    return "Selvä, asetetaan valot violeteiksi"

def say_command():
    global_label.config(text="- Asking the bot to repeat something -")
    return global_input[1]

def introduction():
    global_label.config(text="- Introducing yourself to the bot -")
    return "Hei vain" + global_input[1] + ". Sima on palveluksessanne."

def search_information():
    # If this function ends up being the only one to use urls, remove the former infoArray lines.
    infoArray = []
    with open(location + '/default_entries.txt') as infoFile:
        for line in infoFile:
            infoArray.append(line)

    original_url = infoArray[3]

    finn_wiki = wikipediaapi.Wikipedia('fi')
    page_py = finn_wiki.page(global_input[1])

    summary = page_py.summary[0:300]
    summary = summary[:summary.rfind('.')]
    # Not an elegant solution. Consider updating in the future.
    if not summary:
        url = original_url + global_input[1]
        chrome_browser.get(url)
        try:
            summary = chrome_browser.find_element_by_xpath('//*[@id="extabar"]/div/div/div[1]/div/div[1]').text.replace("/\n","")
            summary = summary[:summary.rfind('\n')]
            print("case 1")
        except NoSuchElementException:
            url = original_url + "mikä+on+" + global_input[1]
            try:
                summary = chrome_browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[1]').text
                print("case 1.5")
                # Checking if the search result is actually a list:
                if not summary: 
                    summary = chrome_browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[1]').text
                    summary = summary[:summary.rfind('\n')]
                    print("case list")
            except:
                try:
                    summary = chrome_browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/span/span').text
                    print("case 2")
                except NoSuchElementException:
                    try:
                        summary = chrome_browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[1]/a').text
                        print("case 3")
                    except NoSuchElementException:
                        try:
                            summary = chrome_browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span/span').text
                            print("case 4")
                        except NoSuchElementException:
                            try:
                                summary = chrome_browser.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]').text
                                print("case 5")
                            except:
                                summary = "Tässä on mitä löysin."
        # Unnecessary repetition. Consider updating in the future.
        summary_line = summary
        if len(summary) >= 150:
            newline_num = summary.find(' ', 150)
            summary_line = summary[:newline_num] + "\n" + summary[newline_num + 1:]
        global_label.config(text="- Asking the bot for some information -\n\nHakujeni perusteella:\n" + summary_line)
        return "Hakujeni perusteella, " + summary
    else:
         # Unnecessary repetition. Consider updating in the future.
        summary_line = summary
        if len(summary) >= 150:
            newline_num = summary.find(' ', 150)
            summary_line = summary[:newline_num] + "\n" + summary[newline_num + 1:]
        global_label.config(text="- Asking the bot for some information -\n\nHakujeni perusteella:\n" + summary_line)
        return "Wikipedian mukaan, " + summary

def demo_start():
    global_label.config(text="- Starting Demo --\n\nHei! Minä olen SIMA, virtuaalinen assistentti.\nMinut on kehitetty muunmuassa ymmärtämään puhuttua suomenkieltä,\nlähettämään komentoja eri älylaitteille,\nsekä vastaamaan kysymyksiisi.\nHaluaisitko nähdä listan mahdollisista toiminnoista?")
    return "Hei! Minä olen SIMA, virtuaalinen assistentti.\nMinut on kehitetty muunmuassa ymmärtämään puhuttua suomenkieltä,lähettämään komentoja eri älylaitteille,sekä vastaamaan kysymyksiisi. Haluaisitko nähdä listan mahdollisista toiminnoista?"


def null_case():
        global_label.config(text="- Unknown -")
        return "Anteeksi, nyt en ymmärtänyt. Voisitko toistaa?"

def sendRequest(input, label=" ", key=" "):
    global global_label
    global global_input
    global global_key
    global_input = input
    global_label = label
    global_key = key
    if isinstance(input, str):
        result_return = eval(input + "()")
    else:
        result_return = eval(input[0] + "()")
    return result_return