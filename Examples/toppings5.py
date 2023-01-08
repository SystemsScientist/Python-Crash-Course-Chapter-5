# toppings5.py, Chapter 5, Python Crash Course
# program uses a list, for loop, and if-else
# block to check and print pizza toppings

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")



