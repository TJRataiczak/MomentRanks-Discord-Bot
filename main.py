from nextcord.ext import commands
from nextcord import Embed
from dotenv import load_dotenv
import os

load_dotenv()

class CustomHelpCommand(commands.HelpCommand):

    def __init__(self):
        super().__init__()
    
    async def send_bot_help(self, mapping):
        
        embed = Embed(title="Command Overview", color=14167442)
        embed.set_author(name="Shot Talkin'",url= "https://twitter.com/ShotTalkin/", icon_url=os.getenv("SHOT_TALKIN_LOGO"))

        for cog in mapping:
            if cog != None:
                command_names = [command.name for command in mapping[cog]]
                command_helps = [command.help for command in mapping[cog]]
                for command_name, command_help in zip(command_names, command_helps):
                    embed.add_field(name=command_name, value=command_help, inline=False)

        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)
    
    async def send_group_help(self, group):
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        return await super().send_command_help(command)



client = commands.Bot(command_prefix=os.getenv("DISCORD_PREFIX"), help_command=CustomHelpCommand())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"loaded: {filename}")


client.run(os.getenv("DISCORD_TOKEN"))