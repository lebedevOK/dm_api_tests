import requests
import json
from data_for_test.urls import Urls

'''Reset registered user password'''
def post_v1_account_password():
  url = f"{Urls.url_base}/v1/account/password"

  payload = {
    "login": "<string>",
    "email": "<string>"
  }
  headers = {
    'X-Dm-Auth-Token': '<string>',
    'X-Dm-Bb-Render-Mode': '<string>',
    'Content-Type': 'application/json',
    'Accept': 'text/plain'
  }

  response = requests.request(
    method="POST",
    url=url,
    headers=headers,
    json=payload)

  print(response.text)
