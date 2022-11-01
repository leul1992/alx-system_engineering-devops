#!/usr/bin/python3
"""module that queries the reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """queries the reddit api and returns a list containing the titles
    of all hot article in subreddit
    """
    headers = {'User-agent': 'MyAPI/0.0.1'}
    if after is None:
        return hot_list
    res = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
        subreddit), headers=headers, allow_redirects=False,
        params={'after': after})
    if res.status_code != 200:
        return None
    r = res.json()
    for result in r['data']['children']:
        hot_list.append(result['data']['title'])
    return recurse(subreddit, hot_list, r['data']['after'])
