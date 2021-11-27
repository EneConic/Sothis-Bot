import discord
from discord.ext import commands
import os
import random

client = commands.Bot(command_prefix = '!!')

@client.event
async def on_ready():

    #Throne Channel
    channel = client.get_channel(748660834305310770)
    """Test Channel"""
    """channel = client.get_channel(741493291761139732)"""

    #Introduction
    Intro = [
        "Hello young ones.",
        "To summon me, you must be in desperate need.",
        "I am quite bored. Won't you tell me tales of your adventures?",
        "It is most rude to interrupt a moment of repose. Very rude indeed.",
        "You can call me Sothis, but I'm also known as \"The Beginning\"."
    ]
    Intro_Select = Intro[random.randint(0,4)]

    #Weather
    Weather = [
        " sunny today.",
        " cloudy today",
        " stormy today.",
        " raining today."
    ]
    Weather_Select = random.choices(Weather, weights=(70, 15, 10, 5), k=1)
    Weather_String = ' '.join([str(elem) for elem in Weather_Select])

    #Daily Activity
    Activity = [
        " nothing going on today.",
        " a special lesson today, according to the twins' journals.",
        " a boulder in the monastery today."
    ]
    Activity_Select = random.choices(Activity, weights=(85, 10, 5), k=1)
    Activity_String = ' '.join([str(elem) for elem in Activity_Select])

    #Status
    Status_List = [
        "Mocking Byleth", #0
        "Mocking Fyleth", #1
        "Haunting Rhea",  #2
        "Floating around",#3
        "Bullying Seteth",#4
        "Taking a nap"    #5
    ]
    Status_Select = Status_List[random.randint(0,5)]

    #Intro, Weather, Activity Send
    await channel.send(Intro_Select)
    await channel.send("It is" + Weather_String)
    await channel.send("There is" + Activity_String)

    #Status Send
    await client.change_presence(activity=discord.Game(Status_Select))

@client.command(hidden=True)
async def load(ctx, extension):

    client.load_extension(f'TimeCogs.{extension}')
    print(f"TimeCog {extension} is loaded")

@client.command(hidden=True)
async def unload(ctx, extension):

    client.unload_extension(f'TimeCogs.{extension}')
    print(f"TimeCog {extension} is unloaded")

for filename in os.listdir('./TimeCogs'):
    if filename.endswith('.py'):
        client.load_extension(f'TimeCogs.{filename[:-3]}')

with open("token.txt", "r") as token:
	Start_Bot = token.read()

client.run(Start_Bot)