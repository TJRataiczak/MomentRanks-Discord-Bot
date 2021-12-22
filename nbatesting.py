import json
import requests
import datetime
import sqlite3

# today = datetime.date.today()
# today += datetime.timedelta(days=1)

# print(today.strftime('%B %d'))

conn = sqlite3.connect('nba.db')
c = conn.cursor()
# c.execute("CREATE TABLE games (home text, away text, date text, time text)")

# nbastats = requests.get('https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2021/league/00_full_schedule.json')
# data = nbastats.json()
# with open('data.json', 'w') as f:
#     json.dump(data, f)

# with open('data.json', 'r') as f:
    
#     data = json.load(f)
    
#     for months in data['lscd']:
#         for game in months['mscd']['g']:
#             print(game['h']['tn'])
#             c.execute(f"INSERT INTO games (home, away, date, time) VALUES ('{game['h']['tn']}', '{game['v']['tn']}', '{game['gdte']}', '{game['stt']}')")


c.execute("SELECT * FROM games WHERE home = 'Pistons'")

print(c.fetchall())

conn.commit()
conn.close()