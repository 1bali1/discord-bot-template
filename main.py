# Import req modules
import discord
import os
import utils

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)
cogsPath = "cogs"

# Get the bot token
token = utils.getConfig()["bot-token"]

# Load all cog
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

# On connection event
@bot.event
async def on_connection():
    print("Bot has connected to Discord services!")
    # Changing activity
    await bot.change_presence(activity=discord.CustomActivity(name="Starting..."), status=discord.Status.dnd)


# On ready event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}!")
    
    # Changing activity
    await bot.change_presence(activity=discord.CustomActivity(name=f"{len(bot.guilds)} servers | /info ping"), status=discord.Status.online)

# Run the bot
bot.run(token)