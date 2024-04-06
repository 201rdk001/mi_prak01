from tree import TreeNode, generate_tree
from game import get_opponent
from heuristic_function import heuristic_function

class MinimaxNode(TreeNode):
    def __init__(self, state, player, parent=None):
        TreeNode.__init__(self, state, player, parent)
        self.heuristic_value = None

class Minimax:
    def __init__(self, game):
        self.game = game

        self.root = None
        self.leafs = []
        self.path: list[MinimaxNode] = None

    def generate_move(self):
        if not self.root or not self.was_expected_move(self.path.pop()):
            self.run_algorithm()
            self.path.pop()

        return self.path.pop().changed_index

    def was_expected_move(self, expected):
        return \
            self.game.state == expected.state and \
            self.game.circle_points == expected.circle_points and \
            self.game.cross_points == expected.cross_points

    def calc_tree_depth(self):
        return 5 if len(self.game.state) < 20 else 4

    def run_algorithm(self):
        self.root = MinimaxNode(self.game.state, self.game.player)
        generate_tree(self.root, self.calc_tree_depth())

        self.evaluate_node(self.root, True)
        self.path = self.find_optimal_path(self.root.heuristic_value)
        # print([f'{n.circle_points}:{n.state}:{n.cross_points}' for n in self.path])
        # print([f'{n.state}:{n.changed_index}' for n in self.path])

    def evaluate_node(self, node, is_max):
        if len(node.children) == 0:
            self.leafs.append(node)
            node.heuristic_value = heuristic_function(node, get_opponent(self.game.player))
        elif is_max:
            node.heuristic_value = max([self.evaluate_node(c, False) for c in node.children])
        else:
            node.heuristic_value = min([self.evaluate_node(c, True) for c in node.children])

        return node.heuristic_value

    def find_optimal_path(self, best_heuristic_value):
        paths = []

        for leaf in self.leafs:
            node = leaf
            path = []

            if node.heuristic_value != best_heuristic_value:
                continue

            while node and node.heuristic_value == best_heuristic_value:
                path.append(node)
                node = node.parent

            if path[-1] == self.root:
                paths.append(path)

        return min(paths, key=len)
