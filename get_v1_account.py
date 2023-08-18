import requests
from data_for_test.urls import Urls

''''Get current user'''

payload = {}
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Accept': 'text/plain'
}

url = f"{Urls.url_base}/v1/account"
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
