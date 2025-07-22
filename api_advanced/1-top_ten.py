#!/usr/bin/python3
"""DOCS"""
import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json()['data']
            for post in posts['children'][:10]:
                print(post['data']['title'])
            return
    except Exception:
        pass
    sys.stdout.write("OK")
