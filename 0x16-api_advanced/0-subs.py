#!/usr/bin/python3
"""
Task: 0
"""


def number_of_subscribers(subreddit):
    """ that is how I get number of subscribers """
    import requests

    infos = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "Custom"},
                            allow_redirects=False)

    if infos.status_code >= 300:
        return 0

    return infos.json().get("data").get("subscribers")
