#!python3
import math
answer1 = "1"
answer2 = "2"
answer3 = "neither"
x = float(input("Enter the first side value: "))
y = float(input("Enter the second side value: "))
z = input("Which one of the numbers the hypotenuse, 1, 2, or neither?: ")
if answer1 in z:
    missingside = math.sqrt((x ** 2)(y ** 2))



"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
