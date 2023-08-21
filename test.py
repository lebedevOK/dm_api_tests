import datetime
import requests
from data_for_test.GenDataUser import GenDataUser
from data_for_test.urls import Urls

def post_v1_account():
  """
  Register new user
  """
  url = f"{Urls.url_base}/v1/account"
  now = datetime.datetime.now()
  timestamp = now.strftime("%Y%m%d%H%M%S")
  login_gen = str(timestamp)
  #login_gen = GenDataUser.generate_login()
  email_gen = f"user_{timestamp}@qw.ru"
  #email_gen = GenDataUser.generate_email()

  with open("../emails.txt", "a") as file:
      file.write(email_gen + "\n")

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



