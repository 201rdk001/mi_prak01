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
        player = node.player_type
        move = node.state[i:i+2]

        if player == 'O' and move == 'XX':
            generate_tree(new_child(node, i, 2, 0), depth - 1)
        elif player == 'O' and move == 'XO':
            generate_tree(new_child(node, i, 0, -1), depth - 1)
        elif player == 'X' and move == 'OO':
            generate_tree(new_child(node, i, 0, 1), depth - 1)
        elif player == 'X' and move == 'OX':
            generate_tree(new_child(node, i, -1, 0), depth - 1)
