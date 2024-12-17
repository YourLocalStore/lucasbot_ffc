import discord
import time
import main
import math

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

@commands.group(name="help", invoke_without_command=True)
async def bot_help(ctx):

    help_embed = discord.Embed(description = "Type l!help (Command) to see specific information about commands.",
                               title = "Lucas Bot Help Centre",
                               )

    help_embed.add_field(name = "Miscellaneous", value = "Runtime")
    help_embed.add_field(name = "Owner", value = "Shutdown")

    await ctx.send(embed = help_embed)

@bot_help.command()
async def runtime(ctx):
    runtime_embed = discord.Embed(title = "Miscellaneous - 'Runtime'",
                                  description = "Checks how long the bot has been up."
                                  )
    await ctx.send(embed = runtime_embed)

@bot_help.command()
async def shutdown(ctx):
    shutdown_embed = discord.Embed(title = "Owner - 'Runtime'",
                                   description = "Turns the bot off."
                                   )
    await ctx.send(embed = shutdown_embed)

async def setup(bot):
    bot.add_command(bot_shutdown)
    bot.add_command(bot_runtime)
    bot.add_command(bot_help)
