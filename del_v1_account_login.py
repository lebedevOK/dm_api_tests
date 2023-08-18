import requests
from data_for_test.urls import Urls

'''Logout as current user'''

url = f"{Urls.url_base}/v1/account/login"

payload = {}
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Accept': 'text/plain'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
