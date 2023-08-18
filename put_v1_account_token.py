import requests
from data_for_test.urls import Urls

'''Activate registered user'''

url = f"{Urls.url_base}/v1/account/<uuid>"

payload = {}
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
