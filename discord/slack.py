from .http import Route
from .client import Client
from .slackhttp import HTTPClient

class SlackRoute(Route):
    """ This is a custom route class to allow connection to slack API rather than discord API
    """
    BASE = "https://slack.com/api"

    def __init__(self,method, path, **parameters) -> None:
        # super(self,method, path, **parameters)
        super().__init__(method, path, **parameters)

class Slack(Client):
    def __init__(self, *, loop=None, **options) -> None:
        super().__init__(self, loop=None, **options)
        self.http = HTTPClient(super().connector, proxy=super().proxy, proxy_auth=super().proxy_auth, unsync_clock=super().unsync_clock, loop=self.loop)
