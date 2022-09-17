import os

from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join('auth', 'auth/google-vision-key.json')


client = vision.ImageAnnotatorClient()
response = client.annotate_image({
  'image': {'source': {'image_uri': 'gs://my-test-bucket/image.jpg'}},
  'features': [{'type_': vision.Feature.Type.FACE_DETECTION}]
})

print(response)