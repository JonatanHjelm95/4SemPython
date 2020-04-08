from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import sys
import csv
import html5lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def getCryptos(URL):
    cryptos = []
    req = Request(URL)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html5lib')
    for tr in soup.findAll('tr', attrs={'class': 'cmc-table-row'}):
        crypto = {}
        rank = tr.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank'})
        crypto['rank'] = int(rank.find('div').text)
        name = tr.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})
        crypto['name'] = str(name.find('div').text).capitalize()
        change = tr.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h'})
        crypto['change'] = change.find('div').text
        cryptos.append(crypto)
    return cryptos

def googleSearch(crypto):
    query = str(crypto) + ' crypto coin'
    driver = webdriver.Firefox()
    driver.get("https://google.com/")
    #assert "Coinmarketcap" in driver.title
    searchbar = driver.find_element_by_name("q")
    searchbar.send_keys(query)
    searchbar.send_keys(Keys.RETURN)
    

# Sort results by 24H % change, high -> low
def sortByChange(cryptos):
    l = sorted(cryptos, key = lambda i: (float(str(i['change']).replace('%',''))))
    return l[::-1]

# sort results by name
def sortByName(cryptos):
    return sorted(cryptos, key = lambda i: str(i['name']))

# Sort results by rank; 1,2,3...
def sortByRank(cryptos):
    return sorted(cryptos, key = lambda i: i['rank'])

# returns top 10 ranks
def getTop10Rank(cryptos):
    l = sortByRank(cryptos)
    return l[:10]

# returns top 10 % change
def getTop10Change(cryptos):
    l = sortByChange(cryptos)
    return l[:10]


# Searches top 100 ranked cryptovalutas, sorts by % change
# picks top 1 and performs a google search with selenium
if __name__ == '__main__':
    cryptos = getCryptos('https://coinmarketcap.com/')
    top10 = getTop10Change(cryptos)
    top1Name = top10[0]['name']
    googleSearch(top1Name)