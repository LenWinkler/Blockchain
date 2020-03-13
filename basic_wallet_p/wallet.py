import requests

import json

# load id
i = open('user_id.txt', 'r')
user_id = i.read()
i.close()

if user_id == '':
    user_id = input('Enter your user id: ')
    i = open('user_id.txt', 'w')
    i.write(user_id)
    i.close()
else:
    returning_user = input(f'Are you {user_id}? (y/n): ')
    if returning_user == 'n':
        user_id = input('Enter your user id: ')
        i = open('user_id.txt', 'w')
        i.write(user_id)
        i.close()
# balance counter
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

print(f'{user_id}\'s account balance is {balance} coin(s)')