#!/usr/bin/python3
"""
task 1
"""


def top_ten(subreddit):
    """
    that is how I get the top 10 hot posts of the subreddit
    """
    import requests

    infos = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit), headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if infos.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in infos.json().get("data").get("children")]
