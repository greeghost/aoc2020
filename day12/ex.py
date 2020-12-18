EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

FORWARD = 'F'

LEFT = 'L'
RIGHT = 'R'

class Ship():
    def __init__(self, instrs):
        self.x = 0
        self.y = 0
        self.instructions = instrs

        self.facing = EAST

        self.wx = 10
        self.wy = 1

    def turn(self, angle):
        self.facing = (self.facing + angle / 90) % 4

    def forward(self, val):
        if self.facing == EAST:
            self.x += val
        elif self.facing == NORTH:
            self.y += val
        elif self.facing == WEST:
            self.x -= val
        elif self.facing == SOUTH:
            self.y -= val

    def move(self, direction, val):
        directions = ['E', 'N', 'W', 'S']
        if directions.index(direction) == EAST:
            self.x += val
        elif directions.index(direction) == NORTH:
            self.y += val
        elif directions.index(direction) == WEST:
            self.x -= val
        elif directions.index(direction) == SOUTH:
            self.y -= val

    def follow_instruction(self, instr, t, f, m):
        if instr[0] == 'L':
            t(self, instr[1])
        elif instr[0] == 'F':
            f(self, instr[1])
        else:
            m(self, instr[0], instr[1])

    def simulate(self, t, f, m):
        oldx, oldy = self.x, self.y
        for instr in self.instructions:
            self.follow_instruction(instr, t, f, m)
        return oldx - self.x, oldy - self.y

    def question1(self):
        a, b = self.simulate(Ship.turn, Ship.forward, Ship.move)
        return abs(a) + abs(b)

    def turn_waypoint(self, angle):
        for i in range(int(self.facing + angle / 90) % 4):
            tmp = self.wy
            self.wy = self.wx
            self.wx = -tmp

    def forward_to_waypoint(self, val):
        self.x += val * self.wx
        self.y += val * self.wy

    def move_waypoint(self, direction, val):
        directions = ['E', 'N', 'W', 'S']
        if directions.index(direction) == EAST:
            self.wx += val
        elif directions.index(direction) == NORTH:
            self.wy += val
        elif directions.index(direction) == WEST:
            self.wx -= val
        elif directions.index(direction) == SOUTH:
            self.wy -= val

    def question2(self):
        a, b = self.simulate(Ship.turn_waypoint, Ship.forward_to_waypoint, Ship.move_waypoint)
        return abs(a) + abs(b)



input = open('input.in','r')
lines = input.read().split('\n')[:-1]

for i in range(len(lines)):
    instr, val = lines[i][0], int(lines[i][1:])
    if instr == RIGHT:
        instr = LEFT
        val = 360 - val
    lines[i] = instr, val

print(f"Question 1 : {Ship(lines).question1()}")
print(f"Question 2 : {Ship(lines).question2()}")
