#Find the largest of three numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num2 < num1 > num3:
    print("First number is largest")
elif num1 < num2 > num3:
    print("Second number is largest")
else:
    print("Third number is largest")