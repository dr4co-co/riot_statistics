from RiotApi.LeagueOfLegendsApiConnection import LeagueOfLegendsApiConnection

def Main():
    with open('pfad', 'r') as file:
        apiKey = file.read()

    api = LeagueOfLegendsApiConnection(apiKey)
    print(api.getSummonerStats('Dr4co', 'EUW1'))

Main()