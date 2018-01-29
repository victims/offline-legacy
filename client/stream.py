import requests
import json

r = requests.get('http://victi.ms/service/v2/remove/1970-01-01T00:00:00/', stream=True)
with open('update.out', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
