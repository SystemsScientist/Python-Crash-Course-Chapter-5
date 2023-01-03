# cars.py, Chapter 5, Python Crash Course
# program a for loop and if block to find
# and print 'bmw' in uppercase

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



