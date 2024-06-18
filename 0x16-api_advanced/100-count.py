#!/usr/bin/python3
"""
ecursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a sorted count of given keywords
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10&after={}".format(subreddit, after)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'alx-stud-linux'})
    req = requests.get(url, headers=headers, allow_redirects=False)
    try:
        results = req.json()
        if req.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return
    posts = req.json().get("data").get("children")
    after = req.json().get("data").get("after")
    for post in posts:
        hot_list.append(post.get("data").get("title"))
    if after is not None:
        return count_words(subreddit, word_list, hot_list, after)
    word_dict = {}
    for word in word_list:
        word_dict[word.lower()] = 0
    for title in hot_list:
        for word in word_list:
            word_dict[word.lower()] += title.lower().split(' ').count(word.lower())
    for key, value in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        if value != 0:
            print("{}: {}".format(key, value))
    return hot_list
