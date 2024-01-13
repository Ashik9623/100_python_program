# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

#Conversion factor
conv_fac = 0.62171

# calculate miles
miles = kilometers * conv_fac
print("%0.2f kilometers is equal to %0.2f" %(kilometers, miles))