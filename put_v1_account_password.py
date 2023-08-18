import requests
import json
from data_for_test.urls import Urls

'''Change registered user password'''
def put_v1_account_password():
  url = f"{Urls.url_base}/v1/account/password"

  payload = {
    "login": "<string>",
    "token": "<uuid>",
    "oldPassword": "<string>",
    "newPassword": "<string>"
  }
  headers = {
    'X-Dm-Auth-Token': '<string>',
    'X-Dm-Bb-Render-Mode': '<string>',
    'Content-Type': 'application/json',
    'Accept': 'text/plain'
  }

  response = requests.request(
    method="PUT",
    url=url,
    headers=headers,
    json=payload)

  print(response.text)
