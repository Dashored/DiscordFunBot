import discord
import logging

def handle_events(bot):

    @bot.event
    async def on_ready():
        for cog in bot._cogs:
            await bot.add_cog(cog)
        print("Funbot is ready to use!")
