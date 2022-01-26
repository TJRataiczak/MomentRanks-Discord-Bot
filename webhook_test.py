from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/930520597065236500/dam7Ui3q41r-dk9Ocgn_z3rrpIJfzg85HbQemnfFvy9v-eyBSfn7ItbiPhjCkgbvQq6Y")

embed = DiscordEmbed(color=14167442)
embed.set_author(name="Shot Talkin'",url= "https://twitter.com/ShotTalkin/")
embed.title = "Top 5 Scorers"
embed.add_embed_field(name='Lebron James', value="3s: 3")
embed.add_embed_field(name='Trey Murphey', value="3s: 3")
embed.add_embed_field(name='Austin Rivers', value="3s: 1")
embed.add_embed_field(name='Rudy Gobert', value="3s: 5")
embed.add_embed_field(name='Karl Towns', value="3s: 2")

webhook.add_embed(embed)

webhook.execute()