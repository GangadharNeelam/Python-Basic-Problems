#Electricity Bill
c=int(input('Customer ID:'))
u=float(input('Units consumed:'))
if u<=199:
    b=u*1.20
elif u>199 and u<400:
    b=u*1.50
elif u>400 and u<600:
    b=u*1.80
else:
    b=u*2.00
if b>400:
    s=0.15*b
    n=b+s
    print(c)
    print(u)
    print(b)
    print(s)
    print(n)

    
