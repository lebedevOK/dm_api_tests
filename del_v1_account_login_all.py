import requests
from data_for_test.urls import Urls

'''Logout from every device'''
def del_v1_account_login_all():
  url = f"{Urls.url_base}/v1/account/login/all"

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
