from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import sys
import csv
import html5lib

def getCryptos(URL):
    cryptos = []
    req = Request(URL)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html5lib')
    for tr in soup.findAll('tr', attrs={'class': 'cmc-table-row'}):
        crypto = {}
        rank = tr.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank'})
        crypto['rank'] = rank.find('div').text
        name = tr.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})
        crypto['name'] = str(name.find('div').text).capitalize()
        change = tr.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h'})
        crypto['change'] = change.find('div').text
        cryptos.append(crypto)
    return cryptos

def sortByChange(cryptos):
    return sorted(cryptos, key = lambda i: (float(str(i['change']).replace('%',''))))

def sortByName(cryptos):
    return sorted(cryptos, key = lambda i: str(i['name']))

def sortByRank(cryptos):
    return sorted(cryptos, key = lambda i: i['rank'])


if __name__ == '__main__':
    URL = 'https://coinmarketcap.com/'
    cryptos = getCryptos(URL)
    print(sortByRank(cryptos))