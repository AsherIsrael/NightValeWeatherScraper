from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import re

class WeatherScraper(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            text = self.get_starttag_text()
            isWeather = re.match("Weather", text)
            if isWeather:
                
                weatherName = re.search(". (?=by)", text)
                self.titles = self.titles + [weatherName]

    def getTitles(self, url):
        self.titles = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return self.titles
        else:
            return []


def nightValeSpider():
    print("We got this far at least")
    totalTitles = []
    try:
        parser = WeatherScraper()
        totalTitles = totalTitles + parser.getTitles("http://nightvale.libsyn.com/")
        for title in totalTitles:
            print(title)
    except:
        print("Something went wrong")

