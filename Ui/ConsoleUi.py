from RiotApi.LeagueOfLegendsApiConnection import LeagueOfLegendsApiConnection
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def Main():
    with open('../assets/api_key.txt', 'r') as file:
        apiKey = file.read()

    api = LeagueOfLegendsApiConnection(apiKey)
    print(api.getSummonerStats('Dr4co', 'EUW1'))

Main()