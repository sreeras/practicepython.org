from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

now = datetime.now()

print ("You will turn hundred in {0}".format((now.year-age)+100))