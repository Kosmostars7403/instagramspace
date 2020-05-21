from os import listdir, getenv
from pathlib import Path
import instabot
from PIL import Image
from dotenv import load_dotenv

def get_name(path):
    split_path = (path.replace('/', '.')).split('.')
    return split_path[-2]

def create_instagram_thumbnail(filename):
    name = get_name(filename)
    image = Image.open(filename)
    image.thumbnail((1080, 1080))
    Path("./insta_images").mkdir(parents=True, exist_ok=True)
    rgb = image.convert('RGB')
    rgb.save(("./insta_images/{}.jpg").format(name), format="JPEG")


def upload_images(filename):
    bot = instabot.Bot()
    bot.login(username=LOGIN, password=PASSWORD)
    name = get_name(filename)
    bot.upload_photo(('./insta_images/{}.jpg').format(name), caption="Nice pic!")


if __name__ == '__main__':
    load_dotenv()
    login = getenv('LOGIN')
    password = getenv('PASSWORD')

    images = listdir('images')

    for image in images:
        create_instagram_thumbnail(('./images/{}').format(image))
        upload_images(image)














