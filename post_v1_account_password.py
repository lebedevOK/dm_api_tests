import requests
import json
from data_for_test.urls import Urls

'''Reset registered user password'''

url = f"{Urls.url_base}/v1/account/password"

payload = json.dumps({
  "login": "<string>",
  "email": "<string>"
})
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
