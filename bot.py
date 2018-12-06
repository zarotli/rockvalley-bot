import asyncio
import json
import random
import time

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Connected and ready to use")


@bot.command(pass_context=True)
async def Vote(ctx):
    await bot.say("Vote Here!")


@bot.event
async def on_message(message):
    if message.content.startswith('!Vote'):
        embed = discord.Embed(title="Votes:", description="(Vote Top Will Get The Highest Rank)", color=0x00ff00)
        embed.add_field(name="Votes Link 1", value="https://minecraftservers.biz/servers/142784/vote/", inline=True)
        embed.add_field(name="Vote Link 2", value="https://minecraft-mp.com/server/209144/vote/", inline=True)
        embed.add_field(name="Vote Link 3", value="https://topg.org/Minecraft/in-502386", inline=True)
        embed.add_field(name="Vote Link 4", value="https://minecraft-server-list.com/server/433136/vote/", inline=True)
        embed.set_thumbnail(url="https://cdn.minecraft-server-list.com/servericon/433136.png")
        await bot.send_message(message.channel, embed=embed)


bot.run("process.env.BOT_TOKEN")
