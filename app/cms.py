from bs4 import BeautifulSoup
from datetime import datetime
import os

class load_content:

    def __init__(self, html_file):
        self.html_file = html_file

    def load_images(self):
        html_doc = open(self.html_file, "r+")
        soup = BeautifulSoup(html_doc, "html5lib")
        div_happy_images = soup.find('div', {'class' : 'row'})
        content_block = div_happy_images.find_next()
        images = os.listdir("static/happy-images")
        for image in images:
            next_image = soup.new_tag('img')
            next_image.attrs['alt'] = '#'
            next_image.attrs['class'] = 'retrieved-photos'
            next_image.attrs['src'] = "/static/happy-images/" + str(image)
            content_block.append(next_image)
        html_doc.close()
        html = soup.prettify('utf-8')
        with open(self.html_file, "wb") as hf:
            hf.write(html)

x = load_content('templates/main.html')
x.load_images()
