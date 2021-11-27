import discord
from discord.ext import commands
import random
import os

class Memes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    async def memes(self, ctx):

        Meme_List = os.listdir(os.chdir("C:\\Users\\Akara\\Desktop\\Code\\Python\\Discord\\Sothis\\M3M35"))
        Meme_Choice = random.choice(Meme_List)
        await ctx.send(file=discord.File(Meme_Choice))

def setup(client):

    client.add_cog(Memes(client))