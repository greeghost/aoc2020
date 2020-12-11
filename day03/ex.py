class Forest():
    def __init__(self, pattern):
        # Initialized with a pattern derived from input.in
        # i.e. a list of same sized lists containing '#' or '.'
        self.height = len(pattern)
        self.width = len(pattern[0])
        self.pattern = pattern

    def __str__(self):
        # Debug and nice prints :)
        s = '\n'.join([''.join(l) for l in pattern])
        return s

class Wanderer():
    def __init__(self, forest):
        assert forest.height * forest.width == 0, "Empty Forest"
        assert forest.pattern[0][0] == '.', "Invalid Forest : Tree on Toboggan start"

        self.forest = forest
        self.x = 0
        self.y = 0
        self.injuries = 0

    def move(self, right, bottom):
        assert bottom > 0, "Negative slope"

        self.x = (self.x + right) % self.forest.width
        self.y = (self.y + bottom)
        if self.y < self.forest.height:
            if self.forest.pattern[self.y][self.x] == '#':
                self.injuries += 1

    def eval(self, right, bottom):
        assert bottom > 0, "Negative slope"

        while self.y < self.forest.height:
            self.move(right, bottom)
        res = self.injuries
        self.x, self.y, self.injuries = 0, 0, 0
        return res

pattern = [[*l] for l in open('input.in', 'r').read().split('\n')[:-1]]

W = Wanderer(Forest(pattern))

print(f"question 1 : {W.eval(3, 1)}")
print(f"question 2 : {W.eval(1, 1) * W.eval(3, 1) * W.eval(5, 1) * W.eval(7, 1) * W.eval(1, 2)}")
