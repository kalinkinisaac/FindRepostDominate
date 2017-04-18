import vk
from .config_holder import Config

# Init config
Config.collect()

# Bot session to create bot_api
bot_session = vk.AuthSession(
    app_id=Config.app_id,
    user_login=Config.bot_login,
    user_password=Config.bot_password
)

# Bot api -- main interface to communicate with vk.com
bot_api = vk.API(
    session=bot_session,
    v=Config.api_config['v'],
    lang=Config.api_config['lang'],
    timeout=Config.api_config['timeout']
)
