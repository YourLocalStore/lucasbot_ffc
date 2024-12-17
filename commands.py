import discord
import main
import time, math
import requests

from discord.ext import tasks, commands

@commands.command(name="shutoff")
@commands.is_owner()
async def bot_shutdown(ctx):
    bot_shutdown = "Shutting down..."
    await ctx.send(f"{bot_shutdown}")
    await ctx.bot.close()

@commands.command(name="runtime")
async def bot_runtime(ctx):

    if ctx.author:
        end_time = time.time()
        total_time = (end_time - main.start_time)

        hours = total_time // 3600
        minutes = (total_time % 3600) // 60
        seconds = (total_time % 3600) % 60

        await ctx.send(f"Bot Runtime: {int(hours)}h {int(minutes)}m {int(seconds)}s")

@commands.command(name = "randomcat")
async def get_random_cat(ctx):
    car_url = 'https://api.thecatapi.com/v1/images/search'
    cat_embed = discord.Embed(
        title = "One car, coming right up! 🐈",
        description = "bottom text"
    )
    
    try:
        cat_status = requests.get(car_url)

        if cat_status.status_code == 200:
            print("Successful connection!")
            cat_image = cat_status.json()[0]["url"] # Stored as first index, get matching k,v pair
            cat_embed.set_image(url = cat_image)

            await ctx.send(embed = cat_embed)

        else:
           print(f"Unsuccessful connection... {cat_status.status_code}")
    
    except Exception as err:
        print(err)

@commands.command(name = "randomdog")
async def get_random_dog(ctx):
    dog_url = 'https://dog.ceo/api/breeds/image/random'
    dog_embed = discord.Embed(
        title = "One dog, coming right up! 🐶",
        description = "bottom text"
    )

    try:
        dog_status = requests.get(dog_url)

        if dog_status.status_code == 200:
            print("Successful connection!")
            dog_image = dog_status.json()["message"]
            dog_embed.set_image(url = dog_image)

            await ctx.send(embed = dog_embed)

        else:
           print(f"Unsuccessful connection... {dog_status.status_code}")
    
    except Exception as err:
        print(err)

"""
GROUPING FOR HELP COMMAND
"""
@commands.group(name="help", invoke_without_command=True)
async def bot_help(ctx):

    help_embed = discord.Embed(
        description = "Type l!help (Command) to see specific information about commands.",
        title = "Lucas Bot Help Centre",
    )
    help_embed.add_field(
        name = "Miscellaneous", 
        value = "runtime"
    )
    help_embed.add_field(
        name = "Fun", 
        value = "randomcat, randomdog, randomcow"
    )
    help_embed.add_field(
        name = "Owner", 
        value = "shutdown"
    )

    await ctx.send(embed = help_embed)

@bot_help.command()
async def runtime(ctx):
    em = discord.Embed(
        title = "Miscellaneous - 'l!runtime'",
        description = "Checks how long the bot has been up."
    )
    await ctx.send(embed = em)

@bot_help.command()
async def randomcat(ctx):
    em = discord.Embed(
        title = "Fun - 'l!randomcat'",
        description = "Posts a random cat image to the given channel"
    )
    await ctx.send(embed = em)

@bot_help.command()
async def randomdog(ctx):
    em = discord.Embed(
        title = "Fun - 'l!randomdog'",
        description = "Posts a random dog image to the given channel"
    )
    await ctx.send(embed = em)

@bot_help.command()
async def randomcow(ctx):
    em = discord.Embed(
        title = "Fun - 'l!randomcow'",
        description = "Posts a random dog image to the given channel"
    )
    await ctx.send(embed = em)

@bot_help.command()
async def shutdown(ctx):
    em = discord.Embed(
        title = "Owner - 'l!shutdown'",
        description = "Turns the bot off."
    )
    await ctx.send(embed = em)

async def setup(bot):
    bot.add_command(bot_shutdown)
    bot.add_command(bot_runtime)
    bot.add_command(bot_help)
    bot.add_command(get_random_cat)
    bot.add_command(get_random_dog)
