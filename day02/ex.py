class PasswordChecker(object):
    old_correct_passwords = 0
    correct_passwords = 0

    def __init__(self, i1, i2, char, psswd):
        self.i1 = i1
        self.i2 = i2
        self.char = char
        self.psswd = psswd

    def old_psswd_check(self):
        if psswd.count(char) >= i1 and psswd.count(char) <= i2:
            PasswordChecker.old_correct_passwords += 1

    def psswd_check(self):
        if (psswd[self.i1 - 1] == char) ^ (psswd[self.i2 - 1] == char):
            PasswordChecker.correct_passwords += 1


import re
input = open('input.in','r')
lines = input.read().split('\n')[:-1]

for s in lines:

    m = re.search('(\w+)-(\w+) (\w): (\w+)', s)
    i1, i2, char, psswd = m.groups()
    i1, i2 = int(i1), int(i2)

    PC = PasswordChecker(i1, i2, char, psswd)
    PC.old_psswd_check()
    PC.psswd_check()

print(f"question 1 : {PasswordChecker.old_correct_passwords}")
print(f"question 2 : {PasswordChecker.correct_passwords}")
