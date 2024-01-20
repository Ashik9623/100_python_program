def compute_hsf(x,y):
    
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

print("The H.C.F is", compute_hsf(num1, num2))
    
