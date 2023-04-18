import requests
from bs4 import BeautifulSoup
import re



wordlist = dict()

session = requests.Session()


def downloadTable(url, title):
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
        #print(word)
    #print('-----------------------------------------------------------------------------')
    

def downloadWords(url):
    response = session.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.findAll('li')
    for link in lis[23:99]:
        hz = link.find('a', href=True).text
        downloadTable(link.find('a', href=True)['href'], link.find('a', href=True).text)


downloadWords('https://langformula.ru/voc3000/')
print(wordlist)