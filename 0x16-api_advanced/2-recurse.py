#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): A token for pagination to retrieve the next page of results.

    Returns:
        list: A list containing the titles of all hot articles, or None if no results are found for the given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent header
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

if __name__ == '__main__':
    hot_list = recurse(sys.argv[1])
    if hot_list is not None:
        print(len(hot_list))
    else:
        print("None")

