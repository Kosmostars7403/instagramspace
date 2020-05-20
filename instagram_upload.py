from os import listdir, getenv
from pathlib import Path
import instabot
from PIL import Image
from dotenv import load_dotenv

def instagram_thumbnail(filename):
    name = (filename.replace('/', '.')).split('.')
    image = Image.open(filename)
    image.thumbnail((1080, 1080))
    Path("./insta_images").mkdir(parents=True, exist_ok=True)
    rgb = image.convert('RGB')
    rgb.save(("./insta_images/{}.jpg").format(name[-2]), format="JPEG")


def upload_images(filename):
    bot = instabot.Bot()
    bot.login(username=LOGIN, password=PASSWORD)
    name = (filename.replace('/', '.')).split('.')
    bot.upload_photo(('./insta_images/{}.jpg').format(name[-2]), caption="Nice pic!")


if __name__ == '__main__':
    load_dotenv()
    LOGIN = getenv('LOGIN')
    PASSWORD = getenv('PASSWORD')

    images = listdir('images')

    for image in images:
        instagram_thumbnail(('./images/{}').format(image))
        upload_images(image)














