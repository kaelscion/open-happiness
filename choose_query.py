from bs4 import BeautifulSoup
from app import db, models
import time, os, requests, shutil, random

class data_miner:

    urls = []
    query = ''

    def __init__(self, base_url):
        self.base_url = base_url

    def get_query(self):
        adjectives = models.Adjectives.query.all()
        positives = models.Positive.query.all()

        rand_selector_adj = random.randint(1, len(adjectives))
        rand_selector_pos = random.randrange(1, len(positives))

        selected_adj = models.Adjectives.query.get(rand_selector_adj)
        selected_pos = models.Positive.query.get(rand_selector_pos)
        self.query = str(selected_adj.adjective) + ' ' + str(selected_pos.category)

    def get_links(self, query):
        html=self.base_url
        print self.query
        payload={'q': query}
        r=requests.get(html, params=payload)
        soup=BeautifulSoup(r.content, "html5lib")
        for image in soup.find_all('img'):
            self.urls.append(image.attrs['src'])

    def download_files(self, query):
        number = 1
        new_directory = 'app/static/happy-images/%s%s' % (query, time.strftime("%m%y%I%M"))
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        for item in self.urls:
            with open('%s/%s%s.jpg' % (new_directory, query, str(number) ), 'wb') as out_file:
                req = requests.get(item, stream=True)
                shutil.copyfileobj(req.raw, out_file)
                number += 1

x = data_miner('http://www.google.com/images')
x.get_query()
x.get_links(x.query)
x.download_files(x.query)
