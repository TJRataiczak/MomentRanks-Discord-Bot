import requests
import datetime
import sqlite3
import time

# def mostPoints(item):
#     return item[2]

# now = datetime.datetime.now()
# time_to_check = now.replace(hour= 10, minute=0,second=0,microsecond=0)
# page = 0

# if now > time_to_check:
#     date = datetime.date.today()
# else:
#     date = datetime.date.today() - datetime.timedelta(days=1)

# conn = sqlite3.connect("basketball.db")
# c = conn.cursor()

# c.execute("CREATE TABLE player_stats (first_name text, last_name text, assists integer, blocks integer, rebounds integer, steals integer, points integer, free_throws_made integer, free_throws_attempted integer, three_points_made integer, three_points_attempted integer, date text)")

# c.execute(f"DELETE FROM player_stats WHERE date = '{date}'")

# while page != None:
#     url = f"https://www.balldontlie.io/api/v1/stats?start_date=2022-01-10&end_date=2022-01-11&page={page}&per_page=100"

#     response = requests.get(url=url)
#     response_json = response.json()

#     for game in response_json["data"]:
#         print(game["player"]["first_name"])
#         print(game["player"]["last_name"])
        # c.execute(f"""INSERT INTO player_stats (first_name, last_name, assists, blocks, rebounds, steals, points, free_throws_made, free_throws_attempted, three_points_made, three_points_attempted, date)
        #             VALUES ("{game['player']['first_name']}", "{game['player']['last_name']}", {game['ast']}, {game['blk']}, {game['reb']}, {game['stl']}, {game['pts']}, {game['ftm']}, {game['fta']}, {game['fg3m']}, {game['fg3a']}, "{date}")""")
        
    # page = response_json["meta"]["next_page"]

# c.execute(f"SELECT first_name, last_name, points FROM player_stats WHERE first_name = 'Khris'")

# data = c.fetchall()

# data.sort(key=mostPoints, reverse=True)

# print(data)

# conn.commit()
# conn.close()


response = requests.get(url = "https://www.balldontlie.io/api/v1/stats?player_ids[]=140&seasons[]=2021&page=2")
response_json = response.json()

print(response_json["data"])

for game in response_json["data"]:
    print(game['game']['date'])