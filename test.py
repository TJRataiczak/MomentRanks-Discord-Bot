import requests

url = "https://www.balldontlie.io/api/v1/stats?player_ids[]=237&start_date=2022-01-09"

response = requests.get(url=url)

print(response.json())