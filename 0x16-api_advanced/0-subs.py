#!/usr/bin/python3
"""module queries reddit api"""
import requests


def number_of_subscribers(subreddit):
    """queries reddit api and return number of subscribers"""
    headers = {'User-agent': 'MyAPI/0.0.1'}
    res = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=headers, allow_redirects=False)
    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    return 0
