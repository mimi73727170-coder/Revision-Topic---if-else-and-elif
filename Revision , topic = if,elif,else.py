# Practice Task - 1
age = eval(input("Enter your age :"))
if age >= 18 :
    print("Eligible for vote")
else :
    print("Not eligible for vote")

# Practice Task - 2
marks = eval(input("Enter marks :"))
if marks >= 90 :
    print("Excellent")
elif marks >= 75 :
    print("Very good")
elif marks >= 50 :
    print("Good")
else :
    print("Need improvement")

# Challenge 
print("A SIMPLE LOGIN SYSTEM")
username = input("Enter username :")
password = input("Enter password : ")
if username == "admin" and password == "python123" :
    print("Login successfully ")
elif username != "admin" :
    print("Invalid username")
elif password != "python123" :
    print("Invalid password")
