a = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
b = int(input("Enter the second number: "))
match operator:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/":
        result = a / b
    case _:
        print("please enter the vailed number or operator")
print(result)