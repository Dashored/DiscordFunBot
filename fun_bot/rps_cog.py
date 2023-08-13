import discord
from discord.ext import commands
from .views.ask_duel import AskDuel

class RockPaperScissors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if self.bot.settings.rps.get("allowed_channel"):
            return ctx.channel.id == self.bot.settings.rps.get("allowed_channel") if self.bot.settings.rps.get("allowed_channel") != 0 else True 
        
        return True
    
    @commands.group(name='rps')
    async def rps(self,ctx):
        if ctx.invoked_subcommand is None:
            pass
        

    @rps.command(name='duel')
    async def duel_command(self, ctx,target:discord.Member):
        if target == ctx.author:
            await self.bot.reply_to_command(ctx,message="You played yourself. Wait, you can't.")
            return
        view = AskDuel(ctx.author,target)
        
        await self.bot.reply_to_command(ctx,message = f"Hey {target.mention}! {ctx.author.mention} challenged you to a rps duel!",view=view)