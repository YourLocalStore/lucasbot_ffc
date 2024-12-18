import discord
import commands
import random, random_msg
import os, dotenv, sys
import time

from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
bot_client = commands.Bot(
    command_prefix="l!", 
    owner_id = int(os.environ['ID_STORE']), 
    case_insensitive=True, intents=intents, 
    help_command=None
)

start_time = time.time()
msg_sent_at = {}

@bot_client.event
async def on_ready():
    print(f"{bot_client.user}: Logged In")

    try:
        await bot_client.load_extension('commands')
    except Exception as err:
        print(err)

    loop_message.start()

@bot_client.event
async def on_message(msg): 
    l_id = int(os.environ["ID_BREAD"])

    try:
        if (msg.author == bot_client.user):
            return
    
        if not msg_sent_at.get(msg.author.id):
            time_start = time.time()
            msg_sent_at[msg.author.id] = time_start
            print(msg_sent_at)

        else:
            for k, v in msg_sent_at.items():
                if k == l_id:
                    time_end = time.time()
                    time_taken = time_end - v

                    if time_taken < 60:
                        await msg.channel.send(f"<@{l_id}>, There has been a {int((time_taken // 3600) % 60)}m {int((time_taken % 3600) % 60)}s gap" + \
                                                " Since you last sent a message. \n" +
                                                "https://tenor.com/view/mr-krabs-back-to-work-spongebob-get-back-to-work-krusty-krab-gif-16474125980856176144"
                                                )
                        
                    elif (time_taken >= 60) and (time_taken < 300):
                        await msg.channel.send(f"<@{l_id}>, There has been a {int((time_taken // 3600) % 60)}m {int((time_taken % 3600) % 60)}s gap" + \
                                                " Since you last sent a message. Work... NOW!!\n" +
                                                "https://tenor.com/view/mr-krabs-back-to-work-spongebob-get-back-to-work-krusty-krab-gif-16474125980856176144"
                                                )
                        
                    else:
                        del msg_sent_at[l_id]
                        break

                    msg_sent_at[l_id] = time_end
                break

    except Exception as err:
        await msg.channel.send(f"womp womp.... {err}")

    await bot_client.process_commands(msg)

@tasks.loop(hours = 2)
async def loop_message():
    message_choice = random.choice(["text", "video"])

    try:
        channel = bot_client.get_channel(934692159792242708)

        lucasbot_random_msg = discord.Embed(
            title = "Lucas Bot Announcment",
            description = "Wisdom and Random BS Bi-hourly!"
        )
        
        if message_choice == "text":
            lucasbot_random_msg.add_field(
                name = "",
                value = random.choice(random_msg.random_messages)
            )
            await channel.send(embed = lucasbot_random_msg)

        else:
            await channel.send(embed = lucasbot_random_msg)
            await channel.send(random.choice(random_msg.random_videos))

    except Exception as err:
        await channel.send(f"Something went wrong! {err}")

bot_client.run(os.getenv('DISCORD_BOT_TOKEN'))