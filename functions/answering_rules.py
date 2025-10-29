import requests
import json
from config import Config


def update_answer_rule(api_key, user, domain, dnd):
    url = (
        "https://"
        + Config.BASE_URL
        + f"/ns-api/v2/domains/{domain}/users/{user}/answerrules/*"
    )
    payload = {"enabled": "yes", "do-not-disturb": {"enabled": dnd}}

    headers = {"accept": "application/json", "authorization": f"Bearer {api_key}"}

    response = requests.put(url, json=payload, headers=headers)
    if response.status_code != 202:
        raise Exception(
            f"Error: recieved status code {response.status_code} for {user}@{domain}\n{response.text}"
        )
    response_dict = json.loads(response.text)

    return response_dict
