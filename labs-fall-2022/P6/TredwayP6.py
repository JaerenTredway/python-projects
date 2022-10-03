# TredwayP6
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: Demonstrate using functions.

#Global Variables*****************
program_name = "My Program"


#Function Definitions*************

def display_header():
    '''Displays program introduction for the user.'''
    print("\n*****************************")
    print("DISTANCE BETWEEN 2 LOCATIONS")
    print("This program will get 2 locations from the user,")
    print("and then display the distance between them.")

def continue_loop():
    '''Asks user if they want to continue.'''
    user_input = input("Do you want to continue? ")
    # this cleans the input so that any version of 'yes' works:
    do_continue = user_input.strip()[0].lower() == 'y'
    # and returns a boolean value:
    return do_continue

def display_footer(program):
    '''Displays a farewell at the end of the program.'''
    print(f"Thanks for using {program}!")

#Main*****************************
 
display_header()

# Create an infinite while-loop, which the user can
#   continue or break out of:
while True:
    #do stuff
    if not continue_loop(): break

display_footer(program_name)
