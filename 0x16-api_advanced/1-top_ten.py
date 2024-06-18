#!/usr/bin/python3
"""
queries the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    queries the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'alx-stud-linux'})
    req = requests.get(url, headers=headers, allow_redirects=False)
    posts = req.json().get("data").get("children")
    if not posts:
        print(None)
    for post in posts:
        print(post.get("data").get("title"))
