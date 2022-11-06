#!/usr/bin/python3
"""module export data in json format"""
import json
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    id_no = argv[1]
    users = requests.get(url + 'users/{}'.format(id_no)).json()
    todo = requests.get(url + 'todos?userId={}'.format(id_no)).json()
    lists = []
    for to in todo:
        temp = {'task': to.get('title'), 'completed': to.get('completed'),
                'username': users.get('username')}
        lists.append(temp)

    with open(id_no + '.json', 'w') as fi:
        json.dump({id_no: lists}, fi)
