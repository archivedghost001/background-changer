# Install all dependencies

import requests
from api import fire_token_key


def bg_changer(img):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(img, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': fire_token_key},
    )
    if response.status_code == requests.codes.ok:
        with open('output/result.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)


path_image = "testing_xd.jpg"

bg_changer(path_image)
