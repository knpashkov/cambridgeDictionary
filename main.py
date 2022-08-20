import requests
from bs4 import BeautifulSoup
import os

while True:
    req = input('Слово: ')
    url = 'https://dictionary.cambridge.org/dictionary/english-russian/' + req
    url1 = 'https://dictionary.cambridge.org/'

    response = requests.get(url, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    soup = BeautifulSoup(response.text, 'lxml')
    all_audio = soup.findAll('source')

    try:
        lnk = ''
        for i in range(len(all_audio)):
            if ('.mp3' in all_audio[i]['src']) and ('/us_pron/' in all_audio[i]['src']):
                lnk = url1 + all_audio[i]['src']
        r = requests.get(lnk, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    except:
        print('Слово отсутствует')
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        mp3 = open(req + '.mp3', 'wb')
        mp3.write(r.content)
        mp3.close()
        print('Запись сохранена')
        input()
        os.system('cls' if os.name == 'nt' else 'clear')





