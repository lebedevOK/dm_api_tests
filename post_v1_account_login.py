import requests
import json
from data_for_test.urls import Urls

'''Authenticate via credentials'''

url = f"{Urls.url_base}/v1/account/login"

payload = json.dumps({
  "login": "<string>",
  "password": "<string>",
  "rememberMe": "<boolean>"
})
headers = {
  'X-Dm-Bb-Render-Mode': '<string>',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
