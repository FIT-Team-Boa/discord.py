from .http import Route

class SlackRoute(Route):
    """ This is a custom route class to allow connection to slack API rather than discord API
    """
    BASE = "https://slack.com/api"

    def __init__(self,method, path, **parameters) -> None:
        # super(self,method, path, **parameters)
        super().__init__(method, path, **parameters)

