import urllib.request, requests
from bs4 import BeautifulSoup



def News():
    #specify the url of news website from where the news should be scrpped to be displayed by bot
    url = "http://www.lokmat.com/"

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    news = soup.find('ul', class_='live-news-list')

    for i in news.findAll('li'):
        data = i.text
        return data


