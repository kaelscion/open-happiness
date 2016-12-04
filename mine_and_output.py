from bs4 import BeautifulSoup
import requests

class data_miner:


    def __init__(self, base_url):
        self.base_url = base_url


    def get_links(self):
        html=self.base_url
        payload={'q':'fluffy kittens'}
        r=requests.get(html, params=payload)
        soup=BeautifulSoup(r.content, "html5lib")
        with open('image_results.html', 'w') as f:
            for image in soup.find_all('img'):
                f.write(image.attrs['src'] + '\n')
        
x = data_miner('http://www.google.com/images')
x.get_links()