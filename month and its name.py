m = int(input('Enter a month:'))
if m==4 or m==6 or m==8 or m==9 or m==11:
    print('month', m, 'has 30 days')
elif m==2:
    print('month', m, 'has 28 days')
elif m>12:
    print("There are only 12 months")
else:
    print('month', m, 'has 31 days')
