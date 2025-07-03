import requests
from utils.config import BASE_URL, AUTH_HEADERS, ACTION_HEADERS, BASE_URL_ACTION, LIGHT_ID

def perform_action(device_id, query):
    url = f"{BASE_URL}/{device_id}/action?{query}"
    print(url)
    response = requests.get(url, headers=ACTION_HEADERS)
    return response

def authenticate(payload):
    url = f"{BASE_URL}/auth"
    response = requests.post(url, headers=AUTH_HEADERS, data=payload)
    return response
