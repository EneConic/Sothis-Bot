import discord
from discord.ext import commands
import time
import random

class ChitChat(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(hidden=False, help="Ask me anything!")
    async def question(self, ctx, *, message):

        Answers = ["Yes ", "No ", "Perhaps ", "If you work towards it ", "Absolutely ", "Absolutely not", "May the goddess forgive you "]
        Answer_List = Answers[random.randint(0,5)]
        await ctx.send(Answer_List + f'{ctx.message.author.mention}')

    @commands.command(hidden=False, help="The latest news of Garreg Mach!")
    async def gossip(self, ctx):

                    #|-------------------------------------Church(9)---------------------------------------| |--------Professors(3)---------|  |----------------------------------Black Eagles(8)---------------------------------------|  |----------------------------------Blue Lions(8)------------------------------|  |-------------------------------Golden Deer(8)-----------------------------------|  |----------Ashen Wolves(4)-----------|  |-----------DLC(3)--------|
        Class_Roster = ['Sothis', 'Rhea', 'Seteth', 'Flayn', 'Catherine', 'Shamir', 'Cyril', 'Gilbert', 'Alois', 'Byleth', 'Fyleth', 'Manuela', 'Hanneman', 'Edelgard', 'Hubert', 'Caspar', 'Linhardt', 'Bernadetta', 'Dorothea', 'Ferdinand', 'Petra', 'Dimitri', 'Dedue', 'Felix', 'Sylvain', 'Ingrid', 'Mercedes', 'Ashe', 'Annette', 'Claude', 'Hilda', 'Marianne', 'Lysithea', 'Lorenz', 'Raphael', 'Ignatz', 'Leonie', 'Yuri', 'Constance', 'Balthus', 'Hapi', 'Jeritza', 'Anna', 'Aefric']
        Class_Roster_Select_1 = Class_Roster[random.randint(0,43)]
        Class_Roster_Select_2 = Class_Roster[random.randint(0,43)]

        Gossip_Number = ['single', 'double']
        Gossip_Number_Select =  Gossip_Number[random.randint(0,1)]

        if Gossip_Number_Select == Gossip_Number[0]:

            Single_Gossip = [
                "{} sleeps alone.",
                "{} has snuck out of the dorms at night before.",
                "{} is studying.",
                "{} is dying.",
                "{} wants extra credit.",
                "{} hates everything.",
                "{} took a nap.",
                "{} went into town.",
                "The Archbishop does not like {}.",
                "{} is a true noble.",
                "{} is failing their classes.",
                "{} wants to go home.",
                "{} hates the Church.",
                "{} hates the Empire.",
                "{} hates the Kingdom.",
                "{} hates the Alliance.",
                "{} loves the Church.",
                "{} loves the Empire.",
                "{} loves the Kingdom.",
                "{} loves the Alliance.",
                "The Archbishop knows what {} is planning...",
                "{} fell into the pond today. And yesterday too!",
                "{} wants some \"extra credit\" from their professor.",
                "{} is currently training.",
                "{} is plotting a scheme.",
                "{} went to the Cathedral to pray.",
                "Someone find {}. They're committing tax evasion.",
                "{} fell asleep in class.",
                "{} went for a walk around the monstery today.",
                "Oh, guess what?! {} went shopping for a special someone!"
                "Did you know that {} has a secret stash of alcohol in their room? It's true! I'm not lying!",
                "{} lost another item again. Someone call an Eisner to return it.",
                "{} was last seen a few days ago. I wonder what happened to them?",
                "{} lost their homework.",
                "{} hunted a huge deer for dinner!",
                "{} is feeling unwell today.",
                "It's {}'s turn to clean the stables. Yuck.",
                "{} has drank nothing but coffee today.",
                "{} hasn't slept in days! For the love of me, go to bed!"
            ] #0-37
            Single_Gossip_Select = Single_Gossip[random.randint(0,36)]

            await ctx.send(Single_Gossip_Select.format(Class_Roster_Select_1))

        if Gossip_Number_Select == Gossip_Number[1]:

            Double_Gossip = [
                "{} and {} are dating.",
                "{} and {} are eating dinner together.",
                "{} and {} are studying.",
                "{} and {} hate each other.",
                "{} and {} are cuddling.",
                "{} and {} are holding hands.",
                "{} and {} took a nap together.",
                "{} and {} went shopping together! I wonder what they bought...?",
                "{} is plotting against {}.",
                "{} got into a fight with {}.",
                "{} put their Minecraft bed next to {}'s.",
                "{} spent the night in {}'s dorm. At least they weren't loud this time.",
                "{} really wants to kiss {}. Please just keep it behind closed doors.",
                "{} and {} are cooking together.",
                "{} wants to give {} a gift but can't decide what to give.",
                "{} went fishing with {} at the pond.",
                "{} has a crush on {}.",
                "{} and {} are having tea time.",
                "{} bought {} a gift.",
                "{} and {} are planning something together.",
                "{} and {} snuck off together last night.",
                "{} wants to kill {}.",
                "{} gave {} a big hug!",
                "{} and {} are arguing a lot today."
            ] #0-22
            Double_Gossip_Select = Double_Gossip[random.randint(0,22)]

            await ctx.send(Double_Gossip_Select.format(Class_Roster_Select_1, Class_Roster_Select_2))

    @commands.command(hidden=True, help="A puzzle to amuse you")
    async def puzzle(self, ctx):

        Message_List = [
            "Byleth is a bad professor",
            "The students are cheating",
            "Seteth has a daughter",
            "Jeralt is alive",
            "Hubert loves the Church"
        ]
        Message_Select = Message_List[random.randint(0,4)]
        Distance = random.randrange(1, 10, 1)

        Random_Change = ['Up', 'Down']
        Random_Change_Select = Random_Change[random.randint(0, 1)]

        if Random_Change_Select == Random_Change[0]:
            for change in Message_Select:
                Coded_Message = ord(change) + Distance
                await ctx.send(Coded_Message)
                await ctx.send("Now guess the message! (Ask Byleth for the answer currently)")
                break

        if Random_Change_Select == Random_Change[1]:
            for change in Message_Select:
                Coded_Message = ord(change) + Distance
                await ctx.send(Coded_Message)
                await ctx.send("Now guess the message! (Ask Byleth for the answer currently)")
                break

    #DM a user
    @commands.command(hidden=False, help='Send a secret message')
    async def message(self, ctx):
        ### USER ID ###
        #Hubert_User = await self.client.fetch_user(546798537199976448)
        #Edelgard_User = await self.client.fetch_user(459434351063465985)
        Byleth_User = await self.client.fetch_user(391848381380558862)
        #Claude_User = await self.client.fetch_user(767470098666749962)
        #Rhea_User = await self.client.fetch_user(195459199612878849)

        ### SENDER NAME ###
        Sender_User = ctx.message.author.nick

        ### MESSAGE ###
        #Hubert_Message = ("<@" +str(Sender_User) + "> says hello!")
        #Edelgard_Message = ("BELIEVE IN ME!")
        Byleth_Message = ("<" +str(Sender_User) + "> says hello!")
        #Rhea_Message = ("I'm still alive!")

        ### SENT MESSAGE ###
        #await Hubert_User.send(Hubert_Message)
        #await Edelgard_User.send(Edelgard_Message)
        await Byleth_User.send(Byleth_Message)
        #await Rhea_User.send(Rhea_Message)
        print("Message Sent!")


def setup(client):

    client.add_cog(ChitChat(client))