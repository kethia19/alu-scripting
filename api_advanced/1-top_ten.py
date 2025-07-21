#!/usr/bin/python3
"""
This module defines a function to query the Reddit API and print
the titles of the top 10 hot posts for a given subreddit.
If the subreddit is invalid or inaccessible, it prints "OK".
"""

import requests


def top_ten(subreddit):
    """Print top 10 hot post titles or 'OK' if subreddit is invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
            return
    except Exception:
        pass
    print("OK")
