#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Retrieves and prints the titles of the first 10 hot posts for a subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}  # Custom User-Agent
    params = {"limit": 10}
    response = requests.get(url, headers=headers, allow_redirects=False, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if posts:
            for post in posts:
                print(post["data"]["title"])
        else:
            print("No posts found for this subreddit.")
    else:
        print("None")

if __name__ == "__main__":
    top_ten("programming")  # For testing purposes