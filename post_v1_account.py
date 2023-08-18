import datetime
import requests
import json
from data_for_test.urls import Urls

'''Register new user'''


def generate_email():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    email = f"user_{timestamp}@qw.ru"
    return email

def post_v1_account():
  url = f"{Urls.url_base}/v1/account"
  email_gen = generate_email()
  login_gen = email_gen[:19]

  payload = {
      "login": login_gen,
      "email": email_gen,
      "password": "4testMeNow"
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
      json=payload
  )
  print(email_gen)
  return response

response = post_v1_account()
print(response.status_code)



