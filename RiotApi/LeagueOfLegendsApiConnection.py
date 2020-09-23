from riotwatcher import LolWatcher, ApiError

class LeagueOfLegendsApiConnection():

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.watcher = LolWatcher(apiKey)

    def getSummonerStats(self, summonerName, region):
        return self.watcher.summoner.by_name(region, summonerName)

    def getRankedStats(self, summonerStats, region):
        return self.watcher.league.by_summoner(region, summonerStats['id'])

    def getAmountOfGamesByGamemode(self, rankedStats, gamemode):
        return (int(rankedStats[gamemode]['wins']) + int(rankedStats[gamemode]['losses']))

    def getWinrateByGamemode(self, rankedStats, gamemode):
        return (int(rankedStats[gamemode]['wins']) / self.getAmountOfGamesByGamemode(rankedStats, gamemode) * 100)

    def getMatchList(self):
        pass