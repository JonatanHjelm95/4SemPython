import Webscraper as ws
import matplotlib.pyplot as plt
import numpy as np

def top10ChartChange():
    cryptos = ws.getCryptos('https://coinmarketcap.com/')
    cryptos = ws.getTop10Change(cryptos)
    cryptos = cryptos[::-1]
    names = []
    values = []
    for c in cryptos:
        names.append(c['name'])
        values.append(c['change'])
    y_pos = np.arange(len(names))
    plt.xticks(y_pos, names, rotation='vertical')
    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.ylabel('24h % change')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    top10ChartChange()
    
