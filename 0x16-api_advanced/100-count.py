#!/usr/bin/python3
"""
100-count
"""
import requests
from collections import defaultdict

def count_words(subreddit, word_list, counts=defaultdict(int), after=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        counts (dict): A dictionary to store the counts of each keyword.
        after (str): A token for pagination to retrieve the next page of results.

    Returns:
        None
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
            title = post['data']['title']
            words = title.split()
            for word in words:
                word = word.lower().strip('.,!?')
                if word in word_list:
                    counts[word] += 1

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, counts, after)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())

