from pprint import pprint
TBA = "TBA"


input = open('input.in', 'r').read().split('\n')[:-1]

answers = []
l = set()
for line in input:
    if line == '':
        answers.append(l.copy())
        l = set()
    else:
        l = l.union(set([*line]))
answers.append(l)
print(f"Question 1 : {sum((len(s) for s in answers))}") # 6878

answers = []
l = set([*"abcdefghijklmnopqrstuvwxyz"])
for line in input:
    if line == '':
        answers.append(l.copy())
        l = set([*"abcdefghijklmnopqrstuvwxyz"])
    else:
        l = l.intersection(set([*line]))
answers.append(l)
print(f"Question 1 : {sum((len(s) for s in answers))}") # 6878
