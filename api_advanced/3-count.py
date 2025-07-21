#!/usr/bin/python3
"""
Recursive function to count keyword occurrences in Reddit hot post titles
"""

import requests


def count_words(subreddit, word_list, after="", hot_titles=[], counter={}):
    """Recursively count keywords in hot titles of a subreddit"""

    if after is None and not hot_titles:
        # Normalize keywords to lowercase and count duplicates
        lc_words = [word.lower() for word in word_list]
        for word in lc_words:
            counter[word] = counter.get(word, 0)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'limit': 100, 'after': after}

    try:
        res = requests.get(url, headers=headers, params=params)
        if res.status_code != 200:
            return

        data = res.json().get('data', {})
        children = data.get('children', [])

        for post in children:
            title = post.get('data', {}).get('title', "").lower().split()
            for word in title:
                cleaned = ''.join(c for c in word if c.isalnum())
                if cleaned in counter:
                    counter[cleaned] += 1

        next_after = data.get('after')
        if next_after:
            return count_words(subreddit, word_list, after=next_after, hot_titles=hot_titles, counter=counter)
        else:
            # Sorting and printing
            results = [(word, count) for word, count in counter.items() if count > 0]
            results.sort(key=lambda x: (-x[1], x[0]))
            for word, count in results:
                print(f"{word}: {count}")

    except Exception:
        return
    
    
if __name__ == '__main__':
    count_words("hello", ['REDDIT', 'german', 'HI', 'whynot'])
    count_words('unpopular', ['down', 'vote', 'downvote',
                              'you', 'her', 'unpopular', 'politics'])
    count_words("hello", ['hello', 'hello', 'hello'])
    count_words("unpopular", ["react", "python", "java",
    "javascript", "scala", "no_result_for_this"])
