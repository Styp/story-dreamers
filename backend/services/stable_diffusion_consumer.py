import base64
import re
from io import BytesIO

import requests
from PIL import Image


class StableDiffusionConsumer(object):
    def __init__(self):
        self.session = requests.Session()
        self.url_path = "http://34.122.121.121/predictions"

    def fetch_image(self, text: str):
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
        response = self.session.post(self.url_path, json=data)
        response.raise_for_status()

        for image in response.json().get('output', []):
            yield self.parse_image(image)

    def parse_image(self, image_string: str):
        image_data = re.sub('^data:image/.+;base64,', '', image_string)
        return BytesIO(base64.b64decode(image_data))