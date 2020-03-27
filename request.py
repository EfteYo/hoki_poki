import requests
import json

url = 'https://hokipoki.simplymanage.de/insersession.php'
payload = {'session': 'test'}
r = requests.post(url, json=payload)
print(r.json)