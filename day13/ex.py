input = open('input.in','r')
lines = input.read().split('\n')[:-1]

arrival = int(lines[0])
raw_ids = lines[1].split(',')

ids = [(int(i) if i != 'x' else i) for i in raw_ids ]
times_to_wait = [(i - (arrival % i) if i != 'x' else 'x') for i in ids ]

mint = float("+inf")
mini = 0
for i, t in zip(ids, times_to_wait):
    if t != 'x':
        if t < mint:
            mint = t
            mini = i

print(f"Question 1 : {mint * mini}")

def bezout(a, b):
    if b == 0:
        return 1, 0
    u, v = bezout(b, a % b)
    return v, u -  (a // b) * v

from math import gcd, lcm

def solve_two_equation_system(a, b, p, q):
    # return k, m with x = k mod m
    if gcd(int(p), int(q)) == 1:
        u, v = bezout(p, q)
        return (p * u * (b - a) + a) % (p * q), p * q
    else:
        print("WARNING : FLAWS !!")
        u, v = bezout(p, q)
        d = gcd(p, q)
        return (p * u * (b - a) + a) / d, p * q / d ** 2

def solve_n_systems(As, Ps):
    k, m = As[0], Ps[0]
    for i, j in zip(As, Ps):
        if (i, j) == (k, m):
            continue
        k, m = solve_two_equation_system(k, i, m, j)
    return k, m

As, Ps = [], []
cnt = 0
for i in range(len(ids)):
    if ids[i] != 'x':
        As.append(-i)
        Ps.append(ids[i])

k, m = solve_n_systems(As, Ps)
print(f"Question 2 : {k % m}")
