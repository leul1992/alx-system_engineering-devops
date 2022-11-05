#!/usr/bin/python3
"""module to export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    id_no = argv[1]
    todo = requests.get(url + 'todos?userId={}'.format(id_no)).json()
    user = requests.get(url + 'users/{}'.format(id_no)).json()
    with open(id_no + '.csv', 'w', newline='') as fi:
        writer = csv.writer(fi, quoting=csv.QUOTE_ALL)
        for to in todo:
            writer.writerow([user.get('id'), user.get('username'),
                             to.get('completed'), to.get('title')])
