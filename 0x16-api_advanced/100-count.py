#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the titles of hot articles
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count occurrences of.
        after (str): The pagination token for the next page of results.
        counts (dict): A dictionary to store the counts of keywords.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?\
        limit=100&after={}".format(subreddit, after)
    headers = {"User-Agent": "My-Reddit-Scraper"}  # Custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if posts:
            for post in posts:
                title = post["data"]["title"].lower()
                for word in word_list:
                    # Check if word appears in the title (case-insensitive)
                    if f" {word.lower()} " in f" {title} ":
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1

            # Get the pagination token for the next page of results
            after = data["data"]["after"]
            if after is not None:
                return count_words(subreddit, word_list, after, counts)
            else:
                # Print the sorted count of keywords
                sorted_counts = sorted(counts.items(),
                                       key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return
    else:
        return


if __name__ == "__main__":
    subreddit = "programming"  # Example subreddit
    word_list = ["java", "python", "javascript", "c++"]
    count_words(subreddit, word_list)
