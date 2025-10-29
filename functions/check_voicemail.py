import requests
import json
from functions.utility import url_encode
from config import Config


def check_voicemail(api_key, user, domain, folder="new"):
    url = (
        "https://"
        + Config.BASE_URL
        + f"/ns-api/v2/domains/{domain}/users/{user}/voicemails/{folder}/count"
    )

    headers = {"accept": "application/json", "authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error: recieved status code {response.status_code} for {user}@{domain}\n{response.text}"
        )
    response_dict = json.loads(response.text)

    return response_dict
