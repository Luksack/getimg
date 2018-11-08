from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import itertools
import uuid
import os


class ImageDownloader():
    def __init__(self, keyword, amount, directory):
        self.keyword = keyword
        self.amount = amount
        self.directory = directory
        self.request_headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        self.run()

    def extract_data(self):
        url = f'https://www.google.co.in/search?q={self.keyword}&source=lnms&tbm=isch'
        response = urlopen(Request(url, headers=self.request_headers))
        soup = BeautifulSoup(response, 'html.parser')

        find_image = soup.find_all('div', {'class': 'rg_meta'})
        collect_json = (json.loads(link.text) for link in find_image)
        link_records = ((d['ou'], d['ity']) for d in collect_json)

        return itertools.islice(link_records, self.amount)

    def get_image(self, url):
        request = Request(url, headers=self.request_headers)
        resp = urlopen(request)
        return resp.read()

    def save_image(self, raw_image, image_type):
        extension = image_type if image_type else 'jpg'
        file_name = f'{str(uuid.uuid4().hex)}.{extension}'
        save_path = os.path.join(self.directory, file_name)
        with open(save_path, 'wb') as image_file:
            image_file.write(raw_image)

    def download_image(self, images):
        for (url, image_type) in images:
            try:
                raw_image = self.get_image(url)
                self.save_image(raw_image, image_type)
            except Exception as e:
                print(e)

    def run(self):
        images = self.extract_data()
        self.download_image(images)
