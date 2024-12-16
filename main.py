import discord
import random
import os, dotenv

from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot_client = discord.Client(intents=intents)

@bot_client.event
async def on_ready():
    print(f"{bot_client.user}: Logged In")

@bot_client.event
async def on_message(msg):
    if (msg.author == bot_client.user):
        return
    
    if msg.content.startswith("lucas"):
        await msg.channel.send("jonkler: why so serious\n" + 
                                "the rick friend: hehahehahehaha (listening to brazillian phonk)\n" +
                                "caseoh: put that cookie down!!! (german stare) \n" + 
                                "THOSE WHO KNOW 💀💀 explanation in comments \n" 
                               )
        
bot_client.run(os.getenv('DISCORD_BOT_TOKEN'))

