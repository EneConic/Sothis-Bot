import discord
from discord.ext import commands
import datetime

class Date(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=False, help='Tells the date')
    async def date(self, ctx):
        Today_Date = datetime.datetime.now()
        Real_Day = str(Today_Date.day) #Get Day
        Real_Month = Today_Date.month #Get Month
        Real_Year = str(Today_Date.year) #Get Year

        #Get FE3H Month
        FE3H_Month = Real_Month - 1

        FE3H_Moon = [
            "Guardian Moon", #January
            "Pegasus Moon", #Febuary
            "Lone Moon", #March
            "Great Tree Moon", #April
            "Harpstring Moon", #May
            "Garland Moon", #June
            "Blue Sea Moon", #July
            "Verdant Rain Moon", #August
            "Horsebow Moon", #September
            "Wyvern Moon", #October
            "Red Wolf Moon", #November
            "Ethereal Moon" #December
        ]

        Sothis_Month = FE3H_Moon[FE3H_Month]

        await ctx.send(f'Today is day {Real_Day} of the {Sothis_Month}, {Real_Year}')

def setup(client):
    client.add_cog(Date(client))