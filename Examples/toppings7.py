# toppings7.py, Chapter 5, Python Crash Course
# program uses multiple lists, a for loop, and
# an if-else block to check the availability of
# pizza toppings

available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")



