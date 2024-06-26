#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the titles of all hot articles for the subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): containing the titles of hot articles.

    Returns:
        list: Containing the titles of all hot articles for subreddit.
              Returns None if no results are found for the given subreddit.
    """
    global after
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
