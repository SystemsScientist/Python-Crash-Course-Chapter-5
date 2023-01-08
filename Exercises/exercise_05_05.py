# exercise_05_05.py, Chapter 5, Python Crash Course
# 
# Alien Color #3: Turn your if-elif-else chain from exercise_05_04.py
# into an if-elif-else chain.

alien_color = 'green'

#   - If the alien is green, print a message that the player earned
#     5 points

if alien_color == 'green':
    print("You earned 5 points!")

#   - If the alien is yellow, print a message that the player earned
#     10 points

alien_color = 'yellow'

if alien_color == 'green':
    print("\nYou earned 5 points!")
elif alien_color == 'yellow':
    print("\nYou earned 10 points!")


#   - If the alien is red, print a message that the player earned
#     15 points

alien_color = 'red'

if alien_color == 'green':
    print("\nYou earned 5 points!")
elif alien_color == 'yellow':
    print("\nYou earned 10 points!")
elif alien_color == 'red':
    print("\nYou earned 15 points!")

#   - Write three versions of this program, making sure each 
#     message is printed for the appropriate color alien.

alien_color = 'green'

if alien_color == 'green':
    print("\nYou earned 5 points!")
elif alien_color == 'yellow':
    print("\nYou earned 10 points!")
else:
    print("\nYou earned 15 points!")


