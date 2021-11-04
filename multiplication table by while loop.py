#Multipliaction table by using while loop

a = int(input('Enter a:'))
b = int(input('Énter b:'))
i = 1
while i<=b:
    print(a, '*', i, '=', a*i)
    if i>=5:
        break
    i += 1
