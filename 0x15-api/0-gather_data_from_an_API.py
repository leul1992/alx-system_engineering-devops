#!/usr/bin/python3
"""script accepts integer and display employ standard output"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    id_no = argv[1]
    users = requests.get(url + 'users/{}'.format(id_no)).json()
    total_task = requests.get(url + 'todos?userId={}'.format(id_no)).json()
    done_task = requests.get(url + 'todos?userId={}&completed=true'.format
                             (id_no)).json()

    print("Employee {} is done with tasks({}/{}):".format(users.get('name'),
          len(done_task), len(total_task)))
    for to in done_task:
        print('\t' + to.get('title'))
