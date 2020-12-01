from .http import Route
from .client import Client
from .slack_http import HTTPClient

class SlackRoute(Route):
    """ This is a custom route class to allow connection to slack API rather than discord API
    """
    BASE = "https://slack.com/api"

    def __init__(self,method, path, **parameters) -> None:
        # super(self,method, path, **parameters)
        super().__init__(method, path, **parameters)

class Slack(Client):
    def __init__(self, *, loop=None, **options) -> None:
        super().__init__(loop=None, **options)
        connector = options.pop('connector', None)
        proxy = options.pop('proxy', None)
        proxy_auth = options.pop('proxy_auth', None)
        unsync_clock = options.pop('assume_unsync_clock', True)
        self.http = HTTPClient(connector, proxy=proxy, proxy_auth=proxy_auth, unsync_clock=unsync_clock, loop=self.loop)
