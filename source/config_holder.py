import json


class ConfigError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
         return repr(self.value)


class Config:
    bot_login = None
    bot_password = None
    app_id = None

    config_path = 'config/config.cfg'

    api_config = None

    @staticmethod
    def collect():
        # Debug
        tokens_file = open(Config.config_path)
        tokens_dict = dict(json.loads(tokens_file.read()))

        app_config = tokens_dict['app']
        credentials = tokens_dict['credentials']
        api_config = tokens_dict['api']

        if 'user_login' in credentials.keys():
            Config.bot_login = tokens_dict['user_token']
        else:
            raise ConfigError('There is not bot_token in config.cfg')

        if 'user_token' in credentials.keys():
            Config.bot_password = tokens_dict['user_token']
        else:
            raise ConfigError('There is not bot_token in config.cfg')

        if 'app_id' in app_config.keys():
            Config.app_id = tokens_dict['app_id']
        else:
            raise ConfigError('There is not app_id in config.cfg')



