from tree import TreeNode, generate_tree, partial_regenerate_tree
from game import get_opponent
from heuristic_function import heuristic_function

class MinimaxNode(TreeNode):
    def __init__(self, state=None, player=None, parent=None, game=None):
        TreeNode.__init__(self, state, player, parent, game)
        self.heuristic_value = None

class Minimax:
    def __init__(self, game):
        self.game = game

        self.root = None
        self.leafs = []
        self.path = []
        self.visited_node_count = 0

    def generate_move(self):
        self.visited_node_count = 0

        if not self.root or not self.was_expected_move(self.path[-1]):
            self.run_algorithm()

        return self.path.pop().changed_index

    def are_nodes_equal(self, a, b):
        return \
            a.state == b.state and \
            a.circle_points == b.circle_points and \
            a.cross_points == b.cross_points

    def was_expected_move(self, expected):
        # Pārbauda, vai pēdējais gājiens atbilst gaidītajam
        return self.are_nodes_equal(self.game, expected)

    def calc_tree_depth(self):
        return 6 if len(self.game.state) < 20 else 5

    def prepare_tree(self):
        self.leafs = []

        if len(self.path) > 0 and self.path[-1].player == self.game.player:
            # Ģenerēt/paplašināt koku no neparedzētā gājiena virsones
            for child in self.path[-1].parent.children:
                if self.are_nodes_equal(self.game, child):
                    self.root = child
                    self.root.parent = None
                    partial_regenerate_tree(self.root, self.calc_tree_depth())
                    return

            raise RuntimeError("Player move missing")
        else:
            # Ģenerēt pilnīgi jaunu koku
            self.root = MinimaxNode(game=self.game)
            generate_tree(self.root, self.calc_tree_depth())

    def run_algorithm(self):
        # Izveido saknes mezglu un koku
        self.prepare_tree()
        # Izvērtē mezglus, izmantojot algoritmu
        self.evaluate_node(self.root, True)
        # Izvēlas optimālo (īsāko) uzvaras ceļu
        self.path = self.find_optimal_path(self.root.heuristic_value)
        self.path.pop()

    def evaluate_node(self, node, is_max):
        self.visited_node_count += 1

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
