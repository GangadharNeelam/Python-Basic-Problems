def num(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
r = num(20, 56, 89)
print(r)
