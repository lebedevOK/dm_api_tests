import requests
import json
from data_for_test.urls import Urls

'''Change registered user password'''

url = f"{Urls.url_base}/v1/account/password"

payload = json.dumps({
  "login": "<string>",
  "token": "<uuid>",
  "oldPassword": "<string>",
  "newPassword": "<string>"
})
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
