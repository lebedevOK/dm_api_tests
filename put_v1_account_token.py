import requests
from data_for_test.urls import Urls

'''Activate registered user'''
def put_v1_account_token():
  token = '123'
  url = f"{Urls.url_base}/v1/account/{token}"

  headers = {
    'X-Dm-Auth-Token': '<string>',
    'X-Dm-Bb-Render-Mode': '<string>',
    'Accept': 'text/plain'
  }

  response = requests.request(
    method="PUT",
    url=url,
    headers=headers
  )

  print(response.text)
