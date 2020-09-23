from RiotApi.LeagueOfLegendsApiConnection import LeagueOfLegendsApiConnection
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def Main():
    with open('../assets/api_key.txt', 'r') as file:
        apiKey = file.read()

    summonerName = 'Icathun Saijax'
    region = 'EUW1'
    gamemode = 1

    api = LeagueOfLegendsApiConnection(apiKey)
    print('SummonerStats')
    sumStats = api.getSummonerStats(summonerName, region)
    print(sumStats)
    print('Rankedstats')
    rankStats = api.getRankedStats(sumStats, region)
    print(rankStats)
    print('Wins')
    wins = api.getAmountOfWinsByGamemode(rankStats, gamemode)
    print(wins)
    print('Losses')
    losses = api.getAmountOfLossesByGamemode(rankStats, gamemode)
    print(losses)
    print('Total games')
    totalGames = api.getAmountOfGamesByGamemode(rankStats, gamemode)
    print(totalGames)
    print('Winrate')
    winrate = api.getWinrateByGamemode(rankStats, gamemode)
    print(winrate)
    print('Matchhistory')
    matchhistory = api.getMatchHistory(sumStats, region)
    print(matchhistory)

Main()