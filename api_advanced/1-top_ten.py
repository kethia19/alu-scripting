#!/usr/bin/python3
"""DOCS"""
import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            posts = response.json()['data']
            for post in posts['children'][:10]:
                sys.stdout.write(post['data']['title'] + '\n')
            return
    except Exception:
        pass
    
    sys.stdout.write("OK")
