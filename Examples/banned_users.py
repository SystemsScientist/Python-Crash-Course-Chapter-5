# banned_users.py, Chapter 5, Python Crash Course
# program uses an if statement and "not in" keywords
# to check whether a user has been banned

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")




