import requests
import re
from bs4 import BeautifulSoup

def scrape_site():
    pages_left = get_pages("http://nightvale.libsyn.com/")
    page_num = 1
    while pages_left:
        pages_left = get_pages("http://nightvale.libsyn.com/webpage/page/{}/size/50".format(page_num))
        page_num += 1
    

def get_pages(url):
    page = requests.get(url)
    found_things = False
    soup = BeautifulSoup(page.content, 'html.parser')
    p_tags = soup.find_all('p')
    weather_strings = []
    for tag in p_tags:
        text = tag.get_text()
        if(re.search(r'(Weather:)', text)):

            found_title = re.search(r'".+"', text)
            if found_title:
                found_things = True
                title = found_title.group()
                artist = ""
                link = ""
                words = text.split(" ")
                adding = False
                for word in words:
                    if adding:
                        reg_pattern = re.compile(r"(\b[,\.]\b|[\w\d\\])+")
                        cleaned_word = re.search(reg_pattern, word)

                        if cleaned_word:
                            cleaned_word = cleaned_word.group()
                            if "." in cleaned_word:
                                link = str(cleaned_word)
                                break
                            artist = artist + cleaned_word + " "
                        else:
                            break
                    if word == "by":
                        adding = True
                print(title)
                print("by")
                print(artist)
                print(link)
                print()
    return found_things   

scrape_site()