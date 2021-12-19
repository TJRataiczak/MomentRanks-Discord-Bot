from nextcord.ext import commands
from nextcord import File, Embed
from dotenv import load_dotenv
import os
import random

class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["cage"])
    async def nick(self, ctx):
        random_image = f"{os.getenv('NICK_CAGE_DIR')}/{random.choice(os.listdir('images/nickcage'))}"
        file = File(random_image, filename="nickfunny.jpg")
        embed = Embed(title=random.choice(["Not the Bees!!!", "It's Cage Time!"]), color=14167442)
        embed.set_image(url="attachment://nickfunny.jpg")
        await ctx.send(file=file, embed=embed)

def setup(bot):
    bot.add_cog(Funny(bot))
    load_dotenv()