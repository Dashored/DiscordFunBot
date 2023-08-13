from .player import Player
from .status import GameStatus
from .choices import RPS

class Game:
    def __init__(self,player1:Player,player2:Player):
        self.player1 = player1
        self.player2 = player2
    
    def determine_winner(self):
        if self.player1.choice == None or self.player2.choice == None:
            self.player1.status = GameStatus.UNDECLARED 
            self.player2.status = GameStatus.UNDECLARED 
        
        elif self.player1.choice == self.player2.choice:
            self.player1.status = GameStatus.DRAW
            self.player2.status = GameStatus.DRAW

        elif (self.player1.choice == RPS.ROCK and self.player2.choice == RPS.SCISSORS) or \
           (self.player1.choice == RPS.PAPER and self.player2.choice == RPS.ROCK) or \
           (self.player1.choice == RPS.SCISSORS and self.player2.choice == RPS.PAPER):
            self.player1.status = GameStatus.WIN
            self.player2.status = GameStatus.LOSE
        else:
            self.player1.status = GameStatus.LOSE
            self.player2.status = GameStatus.WIN