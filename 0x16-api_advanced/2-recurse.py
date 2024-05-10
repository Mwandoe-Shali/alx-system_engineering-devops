#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves the titles of all hot articles for the subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): containing the titles of hot articles.
        after (str): pagination token for the next page of results.

    Returns:
        list: Containing the titles of all hot articles for subreddit.
              Returns None if no results are found for the given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?
            limit=100&after={after}"
    headers = {"User-Agent": "My-Reddit-Scraper"}  # Custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if posts:
            for post in posts:
                hot_list.append(post["data"]["title"])

            # Get the pagination token for the next page of results
            after = data["data"]["after"]
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    subreddit = "programming"  # Example subreddit
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
