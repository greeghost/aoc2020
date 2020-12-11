class Xmas():
    def __init__(self, numbers):
        self.numbers = numbers
        self.decompositions = [(None, None) for _ in numbers]

        self.sums = self._get_sums()
        self.considered = numbers[0 : 25]
        self.pos = 25

    def _get_sums(self):
        sums = [numbers[0] for _ in self.numbers]
        for i in range(1, len(self.numbers)):
            sums[i] = sums[i - 1] + self.numbers[i]
        return sums

    def _find_sum(self, x):
        for i in range(len(self.sums)):
            for j in range(i + 1, len(self.sums)):
                if self.sums[j] - self.sums[i] == x:
                    return i, j
        return None

    def decompose(self):
        for i in self.considered:
            for j in self.considered:
                if i != j:
                    if i + j == self.numbers[self.pos]:
                        self.decompositions[self.pos] = (min(i, j), max(i, j))
                        self.considered = self.considered[1:] + [self.numbers[self.pos]]
                        self.pos += 1
                        return None
        return self.numbers[self.pos]

    def find_first_incoherence(self):
        while not (x := self.decompose()):
            pass
        return x

    def xmas_weakness(self, incoherence):
        i, j = self._find_sum(incoherence)
        interval = self.numbers[i + 1 : j + 1]
        return min(interval) + max(interval)


input = open('input.in','r')
lines = input.read().split('\n')[:-1]
numbers = list(map(int, lines))

xmas = Xmas(numbers)

q1 = xmas.find_first_incoherence()
q2 = xmas.xmas_weakness(q1)

print(f"Question 1 : {q1}")
print(f"Question 2 : {q2}")
