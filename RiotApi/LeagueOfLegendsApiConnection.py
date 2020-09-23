from riotwatcher import LolWatcher, ApiError

class LeagueOfLegendsApiConnection():

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.watcher = LolWatcher(apiKey)

    def getSummonerStats(self, summonerName, region):
        return self.watcher.summoner.by_name(region, summonerName)

    def getRankedStats(self, summonerStats, region):
        return self.watcher.league.by_summoner(region, summonerStats['id'])

    def getAmountOfWinsByGamemode(self, rankedStats, gamemode):
        return int(rankedStats[gamemode]['wins'])

    def getAmountOfLossesByGamemode(self, rankedStats, gamemode):
        return int(rankedStats[gamemode]['losses'])

    def getAmountOfGamesByGamemode(self, rankedStats, gamemode):
        return self.getAmountOfWinsByGamemode(rankedStats, gamemode) + self.getAmountOfLossesByGamemode(rankedStats, gamemode)

    def getWinrateByGamemode(self, rankedStats, gamemode):
        return (int(rankedStats[gamemode]['wins']) / self.getAmountOfGamesByGamemode(rankedStats, gamemode) * 100)

    def getMatchHistory(self, summonerStats, region):
        return self.watcher.match.matchlist_by_account(region, summonerStats['accountId'])['matches']