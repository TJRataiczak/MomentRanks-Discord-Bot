from nextcord.ext import commands
from nextcord import File, Embed
from dotenv import load_dotenv
import os
import random

class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["cage"], help = "Random Nicholas Cage meme")
    async def nick(self, ctx):
        random_image = f"{os.getenv('NICK_CAGE_DIR')}/{random.choice(os.listdir('images/nickcage'))}"
        file = File(random_image, filename="nickfunny.jpg")
        embed = Embed(title=random.choice(["Not the Bees!!!", "It's Cage Time!"]), color=14167442)
        embed.set_author(name="Shot Talkin'",url= "https://twitter.com/ShotTalkin/", icon_url=os.getenv("SHOT_TALKIN_LOGO"))
        embed.set_image(url="attachment://nickfunny.jpg")
        await ctx.send(file=file, embed=embed)
    
    @commands.command(help = "Random Milk Gang meme")
    async def milk(self, ctx):
        random_image = f"{os.getenv('MILK_GANG_DIR')}/{random.choice(os.listdir('images/milkgang'))}"
        file = File(random_image, filename= "milk.gif" if random_image.endswith(".gif") else "milk.jpg")
        embed = Embed(title="Milk Gang :dolphin:", color=14167442)
        embed.set_author(name="Shot Talkin'",url= "https://twitter.com/ShotTalkin/", icon_url=os.getenv("SHOT_TALKIN_LOGO"))
        embed.set_image(url="attachment://milk.gif" if random_image.endswith("gif") else "attachment://milk.jpg")
        await ctx.send(file=file, embed=embed)

def setup(bot):
    bot.add_cog(Funny(bot))
    load_dotenv()