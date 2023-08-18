import requests
import json
from data_for_test.urls import Urls
'''Change registered user email'''
def put_v1_account_email():
  url = f"{Urls.url_base}/v1/account/email"

  payload = {
    "login": "<string>",
    "password": "<string>",
    "email": "<string>"
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
