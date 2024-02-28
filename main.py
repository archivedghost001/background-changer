# Install all dependencies

import requests
from api import fire_token_key
from datetime import datetime
import sys


def bg_changer(img, bg_color):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(img, 'rb')},
        data={'size': 'auto', 'bg_color': bg_color},
        headers={'X-Api-Key': fire_token_key},
    )
    if response.status_code == requests.codes.ok:
        with open('output/result-%s.png' % datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)


# path_image = sys.argv[1]
path_image = str(input("Enter image path: "))
color_name = str(input("Enter color code: "))

bg_changer(path_image, color_name)
