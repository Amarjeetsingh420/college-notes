s1 = int(input("Enter your first subject marks: "))
s2 = int(input("Enter your second subject marks: "))
s3 = int(input("Enter your third subject marks: "))
s4 = int(input("Enter your fourth subject marks: "))
s5 = int(input("Enter your fifth subject marks: "))
percentage = (s1+s2+s3+s4+s5)/5
if(percentage>=90):
    print("o grade")
elif(percentage>=81 and percentage<90):
    print("A+ grade")
elif(percentage>=71 and percentage<80):
    print("A grade")
elif(percentage>=61 and percentage<700):
    print("B grade")
elif(percentage<50):
    print("fail")
