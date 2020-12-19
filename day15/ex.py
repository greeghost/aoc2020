import re

class MemoryGame(object):
    def __init__(self, numbers):
        self.initialization = numbers
        self.reset()

    def reset(self):
        self.turn = 1
        self.last = self.initialization[-1]
        self.new = 0 if not self.initialization[-1] in self.initialization[:-2] else self.initialization[::-1].index(self.last)
        self.history = {}
        for n in self.initialization:
            self.history[n] = self.turn
            self.turn += 1

    def new_turn(self, t):
        self.last = t
        res = self.turn - self.history[t] if t in self.history else 0
        self.history[t] = self.turn
        self.turn += 1
        return res

    def simulate_game(self, n):
        while self.turn <= n:
            self.new = self.new_turn(self.new)
        return self.last



input = open('input.in','r')
lines = input.read().split('\n')[:-1]
numbers = list(map(int, lines[0].split(', ')))

mg = MemoryGame(numbers)
print(f"Question 1 : {mg.simulate_game(2020)}")
mg.reset()
print(f"Question 1 : {mg.simulate_game(30000000)}")
