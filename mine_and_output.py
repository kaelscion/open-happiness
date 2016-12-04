from bs4 import BeautifulSoup
import requests
import urllib2
import shutil

urls = []

class data_miner:
    

    def __init__(self, base_url):
        self.base_url = base_url


    def get_links(self, query):
        html=self.base_url
        payload={'q': query}
        r=requests.get(html, params=payload)
        soup=BeautifulSoup(r.content, "html5lib")
        for image in soup.find_all('img'):
            urls.append(image.attrs['src'])
    
    def download_files(self, query):
        number = 1
        for item in urls:
            with open(query + str(number) + '.jpg', 'wb') as out_file:
                req = requests.get(item, stream=True)
                shutil.copyfileobj(req.raw, out_file)
                number += 1
            print number
                
    
x = data_miner('http://www.google.com/images')
x.get_links("fluffy kittens")
x.download_files("fluffy kittens")
            
                