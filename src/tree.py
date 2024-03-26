class PlayerType:
    CROSS = 'X'
    CIRCLE = 'O'

class TreeNode:
    def __init__(self, state, player_type):
        self.state = state
        self.player_type = player_type
        self.children = []
        self.parent = None
        self.cross_points = 0
        self.circle_points = 0

def calculate_points(node):
    cross_count = node.state.count(PlayerType.CROSS)
    circle_count = node.state.count(PlayerType.CIRCLE)
    node.cross_points = cross_count - circle_count
    node.circle_points = circle_count - cross_count

def generate_tree(node, depth):
    if depth <= 0:
        return

    if node.player_type == PlayerType.CIRCLE:
        for i in range(len(node.state) - 1):
            if node.state[i:i+2] == 'XX':
                new_state = node.state[:i] + PlayerType.CIRCLE + node.state[i+2:]
                child = TreeNode(new_state, PlayerType.CROSS)
                child.parent = node
                node.children.append(child)
                calculate_points(child)
                generate_tree(child, depth - 1)
                child.circle_points -= 1
                child.cross_points += 3
            elif node.state[i:i+2] == 'XO':
                new_state = node.state[:i] + PlayerType.CIRCLE + node.state[i+2:]
                child = TreeNode(new_state, PlayerType.CROSS)
                child.parent = node
                node.children.append(child)
                calculate_points(child)
                generate_tree(child, depth - 1)
                child.circle_points -= 1

    elif node.player_type == PlayerType.CROSS:
        for i in range(len(node.state) - 1):
            if node.state[i:i+2] == 'OO':
                new_state = node.state[:i] + PlayerType.CROSS + node.state[i+2:]
                child = TreeNode(new_state, PlayerType.CIRCLE)
                child.parent = node
                node.children.append(child)
                calculate_points(child)
                generate_tree(child, depth - 1)
                child.cross_points -= 2
                child.circle_points += 3
                

            elif node.state[i:i+2] == 'OX':
                new_state = node.state[:i] + PlayerType.CROSS + node.state[i+2:]
                child = TreeNode(new_state, PlayerType.CIRCLE)
                child.parent = node
                node.children.append(child)
                calculate_points(child)
                generate_tree(child, depth - 1)
                child.cross_points -= 1

                

def print_tree(node, level=0):
    if node is not None:
        print("  " * level + node.state + " - Circle: " + str(node.circle_points) + ", Cross: " + str(node.cross_points))

        for child in node.children:
            print_tree(child, level + 1)

# Example usage:
root_state = "XXOOXOOX"
root_player_type = PlayerType.CROSS
root_node = TreeNode(root_state, root_player_type)
calculate_points(root_node)
generate_tree(root_node, 1)
print_tree(root_node)
