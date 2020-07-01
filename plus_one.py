def plus_one(digits):
    s = ''
    res = []
    for i in digits:
        s += str(i)
    s = str(int(s) + 1)
    res = [int(i) for i in s]
    return res

digits = [9,9]
print(plus_one(digits))