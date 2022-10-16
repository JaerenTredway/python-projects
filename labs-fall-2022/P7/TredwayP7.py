# TredwayP7
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: 
# Notes: 
# Reference/ research: 
#   

#**** IMPORT MODULES: ****
from math import radians, sqrt, sin, cos, asin

#**** GLOBAL VARIABLES: **** (are capitalized)
Program_name = "Program Name"

#**** CLASS DEFINITIONS: ****
class Person:
    #constructor to initialize class attributes:
    def __init__(self):
        self.name = "unknown"

    #class methods:    
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print(f"Hello World! My name is {self.name}.")

class Animal:
    #constructor to initialize class attributes:
    def __init__(self):
        self.description = "generic animal"
        self.noise = "generic animal sound"
        self.name = "unknown"

    #class methods:  
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_description(self,description):
        self.description = description
    def get_description(self):
        return self.description
    def make_noise(self):
        print(self.noise)

# inheritance:
class Lion(Animal):
    pass

    #or add additional methods here:
    def sleep(self):
        print("I am sleeping.")
    
    #over-ride super-class:
    def get_description(slef):
        return("I am a lion.")
    
    # use superclass method:
    #def get_stuff(self):
        #return super().get_description()


# FUNCTION DEFINITIONS *************
 
def display_header():
    '''
    Displays program introduction for the user.
    '''
    print("\n*****************************")
    print(Program_name.upper())
    print("This program will get 2 locations from you,")
    print("and then display the distance between them.")

def continue_loop():
    '''
    Asks user if they want to continue.
    '''
    user_input = input("\nDo you want to continue? ")
    # this cleans the input so that any version of 'yes' works:
    do_continue = user_input.strip()[0].lower() == 'y'
    # and returns a boolean value:
    return do_continue

def get_location(ordinal):
    '''
    Asks the user for a location's latitiude and longitude,
    and returns a tuple with them. 'Ordinal' is the 
    location's order in the sequnce (first, second).
    '''
    print(f"\n(Enter your {ordinal} data set in decimal degrees:)")
    location_lat = float(input(f"Enter {ordinal} location's latitude: "))
    location_long = float(input(f"Enter {ordinal} location's longitude: "))
    return location_lat,location_long

def distance_between(first_location,second_location):
    '''
    Uses the Haversine Formula to find the distance 
    between two locations in km.
    '''
    # assign decimal degrees from args:
    lat1 = first_location[0]
    long1 = first_location[1]
    lat2 = second_location[0]
    long2 = second_location[1]
    # convert decimal degrees into radians:
    lat1, long1, lat2, long2 = map(radians, [lat1,long1,lat2,long2])
    # get latitudinal and logitudinal differences:
    d_lat = lat2 - lat1
    d_long = long2 - long1
    # Haversine Formula:
    a = sin(d_lat/2)**2 + cos(lat1) * cos(lat2) * sin(d_long/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # radius of Earth in km
    distance = c * r
    return round(distance,2)

def display_distance(first_location, second_location, distance):
    '''
    Displays two loactions and the distance between them.
    '''
    print(f"The distance between {first_location} and {second_location} is {distance} km.")  

def display_footer(program):
    '''
    Displays a farewell at the end of the program.
    '''
    print(f"\nThanks for using {program}!")


# MAIN PROGRAM *****************************
 
display_header()

person_one = Person()
person_one.set_name("Luke Skywalker")
print(person_one.name)
print(person_one.get_name())
person_one.greet()
person_two = Person()
person_two.greet()
print()

lion_1 = Lion()
lion_1.set_name("Leo")
print(f"My name is {lion_1.get_name()}")
print(lion_1.get_description())
lion_1.make_noise()
lion_1.sleep()

# Create an infinite while-loop, which the user can
#   continue or break out of:
while True:
    Location_1 = get_location("first")
    Location_2 = get_location("second")
    print(f"\nYou entered: {Location_1} and {Location_2}\n")
    Distance = distance_between(Location_1,Location_2)
    display_distance(Location_1, Location_2, Distance)
    if not continue_loop(): break

display_footer(Program_name)
