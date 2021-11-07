def table(n):
    for i in range (1, 13):
        print(n, 'x', i, '=', n*i)

a = int(input())
b = int(input())
for i in range (a, b+1):
    table(i)
