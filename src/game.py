def get_opponent(player):
    return 'X' if player == 'O' else 'O'

import random
from minimax import Minimax
from alfabeta import Alfabeta

class Game:
    def __init__(self, length, algorithm):
        self.player = 'O'
        self.move_counter = 0

        self.has_ended = False
        self.state = ''.join(random.choice(['X', 'O']) for _ in range(length))
        self.circle_points = 0
        self.cross_points = 0

        if algorithm == 'minimax':
            self.algorithm = Minimax(self)
        else:
            self.algorithm = Alfabeta(self)

    def get_opponent(self):
        return get_opponent(self.player)

    def execute_move(self, index):
        move = self.state[index:index+2]

        if self.player == 'O' and move == 'XX':
            self.circle_points += 2
        elif self.player == 'O' and move == 'XO':
            self.cross_points -= 1
        elif self.player == 'X' and move == 'OO':
            self.cross_points += 2
        elif self.player == 'X' and move == 'OX':
            self.circle_points -= 1
        else:
            raise RuntimeError("Invalid game move")

        self.state = self.state[:index] + self.player + self.state[index+2:]
        self.player = self.get_opponent()
        self.move_counter += 1
        self.has_ended = self.player not in self.state[:-1]

    def generate_computer_move(self):
        # Temporary dummy implementation
        return self.algorithm.generate_move()
        # return self.state.find(self.get_opponent())
    
    def get_winner(self):
        if self.circle_points > self.cross_points:
            return 'O'
        elif self.circle_points < self.cross_points:
            return 'X'
        else:
            return "Neizšķirts"
        
