input = open('input.in', 'r').read().split('\n')[:-1]
passports = []

# Recuperation des donnes
datas = {}
for line in input:
    if line == '':
        passports.append(datas.copy())
        datas = {}
    else:
        for duo in line.split():
            [field, value] = duo.split(':')
            datas[field] = value
passports.append(datas.copy())

# Verification des passeports
def check_passport_q1(p):
    return all([field in p for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
def check_passport_q2(p):
    # <editor-fold> (86 lines)
    # All fields are present
    if not all([field in p for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]):
        return False

    # byr is valid
    try:
        if int(p['byr']) < 1920:
            print(f"byr:{p['byr']}")
            return False
        if int(p['byr']) > 2002:
            print(f"byr:{p['byr']}")
            return False
    except Exception as e:
        print(f"byr:{p['byr']}")
        return False

    # iyr is valid
    try:
        if int(p['iyr']) < 2010:
            print(f"iyr:{p['iyr']}")
            return False
        if int(p['iyr']) > 2020:
            print(f"iyr:{p['iyr']}")
            return False
    except Exception as e:
        print(f"iyr:{p['iyr']}")
        return False

    # eyr is valid
    try:
        if int(p['eyr']) < 2020:
            print(f"eyr:{p['eyr']}")
            return False
        if int(p['eyr']) > 2030:
            print(f"eyr:{p['eyr']}")
            return False
    except Exception as e:
        print(f"eyr:{p['eyr']}")
        return False

    # hgt is valid
    unit = p['hgt'][-2:]
    if unit == 'cm':
        try:
            if int(p['hgt'][:-2]) < 150:
                print(f"hgt:{p['hgt']}")
                return False
            if int(p['hgt'][:-2]) > 193:
                print(f"hgt:{p['hgt']}")
                return False
        except Exception as e:
            print(f"hgt:{p['hgt']}")
            return False
    elif unit == 'in':
        try:
            if int(p['hgt'][:-2]) < 59:
                print(f"hgt:{p['hgt']}")
                return False
            if int(p['hgt'][:-2]) > 76:
                print(f"hgt:{p['hgt']}")
                return False
        except Exception as e:
            print(f"hgt:{p['hgt']}")
            return False
    else:
        print(f"hgt:{p['hgt']}")
        return False

    # hcl is valid
    if not (p['hcl'][0] == '#' and all([p['hcl'][i] in '1234567890abcdef' for i in range(1, 7)])):
        print(f"hcl:{p['hcl']}")
        return False

    # ecl is valid
    if not p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print(f"ecl:{p['ecl']}")
        return False

    # pid is valid
    if not (len(p['pid']) == 9 and all([i in '1234567890' for i in p['pid']])):
        print(f"pid:{p['pid']}")
        return False

    return True
    # </editor-fold>

valid1 = 0
valid2 = 0
for p in passports:
    valid1 += check_passport_q1(p)
    valid2 += check_passport_q2(p)

# Affichage des résultats
print(f"Question 1 : {valid1}")
print(f"Question 2 : {valid2}")
