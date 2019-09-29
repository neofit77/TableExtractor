import json
import requests
from pathlib import Path
from time import sleep


dir_path = Path('image')
images = dir_path.iterdir()

for image in images:
  sleep(10)
  name = image.name[:-4]
  url = 'https://trigger.extracttable.com'
  payload = {'dup_check': 'False'}
  files = {'input': open('{}'.format(image),'rb')}
  headers = {
    'x-api-key': 'bi2EU0vO7Y43vWupTNFFI2zZmdwSBRzp9HcmfwEK'
  }
  response = requests.request('POST', url, headers = headers, data = payload, files = files, allow_redirects=False)
  with open('jsonFiles/{}.json'.format(name),'w') as f:
    f.write(response.text)

