from RiotApi.LeagueOfLegendsApiConnection import LeagueOfLegendsApiConnection


class ChampionAnalyzer():
    def __init__(self, api_key):
        api = LeagueOfLegendsApiConnection(api_key)
