import requests
from data_for_test.urls import Urls

''''Get current user'''
def get_v1_account():

  headers = {
    'X-Dm-Auth-Token': '<string>',
    'X-Dm-Bb-Render-Mode': '<string>',
    'Accept': 'text/plain'
  }

  url = f"{Urls.url_base}/v1/account"
  response = requests.request(
    method="GET",
    url=url,
    headers=headers
  )

  print(response.text)
