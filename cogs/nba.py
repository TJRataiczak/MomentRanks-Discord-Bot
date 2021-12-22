from nextcord.ext import commands
from nextcord import Embed
from dotenv import load_dotenv
import os
import sqlite3
import datetime


class Nba(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nba(self, ctx, *arg):
        
        #Setup today's date and week
        today = datetime.date.today()
        week = [today + datetime.timedelta(days=x) for x in range(7)]

        #Initial connection to database
        conn = sqlite3.connect(os.getenv("NBA_DB"))
        c = conn.cursor()

        #Initialize embed
        embed = Embed(color=14167442)
        embed.set_author(name="Shot Talkin'",url= "https://twitter.com/ShotTalkin/", icon_url=os.getenv("SHOT_TALKIN_LOGO"))
        
        games = []

        if arg != ():
            
            #Search database for all games of the team given in the command
            team_to_search = " ".join(arg).title()
            for day_of_week in week:
                c.execute(f"SELECT * FROM games WHERE (home = '{team_to_search}' OR away = '{team_to_search}') AND date = '{day_of_week}'")
                for item in c.fetchall():
                    games.append(item)
            
            #Add games to the embed
            for game in games:
                game_full_date = game[2].split("-")
                date_of_game = datetime.date(int(game_full_date[0]), int(game_full_date[1]), int(game_full_date[2]))
                embed.add_field(name=f"{game[0]} vs {game[1]}", value=f"{date_of_game.strftime('%A')} @ {game[3]}")

            embed.title = f"NBA Schedule for {today.strftime('%B %d')} - {week[-1].strftime('%B %d')}"

        else:
            #Search database for every game on the current day
            c.execute(f"SELECT * FROM games WHERE date = '{today}'")
            for item in c.fetchall():
                games.append(item)
            
            #Add games to the embed
            for game in games:
                embed.add_field(name=f"{game[0]} vs {game[1]}", value=f"{game[3]}")
            
            embed.title = f"NBA Schedule for {today.strftime('%B %d')}"

        embed.url = "https://www.nba.com/schedule"
        await ctx.send(embed=embed)

        conn.close()

def setup(bot):
    bot.add_cog(Nba(bot))
    load_dotenv()