#!/usr/bin/python3
"""Module for task 1"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts of the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print('None')
        return
    
    try:
        json_response = response.json()
    except ValueError:
        print('None')
        return
    
    data = json_response.get("data", {})
    children = data.get("children", [])
    if not children:
        print('None')
        return
    
    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            print(title)
        else:
            print('None')

# Example usage:
# top_ten('python')

