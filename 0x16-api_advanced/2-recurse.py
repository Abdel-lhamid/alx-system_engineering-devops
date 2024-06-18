#!/usr/bin/python3
"""
function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10&after={}".format(subreddit, after)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'alx-stud-linux'})
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        return None
    posts = req.json().get("data").get("children")
    after = req.json().get("data").get("after")
    for post in posts:
        hot_list.append(post.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
