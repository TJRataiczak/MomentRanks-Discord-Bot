from nextcord.ext import commands
from nextcord import Embed, File
from dotenv import load_dotenv
import os

class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def play(self, ctx):

        embed = Embed(title="MomentRanks Play | NBA Top Shot Fantasy Competition", color=14167442, url=os.getenv("MOMENTRANKS_PLAY_LINK"), description="Compete with your friends with your NBA Top Shot moments. Set a lineup, watch your players, and win rewards!")
        embed.set_author(name="Shot Talkin'",url= "https://twitter.com/ShotTalkin/", icon_url=os.getenv("SHOT_TALKIN_LOGO"))
        embed.set_image(url="https://play.momentranks.com/img/PLAY09_horizontal.png")
        await ctx.send(embed=embed)

    @commands.command(aliases = ["cal"])
    async def calendar(self, ctx):
        
        embed = Embed(title="Top Shot Event Calendar", url=os.getenv("SPREADSHEET_LINK"), color=14167442)
        embed.set_author(name="Shot Talkin'",url= "https://twitter.com/ShotTalkin/", icon_url=os.getenv("SHOT_TALKIN_LOGO"))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Links(bot))
    load_dotenv()