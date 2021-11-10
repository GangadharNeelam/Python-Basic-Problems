# To find given number is armstrong or not

n = int(input("enter a number:"))
r = n
m = n
l = 0
while n:
    n = n//10
    l += 1
s = 0
while r:
    k = r%10
    s += k**l
    r = r//10
if s == m:
    print(m, "is an armstrong number")
else:
    print(m, "is not an armstrong number")

