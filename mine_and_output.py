from bs4 import BeautifulSoup
import requests
import shutil

urls = []
<<<<<<< HEAD
query = 'katmandu'
=======
query = 'puppies'
>>>>>>> d0f0f74a433dd16a2e47f2b50cda38bc4f0f1490

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
<<<<<<< HEAD

    def download_files(self, query):
        number = 1
        for item in urls:
            with open('app/static/happy-images/' + query + str(number) + '.jpg', 'wb') as out_file:
                req = requests.get(item, stream=True)
                shutil.copyfileobj(req.raw, out_file)
                number += 1

x = data_miner('http://www.google.com/images')
x.get_links(query)
x.download_files(query)
=======
    
    def download_files(self, query):
        number = 1
        for item in urls:
            with open('static/happy-images/' + query + str(number) + '.jpg', 'wb') as out_file:
                req = requests.get(item, stream=True)
                shutil.copyfileobj(req.raw, out_file)
                number += 1
    
x = data_miner('http://www.google.com/images')
x.get_links(query)
x.download_files(query)
            
                
>>>>>>> d0f0f74a433dd16a2e47f2b50cda38bc4f0f1490
