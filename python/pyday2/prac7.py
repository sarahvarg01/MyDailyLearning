#Ask for a username and password. Print "Login Successful" if both are correct; 
# otherwise print "Invalid Credentials".

username = input("Enter username: ")
password = input("Enter password: ")

if username == "mereena" and password == "pas123":
    print("Login Successful")
else:
    print("Invalid Credentials")