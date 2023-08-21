import requests
from requests import Response
from ..models.auth_credentials import auth_credentials
from requests import session

class LoginApi:
    def __init__(self, host, headers):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)
        #self.session.headers.update(headers) if headers else None

    def post_v1_account_login(self, json: auth_credentials, **kwargs) -> Response:
        '''
        :param json auth_credentials
        Authenticate via credentials
        '''

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json,
            **kwargs
        )
        return response

    def del_v1_account_login(self):
        '''
        Logout as current user
        '''

        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
        )
        return response

    def del_v1_account_login_all(self):
        '''
        Logout from every device
        '''

        response = self.session.delete(
            url=f"{self.host}/v1/account/login/all",
        )
        return response

