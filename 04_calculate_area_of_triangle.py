a = float(input('Enter your first side:'))
b = float(input('Enter your second side:'))
c = float(input('Enter your third side:'))

#calculate the semi-perimeter
s = (a + b +c) / 2

#Calculate the area 
area = (s*(s - a)*(s-b)*(s -c))**0.5
print('The area of the triangle is %0.2f' %area)