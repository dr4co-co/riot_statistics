from riotwatcher import LolWatcher, ApiError


class LeagueOfLegendsApiConnection():

    def __init__(self, api_key):
        self.watcher = LolWatcher(api_key)

    def get_summoner_stats(self, summoner_name, region):
        return self.watcher.summoner.by_name(region, summoner_name)

    def get_ranked_stats(self, summoner_stats, region):
        return self.watcher.league.by_summoner(region, summoner_stats['id'])

    def get_amount_of_wins_by_gamemode(self, ranked_stats, gamemode):
        return int(ranked_stats[gamemode]['wins'])

    def get_amount_of_losses_by_gamemode(self, ranked_stats, gamemode):
        return int(ranked_stats[gamemode]['losses'])

    def get_amount_of_games_by_gamemode(self, ranked_stats, gamemode):
        return self.get_amount_of_wins_by_gamemode(ranked_stats, gamemode) + self.get_amount_of_losses_by_gamemode(
            ranked_stats, gamemode)

    def get_winrate_by_gamemode(self, ranked_stats, gamemode):
        return int(ranked_stats[gamemode]['wins']) / self.get_amount_of_games_by_gamemode(ranked_stats, gamemode) * 100

    def get_match_history(self, summoner_stats, region):
        return self.watcher.match.matchlist_by_account(region, summoner_stats['accountId'])['matches']

    def get_champ_mastery(self, summoner_stats, region):
        return self.watcher.champion_mastery.by_summoner(region, summoner_stats['id'])