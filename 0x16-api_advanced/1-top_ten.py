#!/usr/bin/python3
"""module queries reddit api"""
import requests


def top_ten(subreddit):
    """queries reddit api and prints the title of the first
    10 hot posts listed
    """
    headers = {'User-agent': 'MyAPI/0.0.1'}
    res = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
        subreddit), headers=headers, allow_redirects=False,
        params={'limit': '10'})
    if res.status_code == 200:
        for r in res.json().get('data').get('children'):
            print(r['data']['title'])
    return None
