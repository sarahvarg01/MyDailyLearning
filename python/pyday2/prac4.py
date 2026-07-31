#Enter marks and print:
#90–100 → A
#80–89 → B
#70–79 → C
#Below 70 → Fail 

marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    print("A")
elif 80 <= marks < 90:
    print("B")
elif 70 <= marks < 80:
    print("C")
else:
    print("Fail")

