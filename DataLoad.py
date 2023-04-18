import requests
from bs4 import BeautifulSoup
import re
import json


wordlist = dict()

session = requests.Session()


def downloadTable(url, title,out=0):
    wordlist[title] = []
    response = session.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    tableRaws = soup.findAll('tr')
    for raw in tableRaws:
        wordObjects = raw.findAll('td')
        word = []
        for wordObject in wordObjects:
            word.append(re.sub(r'\xa0', '', wordObject.text))
        wordlist[title].append(word)
        if out != 0: print(word)
    if out != 0: print('-----------------------------------------------------------------------------')
    

def downloadWords(url,out=0):
    response = session.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.findAll('li')
    for link in lis[23:99]:
        hz = link.find('a', href=True).text
        downloadTable(link.find('a', href=True)['href'], link.find('a', href=True).text,out)

def get_words(out=0):

    downloadWords('https://langformula.ru/voc3000/',out=1)
    #print(wordlist)

    with open("words.json", "w") as outfile:
        json.dump(wordlist, outfile)
def load_words():
    with open('words.json', 'r') as infile:
        my_dict = json.load(infile)
    return my_dict

