import vk, urllib, json
from . import com_api_wrap

class ComCore:

    _dialogs = None

    @staticmethod
    def init():
        pass

    @staticmethod
    def start_lp():
        pass


class LongPollServer:
    template_link = 'https://{}?act=a_check&key={}&ts={}&wait=25&mode=2&version=1'
    raw_long_poll_server = None

    @staticmethod
    def update():
        LongPollServer.raw_long_poll_server = com_api_wrap.messages.getLongPollServer()


    @staticmethod
    def get_link():
        LongPollServer.update()
        return LongPollServer.template_link.format(
            LongPollServer.raw_long_poll_server['server'],
            LongPollServer.raw_long_poll_server['key'],
            LongPollServer.raw_long_poll_server['ts']
        )

    @staticmethod
    def get_page():
        raw_page = urllib.request.urlopen(LongPollServer.get_link())
        page = json.loads(raw_page.read().decode())
        return page

