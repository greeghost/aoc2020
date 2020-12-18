class Seats():
    def __init__(self, seats):
        self.seats = seats
        self.height = len(seats)
        self.width = len(seats[0])

    def getval(self, x, y):
        if x < 0:
            raise IndexError("Negative index for list assignment not allowed in this context")
        if y < 0:
            raise IndexError("Negative index for list assignment not allowed in this context")
        return self.seats[y][x]

    def setval(self, x, y, val):
        self.seats[y][x] = val

    def neighbors(self, x, y):
        if y == 0 and x == 0:
            return [self.getval(x + 1, y), self.getval(x + 1, y + 1), self.getval(x, y + 1)]
        if y == 0 and x == self.width - 1:
            return [self.getval(x, y + 1), self.getval(x - 1, y + 1), self.getval(x - 1, y)]
        if y == self.height - 1 and x == 0:
            return [self.getval(x, y - 1), self.getval(x + 1, y - 1), self.getval(x + 1, y)]
        if y == self.height - 1 and x == self.width - 1:
            return [self.getval(x, y - 1), self.getval(x - 1, y - 1), self.getval(x - 1, y)]
        if y == 0:
            return [self.getval(x - 1, y), self.getval(x - 1, y + 1), self.getval(x, y + 1), self.getval(x + 1, y + 1), self.getval(x + 1, y)]
        if y == self.height - 1:
            return [self.getval(x - 1, y), self.getval(x - 1, y - 1), self.getval(x, y - 1), self.getval(x + 1, y - 1), self.getval(x + 1, y)]
        if x == 0:
            return [self.getval(x, y - 1), self.getval(x + 1, y - 1), self.getval(x + 1, y), self.getval(x + 1, y + 1), self.getval(x, y + 1)]
        if x == self.width - 1:
            return [self.getval(x, y - 1), self.getval(x - 1, y - 1), self.getval(x - 1, y), self.getval(x - 1, y + 1), self.getval(x, y + 1)]
        return [self.getval(x, y - 1), self.getval(x + 1, y - 1), self.getval(x + 1, y), self.getval(x + 1, y + 1), self.getval(x, y + 1), self.getval(x - 1, y + 1), self.getval(x - 1, y), self.getval(x - 1, y - 1)]

    def visible(self, x, y):
        directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
        res = []
        # loc = []
        for dx, dy in directions:
            deltax = dx
            deltay = dy
            try:
                while self.getval(x + deltax, y + deltay) == '.':
                    deltax += dx
                    deltay += dy
                res.append(self.getval(x + deltax, y + deltay))
                # loc.append((x + deltax, y + deltay))
            except IndexError as e:
                pass
        # if (x, y) == (3, 8):
            # print(f"les visibles de {x, y} sont {loc}")
        return res

    def step(self, vf, threshold):
        # 'l' and '@' are temporary values for 'L' and '#'
        # # : occupied
        # L : empty
        changed = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.getval(x, y) == 'L':
                    v = vf(x, y)
                    if v.count('#') + v.count('l') == 0:
                        self.setval(x, y, '@')
                        changed += 1
                elif self.getval(x, y) == '#':
                    v = vf(x, y)
                    if v.count('#') + v.count('l') >= threshold:
                        self.setval(x, y, 'l')
                        changed += 1
        for x in range(self.width):
            for y in range(self.height):
                if self.getval(x, y) == 'l':
                    self.setval(x, y, 'L')
                elif self.getval(x, y) == '@':
                    self.setval(x, y, '#')
        return changed

    def print_layout(self):
        for l in self.seats:
            print(''.join(l))

    def simulate_seating(self, vf, t):
        while self.step(vf, t):
            pass
        cnt = 0
        for l in self.seats:
            for s in l:
                if s == '#':
                    cnt += 1
        return cnt



input = open('input.in','r')
lines = input.read().split('\n')[:-1]
seats = list(map(list, lines))


seat_layout = Seats([s[:] for s in seats])
q1 = seat_layout.simulate_seating(seat_layout.neighbors, 4)

seat_layout = Seats([s[:] for s in seats])
q2 = seat_layout.simulate_seating(seat_layout.visible, 5)

print(f"Question 1 : {q1}")
print(f"Question 2 : {q2}")
