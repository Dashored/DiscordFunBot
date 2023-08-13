import discord
from ..rps_backend import *

class GameView(discord.ui.View):
    def __init__(self,owner:discord.Member,target:discord.Member):
        self.owner = owner
        self.target = target
        self.game = Game(Player(self.owner.id),Player(self.target.id))
        self.text = f"[winner] won the duel: {self.owner.mention} VS {self.target.mention}!"
        super().__init__(timeout=None)
    

    async def interaction_check(self, interaction) :
        return interaction.user in (self.target,self.owner)

    async def check_game_status(self,interaction:discord.Interaction):
        self.game.determine_winner()

        if self.game.player1.status == GameStatus.UNDECLARED:
            return
        
        if self.game.player1.status == GameStatus.DRAW:
            await interaction.channel.send(f"{self.owner.mention} VS {self.target.mention} ended in draw!")
            await interaction.message.delete() 

        else:
            self.text = self.text.replace("[winner]",self.owner.mention if self.game.player1.status == GameStatus.WIN else self.target.mention )
            await interaction.channel.send(self.text)
            await interaction.message.delete() 

    @discord.ui.button(label='Rock', style=discord.ButtonStyle.gray,emoji="✊")
    async def rock(self, interaction: discord.Interaction,button: discord.ui.Button):
        if interaction.user == self.owner:
            self.game.player1.choice = RPS.ROCK 
        else:
            self.game.player2.choice = RPS.ROCK 
        await self.check_game_status(interaction)

        await interaction.response.defer()

    @discord.ui.button(label='Paper', style=discord.ButtonStyle.gray,emoji="🫱")
    async def paper(self, interaction: discord.Interaction,button: discord.ui.Button):

        if interaction.user == self.owner:
            self.game.player1.choice = RPS.PAPER 
        else:
            self.game.player2.choice = RPS.PAPER
        await self.check_game_status(interaction)

        await interaction.response.defer()

    @discord.ui.button(label='Scissors', style=discord.ButtonStyle.gray,emoji="✌️")
    async def scissors(self, interaction: discord.Interaction,button: discord.ui.Button):

        if interaction.user == self.owner:
            self.game.player1.choice = RPS.SCISSORS
        else:
            self.game.player2.choice = RPS.SCISSORS
        await self.check_game_status(interaction)

        await interaction.response.defer()
