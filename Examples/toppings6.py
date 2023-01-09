# toppings6.py, Chapter 5, Python Crash Course
# program checks for an empty list by using a
# a list, an if-else block, and a for loop

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")



