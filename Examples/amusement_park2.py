# amusement_park2.py, Chapter 5, Python Crash Course
# program uses an if-elif-else block to test a variable

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")



