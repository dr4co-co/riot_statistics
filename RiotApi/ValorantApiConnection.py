from riotwatcher import ValWatcher, ApiError

class LeagueOfLegendsApiConnection():

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.watcher = ValWatcher(apiKey)