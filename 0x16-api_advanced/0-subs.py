#!/usr/bin/python3
"""
Queries the Reddit API for the number of subscribers of a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for the specified subreddit.

    Returns:
        int: The number of subscribers of the subreddit.
             Returns 0 if the subreddit is invalid or inaccessible.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-Reddit-Scraper"}  # Custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
