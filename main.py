import discord
import os
import requests
import json
import npm
import crackupbank
from keep_alive import keep_alive
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

load_dotenv()
bot = commands.Bot(command_prefix='!')

BOT_TOKEN = os.getenv("TOKEN")
voicecracks = 0

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    print("boom")
    global voicecracks
    with open("crackupbank.py", "r") as f:
      voicecracks = int(f.read())
    f.close()

@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command()
async def crackup(ctx, user:discord.User=None):
    print("eee")
    if not user:
      global voicecracks
      voicecracks += 1
      with open("crackupbank.py", "w") as f:
        f.write(str(voicecracks))
      f.close()
      await ctx.channel.send("Voice Crack Counter = " + str(voicecracks))
      print("fff")
    else:
      if os.path.exists(str(user)):
        with open(str(user), "r") as f:
          crackuser = int(f.read())
        f.close()
        crackuser += 1
        with open(str(user), "w") as f:
          f.write(str(crackuser))
        f.close()
        await ctx.channel.send(str(user) + " now has " + str(crackuser) + " cracks.")
      else:
        with open(str(user), "w") as f:
          f.write("1")
        f.close()
        with open(str(user), "r") as f:
          crackchange = str(f.read())
        f.close()
        await ctx.channel.send("Voice cracks are now " + crackchange)

@bot.command()
async def crackdown(ctx, user:discord.User=None):
  print("lll")
  if not user:
    global voicecracks
    voicecracks -= 1
    with open("crackupbank.py", "w") as f:
      f.write(str(voicecracks))
    f.close()
    await ctx.channel.send("Voice Crack Counter = " + str(voicecracks))
    print("mmm")
  else:
    if os.path.exists(str(user)):
      with open(str(user), "r") as f:
        crackuser = int(f.read())
      f.close()
      crackuser -= 1
      with open(str(user), "w") as f:
        f.write(str(crackuser))
      f.close()
      await ctx.channel.send(str(user) + " now has " + str(crackuser) + " cracks.")
    else:
      await ctx.channel.send(str(user) + " does not have any voice cracks.")

@bot.command()
async def crackbank(ctx):
  print("ggg")
  global voicecracks
  cracks = str(voicecracks)
  print("hhh")
  await ctx.channel.send("Total Voice Cracks: " + cracks)
  print("iii")

@bot.command()
async def cracks(ctx, user:discord.User):
  print("jjj")
  await ctx.channel.send("The user's name is: " + str(user))
  print("kkk")
  if os.path.exists(str(user)):
    await ctx.channel.send("True")
    with open(str(user), "r") as f:
      usercracks = str(f.read())
    f.close()
    await ctx.channel.send("Their total cracks are: " + usercracks)
  else:
    await ctx.channel.send("False")
    with open(str(user), "w") as f:
      f.write("0")
    f.close()
    with open(str(user), "r") as f:
      crackchange = str(f.read())
    f.close()
    await ctx.channel.send("Voicecracks are now " + crackchange)

keep_alive()
bot.run(BOT_TOKEN)