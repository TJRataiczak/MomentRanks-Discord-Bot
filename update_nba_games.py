import requests
import sqlite3
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

conn = sqlite3.connect(os.getenv("NBA_DB"))
c = conn.cursor()

nbastats = requests.get('https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2021/league/00_full_schedule.json')
data = nbastats.json()

c.execute("DELETE FROM games")

for months in data['lscd']:
    for game in months['mscd']['g']:
        print(game['h']['tn'])
        c.execute(f"""INSERT INTO games VALUES ('{game['h']['tn']}','{game['h']['tc']}',
                     '{game['v']['tn']}','{game['v']['tc']}', '{game['gdte']}', '{game['stt']}')""")

conn.commit()
conn.close()

with open("last_update.txt", "w") as f:
    f.write(str(datetime.datetime.today()))