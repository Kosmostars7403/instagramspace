import requests
from download_func import download_image


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url).json()
    for pic_number, pic in enumerate(response['links']['flickr_images'], 1):
        download_image(pic, (('./images/spacex{}.jpg').format(pic_number)))

if __name__ == '__main__':
    fetch_spacex_last_launch()