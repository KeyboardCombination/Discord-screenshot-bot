import pyautogui
import time
import discord
from discord.ext import commands
from PIL import Image

bot = commands.Bot(command_prefix="s!")

@bot.command()
async def ping(ctx):
    await ctx.send('pong ' + str(bot.latency*1000) + 'ms')

@bot.command()
async def screenshot(ctx):
    screenshot = pyautogui.screenshot()
    screenshot.save(r'screenshots/screenshot.png')
    await ctx.send(file=discord.File('screenshots/screenshot.png'))
    print("Sent screenshot from " + ctx.message.guild.name + " in " + ctx.message.channel.name)



bot.run('TOKEN')
print("Screenshot bot by KeyboardCombination has initialized.")
