import requests
import datetime

from data_for_test.urls import Urls
from dm_api_account.models.registration_model import registration_model
from data_for_test import generation_users
from services.dm_api_account import DmApiAccount
def test_post_v1_account():
    api = DmApiAccount(host=Urls.url_base)
    json = registration_model()
    #json = generation_users()
    response = api.account.post_v1_account(
        json=json
    )

    print(response)
