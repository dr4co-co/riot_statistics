from riotwatcher import ValWatcher, ApiError


class LeagueOfLegendsApiConnection():

    def __init__(self, api_key):
        self.watcher = ValWatcher(api_key)
