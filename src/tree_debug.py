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
                generate_tree(new_child(node, i, 0, 1), depth - 1)
            elif node.state[i:i+2] == 'OX':
                generate_tree(new_child(node, i, -1, 0), depth - 1)


def print_tree(node, level=0):
    if node is not None:
        print('  ' * level + node.state + ' - Circle: ' +
              str(node.circle_points) + ', Cross: ' + str(node.cross_points))

        for child in node.children:
            print_tree(child, level + 1)

def generate_tree_graph(n, i=0, graph=''):
    if i == 0:
        graph += 'digraph {\n'
        graph += 'node [shape=record]\n'

    idx = n.changed_index

    if idx > -1:
        state = n.state[:idx] + f'<u>{n.state[idx]}</u>' + n.state[idx+1:]
    else:
        state= n.state

    graph += f'n{i} [label=<{n.circle_points}|{state}|{n.cross_points}>]\n'

    ni = i + 1
    for c in n.children:
        graph += f'n{i} -> n{ni}\n'
        graph, ni = generate_tree_graph(c, ni, graph)

    if i == 0:
        graph += '}'
        return graph

    return graph, ni

# Example usage:
root_state = 'XXOOXOOX'
root_player_type = 'O'
root_node = TreeNode(root_state, root_player_type)
generate_tree(root_node, 1)
print(generate_tree_graph(root_node))
