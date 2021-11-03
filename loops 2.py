a = int(input('Enter a:'))
b = int(input('Enter b:'))
while a<=b:
    if a%3==0  or a%5==0:
        print(a, end=',')
    a += 1
