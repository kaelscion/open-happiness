from bs4 import BeautifulSoup
import re
import requests

class data_miner:


    def __init__(self, base_url):
        self.base_url = base_url


    def get_links(self):
        html=self.base_url
        payload={'q':'fluffy kittens'}
        r=requests.get(html, params=payload)
        soup=BeautifulSoup(r.content, "html5lib")
        #FINDS ALL LINKS ON SOUP VARIABLE PAGE
        with open('image_results.html', 'w') as f:
            for link in soup.find_all('a'):
                f.write('\n' + link.attrs['href'])


x = data_miner("https://www.google.com/images")
x.get_links()
