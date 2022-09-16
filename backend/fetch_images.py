import base64
import re
from io import BytesIO

import requests
from PIL import Image

session = requests.Session()
url_path = "http://34.122.121.121/predictions"


def fetch_image(text: str):
    data = {
        "input": {
            "prompt": text,
            "width": 512,
            "height": 512,
            "prompt_strength": 0.8,
            "num_outputs": 1,
            "num_inference_steps": 50,
            "guidance_scale": 7.5,
            "seed": 0
        }
    }
    response = session.post(url_path, json=data)
    response.raise_for_status()

    for image in response.json().get('output', []):
        yield parse_image(image)


def parse_image(image_string: str):
    image_data = re.sub('^data:image/.+;base64,', '', image_string)
    return Image.open(BytesIO(base64.b64decode(image_data)))
