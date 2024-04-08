from game import get_opponent


class TreeNode:
    def __init__(self, state, player, parent=None, game=None):
        if game:
            self.state = game.state
            self.player = game.player
            self.circle_points = game.circle_points
            self.cross_points = game.cross_points
        else:
            self.state = state
            self.player = player

            if parent:
                self.circle_points = parent.circle_points
                self.cross_points = parent.cross_points
            else:
                self.circle_points = 0
                self.cross_points = 0

        self.changed_index = -1
        self.parent = parent
        self.children = []

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


def partial_regenerate_tree(node, depth):
    node.clear_calculated_values()

    if len(node.children) > 0:
        for child in node.children:
            partial_regenerate_tree(child, depth - 1)
    else:
        generate_tree(node, depth - 1)
