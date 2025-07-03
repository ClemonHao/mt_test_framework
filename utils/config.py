# utils/config.py

BASE_URL = "https://api.sinric.pro/api/v1/devices/{device_id}/action"
BASE_URL_ACTION = "https://api.sinric.pro/api/v1/devices"
AUTH_TOKEN = "67457f7f13f98f1416f589e9"
ACTION_HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/x-www-form-urlencoded",
}
AUTH_API = "https://api.sinric.pro/api/v1/auth"

APP_KEY = "97152e9f-435b-49b2-aad0-188abc51313f"
APP_SECRET = "b056cf95-a61b-419e-bd98-638cbf2d7802-3b8e3386-0d40-4c85-b34a-65166ec05325"
LIGHT_ID = "67457f7f13f98f1416f589e9"
TV_ID = "683e4256929fca430249ceed"
API_KEY = "ecb143fb-2ecb-4471-9353-3f0ae0f4bec0"

AUTH_HEADERS = {
    "x-sinric-api-key": API_KEY,
    "Content-Type": "application/x-www-form-urlencoded",
}
#BASE_URL = config.BASE_URL
#device_id = config.LIGHT_ID
