# function that checks if the player can make any combinations on the next move
def player_has_next_moves(state, player):
    for i in range(len(state) - 1):
        if player == 'O':
            if state[i:i+2] == 'XX' or state[i:i+2] == 'XO':
                return True
        elif player == 'X':
            if state[i:i+2] == 'OO' or state[i:i+2] == 'OX':
                return True
    return False


def heuristic_function(node, opponent):
    state = node.state
    circle_points = node.circle_points
    cross_points = node.cross_points
    player_type = node.player_type
    opposite_player = opponent
    heuristic_value = 0

    for i in range(len(state) - 1):
        current_symbol = state[i]
        next_symbol = state[i+1]
        if player_has_next_moves(state, player_type):
            # heuristic function for circles
            if opposite_player == 'O':
                if current_symbol == 'X' and next_symbol == 'X':
                    heuristic_value += 2
                elif current_symbol == 'X' and next_symbol == 'O':
                    heuristic_value += 1
                elif current_symbol == 'O' and next_symbol == 'O':
                    heuristic_value -= 2
                elif current_symbol == 'O' and next_symbol == 'X':
                    heuristic_value -= 1
            # heuristic function for crosses
            if opposite_player == 'X':
                if current_symbol == 'O' and next_symbol == 'O':
                    heuristic_value += 2
                elif current_symbol == 'O' and next_symbol == 'X':
                    heuristic_value += 1
                elif current_symbol == 'X' and next_symbol == 'X':
                    heuristic_value -= 2
                elif current_symbol == 'X' and next_symbol == 'O':
                    heuristic_value -= 1

    # adding the current computer points to the heuristic value for circles and crosses
    if opposite_player == 'O':
        heuristic_value += circle_points - cross_points
    elif opposite_player == 'X':
        heuristic_value += cross_points - circle_points

    return heuristic_value
