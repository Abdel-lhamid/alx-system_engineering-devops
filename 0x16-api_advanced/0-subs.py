#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """return nb of subscribers for a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'alx-stud-linux'})
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        return 0
    subs = req.json().get('data').get('subscribers')
    if not subs:
        return 0
    return subs
