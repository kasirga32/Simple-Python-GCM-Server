from gcm import GCM

# Plain text request

API_KEY = "AIzaSyDfPt_RsXH5UacPfDWbUKLsdswuS5o0FbQ"

gcm = GCM(API_KEY, debug=True)

registration_id = 'dVk8mIZRZzU:APA91bFDoA94RpmAy9eES620I9M5V6aKFHaRFyyPcaxp_ZpUGSKt3nbrKJQlO7OSRw0kAwUCu-es8BlPk3iKBKAJg9XkrvFrmltGUYPH6xb8tdVQehfYt6yXrngm7AEgXTRFjS_y45c_'

data = {'message': 'Test'}

response = gcm.plaintext_request(registration_id=registration_id, data=data)

print(response)
