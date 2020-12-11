class Adapters():
    def __init__(self, numbers):
        self.raw_numbers = sorted(numbers)
        self.numbers = [0] + self.raw_numbers + [self.raw_numbers[-1] + 3]
        self.gaps = [self.numbers[i] - self.numbers[i - 1] for i in range(1, len(self.numbers))]
        self.flattened = self.flatten()

    def chain_value(self):
        return self.gaps.count(1) * self.gaps.count(3)

    def flatten(self):
        l = []
        i = 0
        cnt = 0
        while i < len(self.gaps):
            # The chain only consists of 1s and 3s
            if self.gaps[i] == 1:
                cnt += 1
                i += 1
            elif self.gaps[i] == 3:
                if cnt != 0:
                    l.append(cnt)
                    cnt = 0
                i += 1
        return l

    def eval_flat(self):
        l = list(map(eval, self.flattened))
        res = 1
        for i in l:
            res *= i
        return res

# TODO : changer le 50 pour max(adapters.flattened)
l = ["If this value is ever called, then something went **really** wrong...", 1, 2, 4] + [0 for i in range(50)]
def eval(n):
    if l[n]:
        return l[n]
    res = eval(n - 1) + eval(n - 2) + eval(n - 3)
    l[n] = res
    return res

adapters = Adapters(list(map(int, open('input.in','r').read().split('\n')[:-1])))

q1 = adapters.chain_value()
q2 = adapters.eval_flat()

print(f"Question 1 : {q1}")
print(f"Question 2 : {q2}")
