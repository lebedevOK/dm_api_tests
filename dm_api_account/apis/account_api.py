import requests
from requests import Response

from ..models.change_email import change_email
from ..models.change_password import change_password
from ..models.registration_model import registration_model
from ..models.reset_password import reset_password
from requests import session

class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        self.session.headers = headers

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """
        # непонятно, надо или нет тут вызывать функцию registration_model()?
        # в registration_model.py нет самостоятельного json'а, лежит эта функция:
        registration_model()
        response = self.session.post(
            url=f'{self.host}/v1/account',
            json=json,
            **kwargs
        )
        return response

    def get_v1_account(self):
        '''
        Get current user
        '''

        response = self.session.get(
            url=f"{self.host}/v1/account",
        )
        return response

    def post_v1_account_password(self, json: reset_password, **kwargs) -> Response:
        '''
        :param json reset_password
        Reset registered user password
        '''

        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response
    def put_v1_account_email(self, json: change_email, **kwargs) -> Response:
        '''
        :param json change_email
        Change registered user email
        '''

        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_password(self, json: change_password, **kwargs) -> Response:
        '''
        :param json change_password
        Change registered user password
        '''

        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_token(self, token):
        '''
        Activate registered user
        '''

        response = self.session.put(
            url=f"{self.host}/v1/account/{token}",
        )
        return response





