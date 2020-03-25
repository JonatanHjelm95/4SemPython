import random
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import requests
import os
import matplotlib.pyplot as plt
import numpy as np
#cpu_count = multiprocessing.cpu_count()

class BookFetcher:
    def __init__(self, url_list):
        self.url_list = url_list

    def download(url, filename):
        try:
            r = requests.get(url)
            if r.status_code is 200:
                book = str(r.text.encode(r.apparent_encoding))
                # Replacing bad characters
                book = book.replace('\\n', '\n').replace('\\r', '\r').replace('\\xc3\\xa2\\xc2\\x80\\xc2\\x99', '\'').replace('\\xc3\\xa2\\xc2\\x80\\xc2\\x94', '-')
                try:
                    title = BookFetcher.getTitle(BookFetcher, book)
                except:
                    title = 'No title'

                file = open("HandIn6/Downloads/"+str(title)+".txt", "w")
                file.write(book)
                return BookFetcher.avg_vowels(book)
            elif r.status_code is 404:
                raise NotFoundException("Page not found")
        except Exception as e:
            print(e)

    def multi_download(self):
        urlList = BookFetcher.urllist_generator(BookFetcher, 100)
        BookList = []
        book = {}
        with ThreadPoolExecutor(5) as ex:
            for _ in urlList:
                res = ex.submit(BookFetcher.download(_,_), urlList)
  
    
    def multithreading(self, func, args, workers=5):
        with ThreadPoolExecutor(workers) as ex:
            try:
                res = ex.submit(func, args).result()
            except:
                pass
        return res

    def urllist_generator(self, n):
        urllist = []
        for i in range(n):
            baseURL = "https://www.gutenberg.org/files/"
            urllist.append(baseURL+str(i)+"/"+str(i)+"-0.txt")
        return urllist

    
    def getTitle(self, book):
        splitted = book.split('\n')
        for i in range(len(splitted)):
            if "Title:" in splitted[i]:
                return splitted[i].replace('Title:', '').replace(' ', '').replace('\r','').replace('?', '')

    def isVowel(self, ch):
        if ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u':
            return True
        else:
            return False
               
    def countVowels(self, word):
        count = 0
        for i in range(len(word)):
            if BookFetcher.isVowel(BookFetcher, word[i]):
                count+=1
        return count

    def avg_vowels(text):
        splitted = text.split(' ')
        vowelCount = []
        for s in splitted:
            vowelCount.append(BookFetcher.countVowels(BookFetcher, s))
        return sum(vowelCount)/len(vowelCount)

    def hardest_read():
        pass

    def read_books(self):
        books = []
        for filename in os.listdir('HandIn6\Downloads'):
            with open(os.path.join('HandIn6\Downloads', filename), 'r') as f: # open in readonly mode
                
                text = f.read()
                splitted = str(f).split('\\')
                x = splitted[-1]
                xSplitted = x.split('.txt')
                title= xSplitted[0]
                book = {}
                book['title'] = title
                book['rating'] = BookFetcher.avg_vowels(text)
                books.append(book)
        return sorted(books, key = lambda i: (i['rating']))

    def create_chart(self):
        books = BookFetcher.read_books(BookFetcher)
        titles = []
        ratings = []
        for b in books:
            titles.append(b['title'])
            ratings.append(b['rating'])
        y_pos = np.arange(len(titles))
        plt.xticks(y_pos, titles, rotation='vertical')
        plt.bar(y_pos, ratings, align='center', alpha=0.5)
        plt.ylabel('Books')
        plt.tight_layout()
        plt.show()

    def __iter__(self):
        return self

    def __next__(self):
        if random.choice(["go", "go", "go", "stop"]) == "stop":
            raise StopIteration  # signals "the end"
        return 1

class NotFoundException(Exception):
    pass


if __name__ == "__main__":
    # Fetching books
    #BookFetcher.multi_download(BookFetcher)
    # Plotting books sorted with lowest->highest avg_vocal_count
    BookFetcher.create_chart(BookFetcher)