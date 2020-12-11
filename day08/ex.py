import re

ACC = 'acc'
NOP = 'nop'
JMP = 'jmp'

class Command():
    def __init__(self, command, modifier):
        self.command = command
        self.modifier = modifier

    def __str__(self):
        return f"{self.command} {self.modifier}"

class Program():
    def __init__(self, commands):
        self.commands = commands
        self.accu = 0
        self.pos = 0

        self.visited = [0 for c in commands]

    def reset(self):
        self.accu = 0
        self.pos = 0
        self.visited = [0 for c in commands]


    def step(self):
        self.visited[self.pos] += 1
        if self.commands[self.pos].command == ACC:
            self.accu += self.commands[self.pos].modifier
            self.pos += 1
        elif self.commands[self.pos].command == NOP:
            self.pos += 1
        elif self.commands[self.pos].command == JMP:
            self.pos += self.commands[self.pos].modifier

    def eval(self):
        i = 0

        while(self.pos < len(self.commands)):
            self.step()
            i += 1

            if i >= len(self.commands) + 1:
                return 0

        return self.accu

    def loop(self):
        try:
            while not self.visited[self.pos]:
                self.step()
            return True
        except IndexError as e:
            return False

    def question1(self):
        self.loop()
        return self.accu

    def question2(self):
        for i, c in enumerate(self.commands):
            self.reset()
            if c.command == JMP:
                self.commands[i].command = NOP
                if not self.loop():
                    return self.accu
                self.commands[i].command = JMP
            elif c.command == NOP:
                self.commands[i].command = JMP
                if not self.loop():
                    return self.accu
                self.commands[i].command = NOP


commands = []

input = open('input.in','r')
lines = input.read().split('\n')[:-1]
for s in lines:
    m = re.search('(\w+) (.+)', s)
    command, number = m.groups()
    commands.append(Command(command, int(number)))

p = Program(commands)


print(p.question1())
print(p.question2())
