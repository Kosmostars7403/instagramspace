import requests
from download_func import download_image
import argparse
from os import path

def get_extension(url):
    split_url = path.splitext(url)
    return split_url[1]


def fetch_hubble_image(id):
    url = ('http://hubblesite.org/api/v3/image/{}').format(id)
    response = requests.get(url).json()
    image_link = 'http:' + response['image_files'][-1]['file_url']
    filename = ('./images/{}{}').format(str(id), get_extension(image_link))
    download_image(image_link, filename)


def download_hubble_collection(collection_name):
    url = ('http://hubblesite.org/api/v3/images/{}').format(collection_name)
    response = requests.get(url).json()
    for pic in response:
        fetch_hubble_image(pic['id'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скачиваем коллекции фотографий с hubblesite.org')
    parser.add_argument('collection_name', help='Название коллекции')
    args = parser.parse_args()
    collection_name = args.collection_name

    download_hubble_collection(collection_name)
