# exercise_05_04.py, Chapter 5, Python Crash Course
#
# Alien Colors #2: Choose a color for an alient as you
# did in exercise_05_03.py, and write an if-else chain.

alien_color = 'green'

#   - If the alien's color is green, print a statement
#     that the player just earned 5 points for shooting
#     the alien. 

if alien_color == 'green':
    print("You just earned 5 points!")

#   - If the alien's color isn't green, print a statement
#     that the player just earned 10 points.

alien_color = 'red'

if alien_color != 'green':
    print("\nYou just earned 10 points!")


#   - Write one version of this program that runs the if
#     block and another that runs the else block

if alien_color == 'green':
    print("\nYou just earned 5 points!")
else:
    print("\nYou just earned 10 points!")



