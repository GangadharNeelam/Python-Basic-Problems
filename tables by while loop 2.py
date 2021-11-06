a = int(input("Enter a:"))
b = int(input("Enter b:"))
while a<=b:
    i = 18 #from 18 --> 1
    while i>=1:
        print(b, "x", i, "=", b*i)
        i -= 1 
    print()
    b -= 1 #from b -->a
