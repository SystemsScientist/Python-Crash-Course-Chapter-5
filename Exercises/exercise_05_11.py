# exercise_05_11.py, Chapter 5, Python Crash Course
#
# Ordinal Numbers: Ordinal numbers indicate their position
# in a list, such as 1st or 2nd. Most ordinal numbers end
# in "th", except 1, 2, and 3.

#   - Store the numbers 1 through 9 in a list.

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#   - Loop through the list.

print("Here's the list of numbers: ")
for ordinal_number in ordinal_numbers[:]:
    print(ordinal_number)

#   - Use an if-elif-else chain inside the loop to print
#     the proper ordinal ending for each number. Your
#     output should read "1st 2nd 3rd 4th 5th 6th 7th 
#     8th 9th", and each result should be on a separate
#     line.

print("\nHere's the list of numbers as ordinal numbers: ")
for ordinal_number in ordinal_numbers[:]:
    if ordinal_number == 1:
        print(str(ordinal_number) + "st")
    elif ordinal_number == 2:
        print(str(ordinal_number) + "nd")
    elif ordinal_number == 3:
        print(str(ordinal_number) + "rd")
    else:
        print(str(ordinal_number) + "th")



