import requests
from bs4 import BeautifulSoup
import re


wordlist = []

session = requests.Session()



def downloadTable(url):
    response = session.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    tableRaws = soup.findAll('tr')
    for raw in tableRaws:
        wordObjects = raw.findAll('td')
        word = []
        for wordObject in wordObjects:
            word.append(re.sub(r'\xa0', '', wordObject.text))
        wordlist.append(word)
        print(word)
    print('-----------------------------------------------------------------------------')
    

def downloadWords(url):
    response = session.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.findAll('li')
    for link in lis[23:99]:
        downloadTable(link.find('a', href=True)['href'])




downloadWords('https://langformula.ru/voc3000/')