#!/usr/bin/python3
"""
This module defines a function to query the Reddit API and print
the titles of the top 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    If the subreddit is invalid or inaccessible, prints 'None'.
    """
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
        print(None)
    print("OK")
