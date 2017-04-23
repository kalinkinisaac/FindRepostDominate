import vk
from .accounts_holder import Accounts

# Init config
Accounts.collect()

# Bot session to create bot_api
com_session = vk.Session(access_token=Accounts.com_token)

# Bot api -- main interface to communicate with vk.com
com_api = vk.API(
    session=com_session,
    v=Accounts.api_config['v'],
    lang=Accounts.api_config['lang'],
    timeout=Accounts.api_config['timeout']
)
