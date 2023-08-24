import requests
import datetime

from data_for_test.urls import Urls
from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host=Urls.url_base)
    response = api.account.put_v1_account_token("c8ab408e-ec72-46d6-bd4e-dadaae0e24a3")

    print(response.text)
