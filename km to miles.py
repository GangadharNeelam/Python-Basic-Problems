# Taking kilometers input from the user
k = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
m = k * conv_fac
print(k , 'kilometers is eqaul to', m, 'miles')
