import discord
from discord.ext import commands
import random

class Therapy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['open', 'oc'], hidden=False, help="Opens a therapy channel")
    async def openchannel(self, ctx):

        Therapy_Name = "Therapy"
        Therapy_Category = discord.utils.get(ctx.guild.categories, name=Therapy_Name)

        if ctx.guild.create_text_channel(f'Therapy-{ctx.message.author}', category=Therapy_Category) == True:

            await ctx.send("A channel for you is already open.")
        
        else:

            await ctx.guild.create_text_channel(f'Therapy-{ctx.message.author}', category=Therapy_Category)

    @commands.command(aliases=['close', 'cc'], hidden=False, help="Closes the user's therapy channel")
    async def closechannel(self, ctx):

        User_Channel_Name = ctx.message.author
        Therapy_Channel_Name - discord.utils.get(guild.text_channels, name=f'Therapy-{User_Channel_Name}')

        if User_Channel_Name in Therapy_Channel_Name:

            await Therapy_Channel_Name.close()

        else:

            await ctx.send("You do not have a channel to close.")

def setup(client):

    client.remove_cog(Therapy(client))