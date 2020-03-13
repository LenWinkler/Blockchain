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
users_transactions = []

def print_transactions(transactions):
    for item in transactions:
        print(f'\n{item}\n')

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
            # add relevant transactions to users_transactions
            if item['recipient'] == user_id or item['sender'] == user_id:
                users_transactions.append(item)
            # if user is recipient in this transaction, amount to balance
            if item['recipient'] == user_id or item['recipient'] == user_id + '\n':
                balance += int(item['amount'])

print(f'{user_id}\'s account balance is {balance} coin(s)\n')
print(f'{user_id}\'s transactions: \n')
print_transactions(users_transactions)
print('\n')