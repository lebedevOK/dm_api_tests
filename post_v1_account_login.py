import requests
from data_for_test.urls import Urls

'''Authenticate via credentials'''
def post_v1_account_login():
  url = f"{Urls.url_base}/v1/account/login"

  payload = {
    "login": "<string>",
    "password": "<string>",
    "rememberMe": "<boolean>"
  }
  headers = {
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
