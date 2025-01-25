#!/usr/bin/env python3
# fetch_social_media.py
# Will fix this later


import json
import requests

def fetch_social_media_data():
    """
    Fetch data from Twitter, Instagram APIs, and GitHub contributions, and save to a JSON file.
    """
    # Example URLs and API keys (replace with your actual keys)
    twitter_api_url = (
        "https://api.twitter.com/2/tweets?ids=ernest_b_shong"
    )
    instagram_api_url = (
        "https://graph.instagram.com/ernest_b_shong"
        "?fields=id,username&access_token=YOUR_ACCESS_TOKEN"
    )
    github_api_url = (
        "https://api.github.com/repos/bshongwe/bshongwe/commits?author=bshongwe"
    )

    headers = {
        "Authorization": "Bearer YOUR_TWITTER_BEARER_TOKEN"
    }

    try:
        twitter_response = requests.get(twitter_api_url, headers=headers)
        twitter_response.raise_for_status()
        twitter_data = twitter_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Twitter data: {e}")
        twitter_data = {}

    try:
        instagram_response = requests.get(instagram_api_url)
        instagram_response.raise_for_status()
        instagram_data = instagram_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Instagram data: {e}")
        instagram_data = {}

    try:
        github_response = requests.get(github_api_url)
        github_response.raise_for_status()
        github_data = github_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitHub data: {e}")
        github_data = {}

    data = {
        "twitter": twitter_data,
        "instagram": instagram_data,
        "github": github_data,
    }

    with open("social_data.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    fetch_social_media_data()
