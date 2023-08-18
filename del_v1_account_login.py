import requests
from data_for_test.urls import Urls

'''Logout as current user'''
def del_v1_account_login():
  url = f"{Urls.url_base}/v1/account/login"

  headers = {
    'X-Dm-Auth-Token': '<string>',
    'X-Dm-Bb-Render-Mode': '<string>',
    'Accept': 'text/plain'
  }

  response = requests.request(
    method="DELETE",
    url=url,
    headers=headers
  )

  print(response.text)
