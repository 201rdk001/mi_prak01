import random


# So far it's a prototype of what it should be.



def game_mode(mode: int):
    # If the player has chosen to play with the computer
    if mode == 0:

        pass
    
    # If the player has chosen to play with the other player
    else:
        game()



def generate_symbols(length: int):
    return ''.join(random.choice(['X', 'O']) for _ in range(length))




def print_game_string(state, score_o, score_x):
    print("Game string: ", state)

    # These metrics can be displayed in the interface, just like a game string.
    # ||
    # \/
    print(f"Score - O: {score_o}, X: {score_x}")


def find_moves(state, symbol):
    moves = []
    if symbol == 'O':
        patterns = ['XX', 'XO']
    else:
        patterns = ['OO', 'OX']
    
    for pattern in patterns:
        start = 0
        while start < len(state):
            idx = state.find(pattern, start)
            if idx == -1:
                break
            moves.append((idx, pattern))
            start = idx + 1
    return moves


def edit_game_string(state, move):
    idx, pattern = move
    new_symbol = 'O' if 'X' not in pattern else 'X'
    new_state = state[:idx] + new_symbol + state[idx+len(pattern):]
    return new_state

def update_scores(symbol, pattern, score_o, score_x):
    if symbol == 'O':
        if pattern == 'XX':
            score_o += 2
        else:
            score_x -= 1
    else:
        if pattern == 'OO':
            score_x += 2
        else:
            score_o -= 1
    return score_o, score_x


def game():
    length = int(input("Enter the length of the symbol string (15-25): "))
    if length < 15 or length > 25:
        print('Error')
        return
    state = generate_symbols(length)
    score_o, score_x = 0, 0
    current_symbol = 'O'
    
    while True:
        moves = find_moves(state, current_symbol)
        if not moves:
            print("No moves left. Game over.")
            break
        

        print(f"Player {current_symbol} moves:")

        i = 0
        for move in moves:
            print(f"{i}) Index: {move[0]} {move[1]}")
            i += 1
        
        print_game_string(state, score_o, score_x)

        print(f"Player {current_symbol}, choose your move (0-{len(moves)-1}): ")

        # The point where the symbol index is specified.
        move_idx = int(input())

        move = moves[move_idx]
        state = edit_game_string(state, move)
        score_o, score_x = update_scores(current_symbol, move[1], score_o, score_x)
        
        if len(set(state)) == 1:
            # GAME OVER status
            print("Only one symbol left.\nGame over!")
            break
        
        current_symbol = 'O' if current_symbol == 'X' else 'X'
    
    print_game_string(state, score_o, score_x)


    # Game results
    if score_o > score_x:
        print("O wins!")
    elif score_x > score_o:
        print("X wins!")
    else:
        print("Tie!")


def logic_main():
    mode = int(input("Play with a computer(0) or with a player(1): "))
    if mode < 0 or mode > 1:
        print('Error')
        return
    game_mode(mode)


if __name__ == "__main__":
    logic_main()









