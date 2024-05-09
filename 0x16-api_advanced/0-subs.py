def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    try:
        r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                         headers={'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/colomriek)'}).json()
        subs = r.get("data", {}).get("subscribers", 0)
        return subs
    except requests.RequestException as e:
        print("Error fetching subreddit data:", e)
        return 0
