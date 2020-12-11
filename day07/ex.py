import re

class Bag():
    def __init__(self, identifier, graph):
        self.name = identifier
        self.collection = graph
        self.content = []
        self.containers = []
        self.content_amount = {}
        self.weight_mem = None

        self.already_counted = False

    def add_content(self, B, a):
        if not B in self.content:
            self.content.append(B)
            self.content_amount[B.name] = a

    def add_container(self, B):
        if not B in self.containers:
            self.containers.append(B)

    def is_in(self):
        self.already_counted = True
        res = []

        for B in self.containers:
            if not B.already_counted:
                res.append(B.name)
                res += B.is_in()

        return res

    def weight(self):
        if self.weight_mem != None:
            return self.weight_mem
        res = 1
        for B in self.content:
            res += self.content_amount[B.name] * B.weight()
        self.weight_mem = res

        print(f"A {self.name + ' ' * (16 - len(self.name))} bag contains exactly {res - 1}{' ' * (4 - len(str(res - 1)))} other bags inside it")

        return res


class Graph():
    def __init__(self):
        self.bags = {}

    def get_bag(self, b1):
        if not b1 in self.bags.keys():
            self.bags[b1] = Bag(b1, self)
        return self.bags[b1]

    def add_edge(self, b1, b2, a):
        B1 = self.get_bag(b1)
        B2 = self.get_bag(b2)

        B1.add_content(B2, a)
        B2.add_container(B1)


input = open('input.in','r')
lines = input.read().split('\n')[:-1]

collection = Graph()

for s in lines:

    m = re.search('(.+) bags contain (.+).', s)

    bag, content = m.groups()
    contents = content.split(", ")

    for c in contents:
        if c != "no other bags":
            amount, content = re.search('(\d+) (.+) bag', c).groups()
            collection.add_edge(bag, content, int(amount))

B = collection.get_bag("shiny gold")

print(f"\nQuestion 1 : A shiny gold bag can be inside {len(B.is_in())} possibilities for the outside-most bag\n")
print(f"\nQuestion 2 : A shiny gold bag contains exactly {B.weight() - 1} other bags\n")
