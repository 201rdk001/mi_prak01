from game import get_opponent

class TreeNode:
    def __init__(self, state, player, parent=None):
        self.player = player
        self.state = state
        self.cross_points = 0 if not parent else parent.cross_points
        self.circle_points = 0 if not parent else parent.circle_points

        self.height = 1 if not parent else parent.height + 1
        self.parent = parent
        self.children = []

        self.changed_index = -1

def new_child(node, i, circle_points_diff, cross_points_diff):
    new_state = node.state[:i] + node.player + node.state[i+2:]

    child = type(node)(new_state, get_opponent(node.player), node)
    child.circle_points += circle_points_diff
    child.cross_points += cross_points_diff
    child.changed_index = i
    node.children.append(child)

    return child


def generate_tree(node, depth):
    if depth <= 0:
        return

    for i in range(len(node.state) - 1):
        player = node.player
        move = node.state[i:i+2]

        if player == 'O' and move == 'XX':
            generate_tree(new_child(node, i, 2, 0), depth - 1)
        elif player == 'O' and move == 'XO':
            generate_tree(new_child(node, i, 0, -1), depth - 1)
        elif player == 'X' and move == 'OO':
            generate_tree(new_child(node, i, 0, 2), depth - 1)
        elif player == 'X' and move == 'OX':
            generate_tree(new_child(node, i, -1, 0), depth - 1)
