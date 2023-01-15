#Simple Calculator
#1.ADD
#2.Subtract
#3.Multiply
#4.Divide


print("Select an operation to perform")
print("1.ADD")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

operation = input()

if operation == "1":
    num1= input("Enter first number here")
    num2= input("Enter second number")
    print("The sum is" , (int) (num1) + (int) (num2))

elif operation == "2":
    num1 = input("Enter first number here")
    num2 = input("Enter second number")
    print("The substraction is", (int) (num1) - (int) (num2))

elif operation == "3":
    num1 = input("Enter first number here")
    num2 = input("Enter second number")
    print("The product is" , (int) (num1) * (int) (num2))

elif operation == "4":
    num1 = input("Enter first number here")
    num2 = input("Enter second number")
    print("The division is", (int) (num1) / (int) (num2))
else:
    print("Invalid Entry")

