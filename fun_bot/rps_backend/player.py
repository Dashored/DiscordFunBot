from dataclasses import dataclass
from .choices import RPS
from .status import GameStatus

@dataclass
class Player:
    id:int
    choice:RPS=None
    status:GameStatus=GameStatus.UNDECLARED