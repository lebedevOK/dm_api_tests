import requests
from data_for_test.urls import Urls

def del_v1_account_login():
  '''
  Logout as current user
  '''
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
  return response