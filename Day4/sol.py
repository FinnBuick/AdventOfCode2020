req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def isValid(passport):
    passport = set(passport)
    res = req_fields - passport
    res.discard('cid')
    if len(res) == 0:
        return True
    return False

with open("input.txt") as f:
    passports = [[y[0:3] for y in x.split()] for x in f.read().split("\n\n")]
    count = len(passports)
    for passport in passports:
        if not isValid(passport):
            count -= 1

    print(count)

