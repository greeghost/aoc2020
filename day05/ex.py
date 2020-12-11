input = open('input.in', 'r').read().split('\n')[:-1]


def get_id(boarding_pass):
    FB = boarding_pass[:-3]
    LR = boarding_pass[-3:]

    lb1, hb1 = 0, 127
    lb2, hb2 = 0, 7

    for char in FB:
        if char == 'F':
            hb1 -= (hb1 - lb1 + 1) // 2
        else:
            lb1 += (hb1 - lb1 + 1) // 2

    for char in LR:
        if char == 'L':
            hb2 -= (hb2 - lb2 + 1) // 2
        else:
            lb2 += (hb2 - lb2 + 1) // 2

    return 8 * lb1 + lb2

ids = sorted(list(map(get_id, input)))

print(ids)

res = 0
for i in range(len(ids) - 1):
    if ids[i + 1] - ids[i] >= 2:
        print(ids[i], ids[i + 1])
        res = ids[i] + 1

print(f"Question 1 : {max(ids)}")
print(f"Question 2 : {res}")
