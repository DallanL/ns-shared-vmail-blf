import requests
import json
from config import Config


def url_encode(string):
    return (
        (
            ((string.replace("]", "%5D")).replace("/", "%2F")).replace("[", "%5B")
        ).replace(":", "%3A")
    ).replace(" ", "%20")


def check_api_key(api_key):
    url = "https://" + Config.BASE_URL + "/ns-api/v2/apikeys/~"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {api_key}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error: Failed to authenticate API Key: {response.status_code}"
        )
    response_dict = json.loads(response.text)
    if response_dict["user-scope"] != "Super User":
        raise Exception(
            f"Error: API Key has insufficient permissions: {response_dict['user-scope']}"
        )
    return response_dict
