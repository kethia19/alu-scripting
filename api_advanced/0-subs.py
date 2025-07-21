#!/usr/bin/python3
"""
Function that queries the Reddit API to get number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    # """Return the number of subscribers """
    """
    Returns the number of subscribers.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
