import requests
import datetime

from data_for_test.urls import Urls
from dm_api_account.models.registration_model import registration_model
from services.dm_api_account import DmApiAccount
def test_post_v1_account():
    api = DmApiAccount(host=Urls.url_base)
    # получается я и тут вызываю функцию registration_model() чтобы json получить
    # и в account_api - что-то явно где-то лишнее?
    json = registration_model()
    response = api.account.post_v1_account(
        json=json
    )

    print(response)
