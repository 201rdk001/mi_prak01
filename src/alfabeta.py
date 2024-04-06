from tree import TreeNode, generate_tree
from game import get_opponent
from heuristic_function import heuristic_function

TREE_DEPTH = 7

class AlfabetaNode(TreeNode):
    def __init__(self, state, player, parent=None):
        TreeNode.__init__(self, state, player, parent)
        self.heuristic_value = None

class Alfabeta:
    def __init__(self, game):
        self.game = game

        self.root = None
        self.leafs = []
        self.path = None

    def generate_move(self):
        if not self.root or not self.was_expected_move(self.path.pop()):
            self.run_algorithm()
            self.path.pop()

        return self.path.pop().changed_index

    def was_expected_move(self, expected):
        # Pārbauda, vai pēdējais gājiens atbilst gaidītajam
        return \
            self.game.state == expected.state and \
            self.game.circle_points == expected.circle_points and \
            self.game.cross_points == expected.cross_points

    def calc_tree_depth(self):
        return 5 if len(self.game.state) < 20 else 4

    def run_algorithm(self):
        # Izveido saknes mezglu un koku
        self.root = AlfabetaNode(self.game.state, self.game.player)
        generate_tree(self.root, self.calc_tree_depth())

        # Izvērtē mezglus, izmantojot algoritmu
        self.evaluate_node(self.root, True, float('-inf'), float('inf'))
        self.path = self.find_optimal_path(self.root.heuristic_value)

    def evaluate_node(self, node, is_max, alpha, beta):
        if len(node.children) == 0:
            self.leafs.append(node)
            node.heuristic_value = heuristic_function(node, get_opponent(self.game.player))
        elif is_max:
            node.heuristic_value = float('-inf')
            for child in node.children:
                node.heuristic_value = max(node.heuristic_value, self.evaluate_node(child, False, alpha, beta))
                alpha = max(alpha, node.heuristic_value)
                if beta <= alpha:
                    break
        else:
            node.heuristic_value = float('inf')
            for child in node.children:
                node.heuristic_value = min(node.heuristic_value, self.evaluate_node(child, True, alpha, beta))
                beta = min(beta, node.heuristic_value)
                if beta <= alpha:
                    break

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
