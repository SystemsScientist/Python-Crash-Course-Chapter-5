# exercise_05_09.py, Chapter 5, Python Crash Course
# 
# No Users: Add an if test to exercise_05_08.py to
# make sure the list of users is not empty.

usernames = ['mahoney', 'hightower', 'jones',
             'tackleberry', 'hooks', 'fackler']

#   - If the list is empty, print the message "We
#     need to find some users!"

if usernames:
    for username in usernames:
        print("Hello, " + username.title() + "!")
        print("Thank you for logging in again!")
    print("Above is your list of users.")
else:
    print("We need to find some users.")

#   - Remove all of the usernames from your list,
#     and make sure the correct message is printed.

#     First - let's empty the list
for username in usernames[:]:
    usernames.remove(username)
print(usernames)

#     Second - let's check the list for users

if usernames:
    for username in usernames:
        print("Hello, " + username.title() + ".")
        print("Thank you for logging in again!.")
    print("Above is your lis tof users.")
else:
    print("We need to find some users!")



