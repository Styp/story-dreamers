import io
import os

from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join('auth', 'auth/google-vision-key.json')

image_file = os.path.join("images", "008-000.png")

client = vision.ImageAnnotatorClient()
with io.open(image_file, "rb") as image_file:
  content = image_file.read()
  image = vision.Image(content=content)

  response = client.label_detection(image=image)
  labels = response.label_annotations
  print(labels)