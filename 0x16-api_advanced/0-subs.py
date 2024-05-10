#!/usr/bin/python3
"""
Queries the Reddit API for the number of subscribers of a given subreddit.
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for the specified subreddit.

    Returns:
        int: The number of subscribers of the subreddit.
             Returns 0 if the subreddit is invalid or inaccessible.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
