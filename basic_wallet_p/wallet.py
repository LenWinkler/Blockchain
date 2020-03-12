import requests

import json

user_id = input('Enter your user id: ')
balance = 0

r = requests.get(url='http://localhost:5000/chain')

raw_chain = r.json()
# convert to str
str_chain = json.dumps(raw_chain['chain'])
# convert to json
json_chain = json.loads(str_chain)


for block in json_chain:
    
    if len(block['transactions']) > 0:
        transactions = block['transactions']
        for item in transactions:
            print('item', item)
            if item['recipient'] == user_id or item['recipient'] == user_id + '\n':
                balance += int(item['amount'])

print(f'Your account balance is {balance} coin(s)')