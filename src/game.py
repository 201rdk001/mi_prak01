import enum
import random

# pylint: disable=invalid-name
game_length = 15
game_state = []

class PlayerType(enum.Enum):
    CIRCLE = "O"
    CROSS = "X"

class GameAlgorithm(enum.Enum):
    MINIMAX = 0
    ALFABETA = 1

def set_settings(length: int, player: PlayerType, algorithm: GameAlgorithm):
    global game_state
    global game_length

    game_length = length
    game_state = []

    print(length, player, algorithm)

def temp_get_game_state():
    if game_state:
        return game_state

    for _ in range(game_length):
        game_state.append(random.choice(["X", "O"]))

    return game_state
