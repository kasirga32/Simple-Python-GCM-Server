import requests
import json

GCM_URL = "https://android.googleapis.com/gcm/send"
# Set your API_KEY HERE
API_KEY = "AIzaSyDfPt_RsXH5UacPfDWbUKLsdswuS5o0FbQ"
# Put your tokens, can be multiple
REG_IDS = [
    "dVk8mIZRZzU:APA91bFDoA94RpmAy9eES620I9M5V6aKFHaRFyyPcaxp_ZpUGSKt3nbrKJQlO7OSRw0kAwUCu-es8BlPk3iKBKAJg9XkrvFrmltGUYPH6xb8tdVQehfYt6yXrngm7AEgXTRFjS_y45c_"]

headers = {'content-type': 'application/json', "authorization": "key=" + API_KEY}

# Add tag and data e.g. "subtitle": "This is a subtitle"
data = {
    "sender": "Yunus",
    "date": "2016-04-12 10:23:13",
    "title": "GCM",
    "message": "Push Notification Test",}
post_data = {}

post_data['data'] = data
post_data['registration_ids'] = REG_IDS

# Converting data to JSON
post_data_json = json.dumps(post_data)
print(post_data_json)

# Send POST request to GCM
r = requests.post(GCM_URL, data=post_data_json, headers=headers)
print(r.headers['content-type'])
print(r.status_code)
print(r.text)
