from nba_api.stats.endpoints import scoreboardv2, boxscoretraditionalv2
from nba_api.stats.static import players
import requests
import json

# data = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id="0022100626").get_json()

# data = player_game.get_json()

data = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id="0022100625").data_sets

# data = scoreboardv2.ScoreboardV2().get_json()

# data_json = json.loads(data)

# points = []

print(data[0].get_json())

# for stuff in data_json["data"]:
#     print(stuff)



# print(players.find_players_by_last_name("james"))

# print(players.get_active_players())