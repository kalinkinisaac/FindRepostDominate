import vk
from .accounts_holder import Accounts


class ApiWrapper(object):

    _api = None

    def __init__(self, login, password):
        print(login)
        session = vk.AuthSession(
            app_id=Accounts.get_app_id(),
            user_login=login,
            user_password=password
        )
        self._api = vk.API(session)

    def __getattr__(self, method_name):
        return self._api.__getattr__(method_name)

    def __call__(self, method_name, **method_kwargs):
        return self._api(**method_kwargs)

