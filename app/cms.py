from bs4 import BeautifulSoup
from datetime import datetime
import os
import glob

current_images = []
new_images = []

class load_content:

    def __init__(self, html_file):
        self.html_file = html_file

    def load_current_images(self):
        html_doc = open(self.html_file, "r+")
        soup = BeautifulSoup(html_doc, "html5lib")
        for image in soup.find_all('img'):
            current_images.append(image.attrs['src'])

    def load_new_images(self):
        html_doc = open(self.html_file, "r+")
        soup = BeautifulSoup(html_doc, "html5lib")
        div_happy_images = soup.find('div', {'class' : 'row'})
        content_block = div_happy_images.find_next()
        latest_dir = max(glob.glob(os.path.join('static/happy-images', '*/')),  key=os.path.getmtime)
        images = os.listdir(latest_dir)
        for image in images:
            next_image = soup.new_tag('img')
            next_image.attrs['alt'] = '#'
            next_image.attrs['class'] = 'retrieved-photos'
            next_image.attrs['src'] = '%s%s' % (latest_dir, image)
            new_images.append(next_image)

    def generate_html(self):
        html_doc = open(self.html_file, "r+")
        soup = BeautifulSoup(html_doc, 'html5lib')
        div_happy_images = soup.find('div', {'class' : 'row'})
        content_block = div_happy_images.find_next()
        iterable_images = list(set(new_images) - set(current_images))
        for image in iterable_images:
            content_block.append(image)
        html = soup.prettify('utf-8')
        with open(self.html_file, "wb") as hf:
            hf.write(html)

x = load_content('templates/main.html')
x.load_current_images()
x.load_new_images()
x.generate_html()
