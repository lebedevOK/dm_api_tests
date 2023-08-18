import datetime
import requests
import json

'''Register new user'''

from data_for_test.urls import Urls
def generate_email():
  now = datetime.datetime.now()
  timestamp = now.strftime("%Y%m%d%H%M%S")
  email = f"user_{timestamp}@qw.ru"
  return email

url = f"{Urls.url_base}/v1/account"
email_gen = generate_email()
login_gen = email_gen[:19]

payload = json.dumps({
  "login": login_gen,
  "email": email_gen,
  "password": "4testMeNow"
  })

headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
print(email_gen)
print(login_gen)