import requests
from player import Player

class PlayerReader:
    def __init__(self, season):
        self.base_url = "https://studies.cs.helsinki.fi/nhlstats/"
        self.season = season

    def get_players(self):
        url = f"{self.base_url}{self.season}/players"
        response = requests.get(url).json()
        return [Player(player_dict) for player_dict in response]