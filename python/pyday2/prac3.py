#Check whether a number is divisible by both 3 and 5.

num = int(input("Tell the number: "))

if num % 3 == 0 and num % 5 == 0:
    print("It is divided by both 3 and 5")
else:
    print("It is not")