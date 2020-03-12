import requests

import json

user_id = input('Enter your user id: ')
balance = 0

r = requests.get(url="http://localhost:5000/chain")
chain = r.json()

print('chain: ', chain)