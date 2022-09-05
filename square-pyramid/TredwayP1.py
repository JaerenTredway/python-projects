# TredwayP1
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: provides user capability to calculate 
# volume of a pyramid

from math import sqrt

# introduction for user:
print("\nWelcome to SquarePyramid")
print("This program gets a pyramid's height and base length from you,")
print("and returns to you the pyramid's surface area and volume.")

# get user input:
base = float(input("Enter the base length in feet: "))
height = float(input("Enter the height in feet: "))

# make calculations:
volume = (pow(base,2) * height) / 3
slant = sqrt(pow(height,2) + pow((base/2),2))
area_one_side = slant * (base/2)
area_total = (area_one_side * 4) + pow(base,2)

# output results:
print("\nYour Pyramid volume is {:.2f} cubic feet,".format(volume))
print("and the surface area is {:.2f} square feet.".format(area_total))