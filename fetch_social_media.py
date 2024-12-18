#!/usr/bin/env python3
# fetch_social_media.py

import json
import requests


def fetch_social_media_data():
    """
    Fetch data from Twitter and Instagram APIs and save to a JSON file.
    """
    # Example URLs and API keys
    twitter_api_url = (
        "https://api.twitter.com/2/tweets?ids=YOUR_TWEET_ID"
    )
    instagram_api_url = (
        "https://graph.instagram.com/YOUR_USER_ID"
        "?fields=id,username&access_token=YOUR_ACCESS_TOKEN"
    )

    twitter_response = requests.get(twitter_api_url)
    instagram_response = requests.get(instagram_api_url)

    data = {
        "twitter": twitter_response.json(),
        "instagram": instagram_response.json(),
    }

    with open("social_data.json", "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    fetch_social_media_data()
