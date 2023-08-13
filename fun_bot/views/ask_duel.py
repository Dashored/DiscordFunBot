import discord
from .game_view import GameView

class AskDuel(discord.ui.View):
    def __init__(self,owner:discord.Member,target:discord.Member):
        super().__init__(timeout=120)
        self.owner = owner
        self.target = target
    
    async def interaction_check(self, interaction) :
        return interaction.user == self.target
   

    @discord.ui.button(label='Accept', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.defer()
        await interaction.message.delete()
        
        await interaction.channel.send(f"{self.owner.mention} VS {self.target.mention}:",view= GameView(self.owner,self.target))
        
    
    @discord.ui.button(label='Decline', style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.send_message("You declined the duel!",ephemeral=True)
        await interaction.message.delete()
