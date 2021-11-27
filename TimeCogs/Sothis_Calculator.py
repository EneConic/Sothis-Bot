import discord
from discord.ext import commands
import random
import math

class Calculator(commands.Cog):

    def __init__(self, client):
        self.client = client

    #BASIC COMMANDS
    @commands.command(help="Add two numbers", aliases=["+"])
    async def add(self, ctx, a, b):

        result = str(int(a) + int(b))
        await ctx.send("The sum is: " + result)

    @commands.command(help="Subtract two numbers", aliases=["-"])
    async def subtract(self, ctx, a, b):

        result = str(int(a) - int(b))
        await ctx.send("The difference is: " + result)

    @commands.command(help="Multiply two numbers", aliases=["*"])
    async def multiply(self, ctx, a, b):

        result = str(int(a) * int(b))
        await ctx.send("The product is: " + result)

    @commands.command(help="Divide two numbers", aliases=["/"])
    async def divide(self, ctx, a, b):

        result = str(int(a) / int(b))
        await ctx.send("The quotient is: " + result)

    #PROGRAMS
    @commands.command(help="Square root a number", aliases=["sqrt", "sq"])
    async def squareroot(self, ctx, a):

        result = str(int(a)**0.5)
        await ctx.send("The square root is: " + result)

def setup(client):

    client.add_cog(Calculator(client))