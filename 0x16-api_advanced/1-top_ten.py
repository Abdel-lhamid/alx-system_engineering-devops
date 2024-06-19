#!/usr/bin/python3
"""
queries the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    queries the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'alx-stud-linux'})
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        print(None)
        return
    posts = req.json().get('data').get('children')
    for post in posts:
        print(post.get('data').get('title'))
