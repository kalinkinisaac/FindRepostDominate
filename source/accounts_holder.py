import json

# TODO: exceptions

class AccountsError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
         return repr(self.value)


class Accounts:
    com_token = None
    app_id = None

    config_path = 'config/config.cfg'
    accounts_path = 'accounts/accounts.acc'
    api_config = None

    @staticmethod
    def collect():
        # Debug
        config_file = open(Accounts.config_path)
        config_dict = dict(json.loads(config_file.read()))
        accounts_file = open(Accounts.accounts_path)
        accounts_dict = dict(json.loads(accounts_file.read()))

        app_config = config_dict['app']
        community = config_dict['community']
        api_config = config_dict['api']

        actors = accounts_dict['actors']
        army = accounts_file['army']

        Accounts.com_token = community['token']
        Accounts.app_id = app_config['id']



