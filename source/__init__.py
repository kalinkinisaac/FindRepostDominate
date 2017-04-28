
from . import accounts_holder
from source import storage
# Init config
accounts_holder.Accounts.collect()

# Bot session to create bot_api
#com_session = vk.Session(access_token=Accounts.com_token)

# Bot api -- main interface to communicate with vk.com
# com_api = vk.API(
#     session=com_session,
#     v=Accounts.api_config['v'],
#     lang=Accounts.api_config['lang'],
#     timeout=Accounts.api_config['timeout']
# )
serg_api_wrap = storage.ApiWrapper(accounts_holder.Accounts.actors['name1']['user_login'], accounts_holder.Accounts.actors['name1']['user_password'])