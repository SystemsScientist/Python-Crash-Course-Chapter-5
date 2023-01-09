# exercise_05_08.py, Chapter 5, Python Crash Course
#
# Hello Admin: Make a list of five or more usernames,
# including the name 'admin'. Imagine you are writing
# code that will print a greeting to each user after
# they log in to a website. Loop through the list, and
# print a greeting to each user.

usernames = ['mahoney', 'thompson', 'hightower',
             'jones', 'tackleberry', 'hooks', 'martin',
             'fackler', 'barbara', 'admin']

#   - If the username is 'admin', print a special
#     greeting, such as "Hello admin, would you like
#     to see a status report?"

if 'admin' in usernames:
    print("Hello, Admin! Would you like to see a status report?\n")

#   - Otherwise, print a generic greeting, such as
#     "Hello Eric, thank you for logging in again."

if usernames:
    for username in usernames:
        if username != 'admin':
            print("Hello " + username.title() + "! Thank you for logging in again!")



