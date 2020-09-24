from RiotApi.LeagueOfLegendsApiConnection import LeagueOfLegendsApiConnection
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def main():
    with open('../assets/api_key.txt', 'r') as file:
        api_key = file.read()

    summoner_name = 'Icathun Saijax'
    region = 'EUW1'
    gamemode = 1

    api = LeagueOfLegendsApiConnection(api_key)
    print('SummonerStats')
    sum_stats = api.get_summoner_stats(summoner_name, region)
    print(sum_stats)
    print('Rankedstats')
    rank_stats = api.get_ranked_stats(sum_stats, region)
    print(rank_stats)
    print('Wins')
    wins = api.get_amount_of_wins_by_gamemode(rank_stats, gamemode)
    print(wins)
    print('Losses')
    losses = api.get_amount_of_losses_by_gamemode(rank_stats, gamemode)
    print(losses)
    print('Total games')
    total_games = api.get_amount_of_games_by_gamemode(rank_stats, gamemode)
    print(total_games)
    print('Winrate')
    winrate = api.get_winrate_by_gamemode(rank_stats, gamemode)
    print(winrate)
    print('Matchhistory')
    match_history = api.get_match_history(sum_stats, region)
    print(match_history)


main()