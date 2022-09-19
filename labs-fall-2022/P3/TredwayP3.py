# TredwayP3
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: Provides a user with the capability to find fruit in a string.

# Create a database that has the names of seven fruits:
fruit_list = ['banana', 'apple', 'orange', 'peach', 'pear', 'plum', 'mango']

# UI introduction and collect input data:
print("\n\n*************************************************")
print("\nWelcome to FruitFinder. This program will get a")
print("sentence from you, and find the fruit in it.")
input_data = input("\nPlease enter a sentence with some fruit in it: ")
    
# Process data to find the fruit:
input_data_cleaned = input_data.lower().replace(".", "").replace("!","").replace("?","")
data_as_list = input_data_cleaned.split()
target_data = list(set(data_as_list)&set(fruit_list))

# Check for bad data to exit program:
if len(target_data) == 0:
    print("\nYour input has none of the right fruit in it. Program terminated.")
    quit()
    
# Tell the user how many fruits are in their data and show a list of the fruit:
num_fruits = len(target_data)
print("\nYour input data contains {} fruits.".format(num_fruits))
print("\nHere is a list of your fruits:")
print(target_data)

# Find and replace one instance of a fruit in the sentence with “Brussel Sprouts”:
sprout_variant = input_data.replace(target_data[0], "Brussel Sprouts")

# Display the new sentence to the user:
print("\nAnd here is a sprout variant of your input data:")
print(sprout_variant)

