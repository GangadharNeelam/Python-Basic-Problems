#Spy number
n = int(input('Enter  number:'))
s = 0
g = 1
k = n
while n:
    r = n%10
    s += r
    g *= r
    n = n//10
if g==s:
    print(k, 'is a spy number')
else:
    print(k, 'is not a spy number')
