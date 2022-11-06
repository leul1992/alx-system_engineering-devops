#!/usr/bin/python3
"""module export all task data in json format"""
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users/').json()
    lists = {}
    for user in users:
        id_no = user.get('id')
        lists[id_no] = []
        todo = requests.get(url + 'todos?userId={}'.format(id_no)).json()
        for to in todo:
            temp = {'username': user.get('username'),
                    'task': to.get('title'), 'completed': to.get('completed')}
            lists[id_no].append(temp)
    with open('todo_all_employees.json', 'w') as fi:
        json.dump(lists, fi)
