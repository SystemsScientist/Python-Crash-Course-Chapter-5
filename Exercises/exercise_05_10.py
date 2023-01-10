# exercise_05_10.py, Chapter 5, Python Crash Course
#
# Checking Usernames: Do the following to create a program
# that simulates how websites ensure that everyone has a
# unique username.

#   - Make a list of five or more usernames called 
#     current_users.

current_users = ['mahoney', 'hightower', 'jones',
            'tackleberry', 'hooks']

#   - Make another list of five usernames called new_users.
#     Make sure one or two of the new usernames are also in
#     the current_users list.

new_users = ['jones', 'hooks', 'thompson',
             'martin', 'fackler', 'barbara']

#   - Loop through the new_users list to see if each new
#     username has already been used. If it has, print a
#     message that the person will need to enter a new
#     username. If a username has not been used, print a
#     message saying that the username is available.

for new_user in new_users:
    if new_user in current_users:
        print(new_user.title() + " is not available.")
        print("You will need to enter a different username.")
    else:
        print(new_user.title() + " is available!")

#   - Make sure your comparison is case insensitive. If
#     'John' has been used, 'JOHN' should not be accepted.

print("\n")
new_users = ['Jones', 'HOOKS', 'thompson',
             'martin', 'fackler', 'barbara']
for new_user in new_users:
    if ((new_user.lower() in current_users) or (new_user.upper() in current_users) or (new_user.title() in current_users)):
        print(new_user.title() + " is not available.")
        print("You will need to enter a different username.")
    else:
        print(new_user.title() + " is available!")



