a = int(input("Enter first side length: "))
b = int(input("Enter second side length: "))
c = int(input("Enter third side length: "))
if(type(a)==int and type(b)==int and type(c)==int):
    if (a==b and b==c):
        print("equilateral")
    elif (a!=b and b!=c and c!=a):
        print("scalene")
    elif (b<=a and b<=c):
        print( b,"is greatest")
    elif (a==b or b==c or c==a):
        print("isosceles")
else:
    print("please enter length in integer")