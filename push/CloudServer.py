import requests
import json

GCM_URL = "https://android.googleapis.com/gcm/send"
API_KEY = "AIzaSyDfPt_RsXH5UacPfDWbUKLsdswuS5o0FbQ"
REG_IDS = [
    "dVk8mIZRZzU:APA91bFDoA94RpmAy9eES620I9M5V6aKFHaRFyyPcaxp_ZpUGSKt3nbrKJQlO7OSRw0kAwUCu-es8BlPk3iKBKAJg9XkrvFrmltGUYPH6xb8tdVQehfYt6yXrngm7AEgXTRFjS_y45c_"]

headers = {'content-type': 'application/json', "authorization": "key=" + API_KEY}

data = {
        "sender": "Yunus",
        "date": "2014-08-15 13:26:13",
        "title": "GCM",
        "mesaj": "Deneme",}

post_data = {}

post_data['data'] = data
post_data['registration_ids'] = REG_IDS

post_data_json = json.dumps(post_data)
print(post_data_json)

r = requests.post(GCM_URL, data=post_data_json, headers=headers)
print(r.headers['content-type'])

print(r.status_code)
print(r.text)
