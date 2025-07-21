#!/usr/bin/python3
"""
Function that queries the Reddit API to get number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
