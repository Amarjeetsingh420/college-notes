a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if(type(a)==int and type(b)==int and type(c)==int):
    if (a==b and b==c):
        print("all are equal")
    elif (a>=b and a>=c):
        print( a,"is greatest")
    elif (b<=a and b<=c):
        print( b,"is greatest")
    elif (b>=a and c>=a):
        print(c,"is greatest")
else:
    print("please enter an integer")