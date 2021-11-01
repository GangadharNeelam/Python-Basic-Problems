r=int(input('Enter the roll number:'))

physics=int(input('Marks obtained in physics:'))
chemistry=int(input('Marks obtained in chemistry:'))
computers=int(input('Marks obtained in computer science:'))
t=physics+chemistry+computers
p=(t*100)/300
print('Total marks obtained in physics, chemistry computers science is', t)
print('Total percentage=', p)
if p>=80:
    print('First')
elif p>=70 and p<=79:
    print('Second')
elif p>=60 and p<=69:
    print('Third')
elif p>=50 and p<=59:
    print('Fourth')
elif p<=49:
    print('Fail')


