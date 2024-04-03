class TreeNode:
    def __init__(self, state, player_type, parent=None):
        self.player_type = player_type
        self.state = state
        self.children = []
        self.parent = parent
        self.cross_points = 0 if not parent else parent.cross_points
        self.circle_points = 0 if not parent else parent.circle_points
        self.changed_index = -1


def opposite_player(player):
    return 'X' if player == 'O' else 'O'


def new_child(node, i, circle_points_diff, cross_points_diff):
    new_state = node.state[:i] + node.player_type + node.state[i+2:]

    child = TreeNode(new_state, opposite_player(node.player_type), node)
    child.circle_points += circle_points_diff
    child.cross_points += cross_points_diff
    child.changed_index = i
    node.children.append(child)

    return child


def generate_tree(node, depth):
    if depth <= 0:
        return

    for i in range(len(node.state) - 1):
        if node.player_type == 'O':
            if node.state[i:i+2] == 'XX':
                generate_tree(new_child(node, i, 2, 0), depth - 1)
            elif node.state[i:i+2] == 'XO':
                generate_tree(new_child(node, i, 0, -1), depth - 1)

        elif node.player_type == 'X':
            if node.state[i:i+2] == 'OO':
                generate_tree(new_child(node, i, 0, 2), depth - 1)
            elif node.state[i:i+2] == 'OX':
                generate_tree(new_child(node, i, -1, 0), depth - 1)


def print_tree(node, level=0):
    if node is not None:
        print('  ' * level + node.state + ' - Circle: ' +
              str(node.circle_points) + ', Cross: ' + str(node.cross_points))

        for child in node.children:
            print_tree(child, level + 1)


def generate_tree_graph(n, depth, current_depth=0, i=0, graph=''):
    if i == 0:
        graph += 'digraph {\n'
        graph += 'node [shape=record]\n'

    idx = n.changed_index

    if idx > -1:
        state = n.state[:idx] + f'{n.state[idx]}' + n.state[idx+1:]
    else:
        state= n.state
    
    node_heuristic_value = 0
    if not n.children:
        node_heuristic_value = heuristic_function(n)
        graph += f'n{i} [label = <{n.circle_points}|{state}|{n.cross_points} / (depth:{current_depth}) / (h_value:{node_heuristic_value})>]\n'
    else:
        graph += f'n{i} [label = <{n.circle_points}|{state}|{n.cross_points} / (depth:{current_depth})>]\n'

    ni = i + 1
    for c in n.children:
        graph += f'n{i} -> n{ni}\n'
        graph, ni = generate_tree_graph(c, depth, current_depth + 1, ni, graph)

    if i == 0:
        graph += '}'
        return graph

    return graph, ni


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


def heuristic_function(node):
    state = node.state
    circle_points = node.circle_points
    cross_points = node.cross_points
    player_type = node.player_type
    opposite_player = opposite_player_type
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


# Example usage:
root_state = 'XOXXOO'
root_player_type = 'O'
opposite_player_type = 'X'
root_node = TreeNode(root_state, root_player_type)
generate_tree(root_node, 3)
print(generate_tree_graph(root_node, 3))
