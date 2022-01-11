from nextcord.ext import commands
from nextcord import Embed
from dotenv import load_dotenv
import os
import sqlite3
import datetime


class Nba(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Shows games for the day, nba (team/city) Shows games for the next week for that team")
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
            
            if arg[0] == "yesterday":
                yesterday = today - datetime.timedelta(days=1)
                c.execute(f"SELECT * FROM schedule WHERE date = '{yesterday}'")
                for item in c.fetchall():
                    games.append(item)
            else:
                #Search database for all games of the team given in the command
                team_to_search = " ".join(arg).title()
                for day_of_week in week:
                    c.execute(f"SELECT * FROM schedule WHERE ((home_name = '{team_to_search}' OR away_name = '{team_to_search}') OR (home_city = '{team_to_search}' OR away_city = '{team_to_search}')) AND date = '{day_of_week}'")
                    for item in c.fetchall():
                        games.append(item)
            
            #Add games to the embed
            if games != []:
                for game in games:
                    if game[2] == "":
                        game_full_date = game[6].split("-")
                        date_of_game = datetime.date(int(game_full_date[0]), int(game_full_date[1]), int(game_full_date[2]))
                        embed.add_field(name=f"{game[0]} vs {game[3]}", value=f"{date_of_game.strftime('%A')} @ {game[7]}")
                    else:
                        embed.add_field(name=f"{game[0]} vs {game[3]}", value=f"{game[7]}: {game[2]} - {game[5]}")
                
                if arg[0] == "yesterday":
                    embed.title = f"NBA Schedule for {yesterday.strftime('%B %d')}"
                else:
                    embed.title = f"NBA Schedule for {today.strftime('%B %d')} - {week[-1].strftime('%B %d')}"

                embed.url = "https://www.nba.com/schedule"
            
            else:
                embed.title = "Something Went Wrong"
                embed.description = "I can't seem to find that team. Make sure you spelled it correctly and try again!"
       
        else:
            #Search database for every game on the current day
            c.execute(f"SELECT * FROM schedule WHERE date = '{today}'")
            for item in c.fetchall():
                games.append(item)
            
            #Add games to the embed
            for game in games:
                if game[2] == "":
                    embed.add_field(name=f"{game[0]} vs {game[3]}", value=f"{game[7]}")
                
                else:
                    embed.add_field(name=f"{game[0]} vs {game[3]}", value=f"{game[7]}: {game[2]} - {game[5]}")
            
            embed.title = f"NBA Schedule for {today.strftime('%B %d')}"
            embed.url = "https://www.nba.com/schedule"

        await ctx.send(embed=embed)

        conn.close()

    
    @commands.command()
    async def test(self, ctx):
        embed = Embed(color=14167442)
        embed.set_author(name="Shot Talkin'",url= "https://twitter.com/ShotTalkin/", icon_url=os.getenv("SHOT_TALKIN_LOGO"))
        embed.title = "Top 5 Scorers"
        embed.add_field(name='Lebron James', value="3s: 3\nBlocks: 0\nAssists: 1\nSteals: 0\nRebounds: 9")
        embed.add_field(name='Trey Murphey', value="3s: 3\nBlocks: 3\nAssists: 7\nSteals: 0\nRebounds: 10")
        embed.add_field(name='Austin Rivers', value="3s: 1\nBlocks: 5\nAssists: 3\nSteals: 0\nRebounds: 5")
        embed.add_field(name='Rudy Gobert', value="3s: 5\nBlocks: 0\nAssists: 4\nSteals: 0\nRebounds: 9")
        embed.add_field(name='Karl Towns', value="3s: 2\nBlocks: 1\nAssists: 10\nSteals: 0\nRebounds: 4")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Nba(bot))
    load_dotenv()