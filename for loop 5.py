a = int(input('Enter a:'))
b = int(input('Enter b:'))
for i in range(a, b):
    for s in range(1, 13):
        print(i, 'x', s, '=', s*i)
