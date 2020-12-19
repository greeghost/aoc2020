import re

class Memory(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.mem = {}
        self.mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    def masked1(self, value):
        valbl = list(bin(value))[2:]
        val = ['0'] * (36 - len(valbl)) + valbl
        for i in range(len(val)):
            if self.mask[i] == 'X':
                continue
            val[i] = self.mask[i]
        return int("".join(val), 2)

    def set_mem(self, address, value):
        self.mem[address] = value

    def set_mask(self, value):
        self.mask = value

    def docking(self):
        return sum(self.mem.values())

    def v2_encode(self, address, value):
        add = list(bin(address))[2:]
        add = ['0'] * (36 - len(add)) + add
        for i in range(len(add)):
            if self.mask[i] == '0':
                continue
            else:
                add[i] = self.mask[i]
        self.set_mem_floating(add, value)

    def set_mem_floating(self, address, value):
        if not 'X' in address:
            add = int("".join(address), 2)
            self.set_mem(add, value)
        else:
            i = address.index('X')
            a1, a2 = address[:], address[:]
            a1[i] = '0'
            a2[i] = '1'
            self.set_mem_floating(a1, value)
            self.set_mem_floating(a2, value)


memory = Memory()

input = open('input.in','r')
lines = input.read().split('\n')[:-1]

pattern1 = re.compile(r"mask = ([0|1|X]*)")
pattern2 = re.compile(r"mem\[(\d*)\] = (\d*)")

for l in lines:
    if (m := pattern1.fullmatch(l)) != None:
        mask, = m.groups()
        memory.set_mask(mask)
    elif (m := pattern2.fullmatch(l)) != None:
        address, value = m.groups()
        memory.set_mem(address, memory.masked1(int(value)))
    else:
        print(f'Could not parse following line: "{l}"')

print(f"Question 1 : {memory.docking()}")

memory.reset()

for l in lines:
    if (m := pattern1.fullmatch(l)) != None:
        mask, = m.groups()
        memory.set_mask(mask)
    elif (m := pattern2.fullmatch(l)) != None:
        address, value = m.groups()
        memory.v2_encode(int(address), int(value))
    else:
        print(f'Could not parse following line: "{l}"')

print(f"Question 2 : {memory.docking()}")
