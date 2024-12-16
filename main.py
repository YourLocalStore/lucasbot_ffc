import discord
import random
import os, dotenv
import time

from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

random_messages = [
    "God bless you with mountains of gold and silver",
    "Good Morning. Let's basketball.",
    "Beautiful Risings Pharaoh. My temple is calling for its Pharaoh.",
    "Oooooh Lucy I'm Lebron James hairline",
    "tweaking out at staples rn need me a baddie ASAP!!",
    "Y'all see the shoes. Y'all see the money.",
    "knocked out rn",
    "<@524338310555107368> <@264582469037195264> wanna play phas later",
    "<@264582469037195264> vc",
    "https://cdn.discordapp.com/attachments/1157898808915677215/1299644913629003837/arabstone.mp4?ex=676130a5&is=675fdf25&hm=3dddf37848b7ee365eeed5d10b4efb31975ed1254c2fb23d7065debf8e4e96d0&",
    "https://cdn.discordapp.com/attachments/1157898808915677215/1271325075651563634/jamaicanspongebob.mp4?ex=6760febe&is=675fad3e&hm=0d752735283a12914653c188ffb7b170a15a39e6ed49a956ff0881244be2af65&",
    "https://cdn.discordapp.com/attachments/1157898808915677215/1270939547936489493/GUWehfCWoAA0WJN.png?ex=6760e931&is=675f97b1&hm=aed99e544a5620b0474304baecec50532885d085379d79ad5cce32dde82a5d85&",
    "https://cdn.discordapp.com/attachments/934692159792242708/1100317448491765802/stinksmelly-06082022-0001.mp4?ex=6761237a&is=675fd1fa&hm=f85225ab3f656af39a0f063cc35dbbd15c2193b543d922f5e36671bac1885521&",
    "https://cdn.discordapp.com/attachments/934692159792242708/1006723548489986048/words_of_advice.mp4?ex=6760c85d&is=675f76dd&hm=a24222b8170bbab5719c12d133904a0eb1cea5f151717a7ac1b311df4df28b90&",
    "https://cdn.discordapp.com/attachments/934700517840527371/1006284392454430750/v12044gd0000capvuajc77u08pqu0ao0.mp4?ex=6761299f&is=675fd81f&hm=004743d628ef93a3077ed4a54376598c5558da2c02284cfd0ac36f3980e438f7&"
]

bot_client = discord.Client(intents=intents)

@bot_client.event
async def on_ready():
    print(f"{bot_client.user}: Logged In")
    loop_message.start()

@bot_client.event
async def on_message(msg):
    starting_time = time.time() # time since lucas has not chatted

    try:
        if (msg.author == bot_client.user):
            return
        
        elif msg.author.id == 721797796881104936:
            ending_time = time.time()
            total_time = (ending_time - starting_time)

            if total_time < 10:
                await msg.channel.send("<@721797796881104936> work.... NOW!! https://tenor.com/view/wolf-angry-scare-gif-5183071")

            else:
                await msg.channel.send("<@721797796881104936> https://tenor.com/view/mr-krabs-back-to-work-spongebob-get-back-to-work-krusty-krab-gif-16474125980856176144")

    except Exception as err:
        await msg.channel.send(f"womp womp.... {err}")

@tasks.loop(hours = 2)
async def loop_message():
    try:
        channel = bot_client.get_channel(934692159792242708)
        await channel.send(random.choice(random_messages))

    except Exception as err:
        await channel.send("Something went wrong! Please contact <@524338310555107368> immediately.")

bot_client.run(os.getenv('DISCORD_BOT_TOKEN'))

