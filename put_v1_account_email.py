import requests
import json
from data_for_test.urls import Urls
'''Change registered user email'''

url = f"{Urls.url_base}/v1/account/email"

payload = json.dumps({
  "login": "<string>",
  "password": "<string>",
  "email": "<string>"
})
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
