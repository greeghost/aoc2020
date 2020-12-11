input = open('input.in','r')
l = list(map(int, input.read().split('\n')[:-1]))

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[j] + l[i] == 2020:
            print(f"question 1 : {l[i] * l[j]}")

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            if l[j] + l[i] + l[k] == 2020:
                print(f"question 2 : {l[i] * l[j] * l[k]}")
