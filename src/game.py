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

#edited by Ritvars--------
class TreeNode:
    def __init__(self, state, player_type):
        self.state = state
        self.player_type = player_type
        self.children = []

def generate_tree(node, depth):
    if depth <= 0:
        return

    for i in range(len(node.state) - 1):
        if node.state[i] != node.state[i+1]:
            new_state = node.state[:i] + node.player_type.value + node.state[i+2:]
            new_player_type = PlayerType.CIRCLE if node.player_type == PlayerType.CROSS else PlayerType.CROSS
            child = TreeNode(new_state, new_player_type)
            node.children.append(child)
            generate_tree(child, depth - 1)
#------------

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
