from enum import Enum,auto


class GameStatus(Enum):
    WIN = auto()
    LOSE = auto()
    DRAW = auto()
    UNDECLARED = auto()
