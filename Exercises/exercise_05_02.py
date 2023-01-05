# exercise_05_02.py, Chapter 5, Python Crash Course
#
# More Conditional Tests: You don't have to limit the
# number of tests you create to 10. If you want to try
# more comparisons, write more tests and add them to 
# exercise_05_01.py. Have at least one True and one
# False result for each of the following:
#
#   - Tests for equality and inequality with strings

suv = 'durango'
print("Is suv == 'durango'? I predict True.")
print(suv == 'durango')

print("\nIs suv == 'audi'? I predict False.")
print(suv == 'audi')

#   - Tests using the lower() function

suv = 'Durango'
print("\nIs suv.lower() == 'durango'? I predict True.")
print(suv.lower() == 'durango')

#   - Numerical tests involving equality and inequality,
#     greater than and less than, greater than or equal
#     to, and less than or equal to

pi = 3.14159
print("\nIs pi == 3.14159? I predict True.")
print(pi == 3.14159)

print("\nIs pi != 3.14159? I predict False.")
print(pi != 3.14159)

print("\nIs pi > 3.14159? I predict False.")
print(pi > 3.14159)

print("\nIs pi < 3.14159? I predict False.")
print(pi < 3.14159)

print("\nIs pi >= 3.14159? I predict True.")
print(pi >= 3.14159)

print("\nIs pi <= 3.14159? I predict True.")
print(pi <= 3.14159)

#   - Tests using the and keyword and the or keyword

pi = 3.14
tau = 6.28

print("\nIs pi == 3.14 and tau == 6.28? I predict True.")
print(pi == 3.14 and tau == 6.28)

print("\nIs pi == 3.14 or tau != 6.28? I predict True.")
print(pi == 3.14 or tau != 6.28)

#   - Test whether an item is in a list

vip_list = ['william', 'matthew', 'jessie', 'stephanie']
vip = 'matthew'

if vip in vip_list:
    print("\n" + vip.title() + ", you are on the VIP list. Welcome!")

#   - Test whether an item is not in a list

not_vip = 'james'

if not_vip not in vip_list:
    print("\n" + not_vip.title() + ", you are not on the Vip list. Our apologies.")



