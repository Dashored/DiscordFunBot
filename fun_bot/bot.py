import discord
from discord.ext import commands
from .event_handler import handle_events
from .rps_cog import RockPaperScissors



class FunBot(commands.Bot):
    def __init__(self,settings):
        self.settings = settings
        intents = discord.Intents()
        intents.message_content = True
        intents.messages = True

        self._cogs = [RockPaperScissors(self)]
        super().__init__(command_prefix=self.settings.prefix,intents=intents)
        handle_events(self)


    #custom reply command to avoid accidently mentioning roles
    async def reply_to_command(self,ctx,message:str=None,embed:discord.Embed=None,view:discord.ui.View=None,delete_after=None):
        allowed_mentions = discord.AllowedMentions.none()
        allowed_mentions.replied_user = True
        allowed_mentions.users = True
        if ctx.interaction:
            await ctx.interaction.response.send_message(message,embed=embed,allowed_mentions=allowed_mentions,view=view,delete_after=delete_after)
        else:
            await ctx.message.reply(message,embed=embed,allowed_mentions=allowed_mentions,view=view,delete_after=delete_after)
        