# Import modules
import discord
from discord.ext import commands
import utils
from datetime import datetime

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)


# Create class
class InfoCog(commands.Cog, name="InfoCog"):
    def __init__(self, bot):
        self.bot = bot

    # Create a slash command group, example cmd: /info ping
    info = discord.SlashCommandGroup(
        "info", # Group name
        "Information commands.", # Group description
        integration_types={
            discord.IntegrationType.user_install, # Users can use the commands in dm and other servers where the bot isn't joined
            discord.IntegrationType.guild_install, # This is just for guilds
        },
    )
    
    # Create a slash command
    @info.command(name="ping", description="Get the bot's latency!")
    async def infoPing(self, ctx: discord.ApplicationContext):
        # Defer 
        await ctx.defer()
        
        # Get config from config.json
        config = utils.getConfig()
        # Get values
        embedColor = config.get("embed-color", 0x0087f5)
        
        # Check if the given embed color is correct
        try:
            embedColor = hex(embedColor)
        except:
            embedColor = 0x0087f5
            
            
        # Create embed
        embed = discord.Embed(
            title="Ping",
            description=f"Pong!🏓 The bot latency is `{round(self.bot.latency * 1000)}ms`",
            author=discord.EmbedAuthor(ctx.user.name), # If you want you can add url=ctx.user.avatar.url
            footer=discord.EmbedFooter(self.bot.user.name + " • Ping"), # If you want you can add url=self.bot.user.avatar.url
            color=embedColor,
            timestamp=datetime.now()
        )
        
        # Respond
        await ctx.respond(embed=embed)
        
        
# Add the cog to the bot
def setup(bot):
    bot.add_cog(InfoCog(bot))
