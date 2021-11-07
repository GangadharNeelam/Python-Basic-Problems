def table(n):
    for i in range(1, 13):
        print(n, 'x', i, '=', n*i)

a = int(input('Enter a:'))
b = int(input('Enter b:'))
for i in range(a, b+1):
        table(i)
        

        
