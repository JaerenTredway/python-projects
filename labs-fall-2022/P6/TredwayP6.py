# TredwayP6
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: Get the decimal-degree coordinates of two 
#   locations from the user, and display the distance
#   between them in km.
# Notes: I used 6371km as the Earth's radius as per the 
#   instructions, but according to NASA the radius is 
#   closer to 6378km.
# Reference/ research: 
#   https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
#   https://imagine.gsfc.nasa.gov/features/cosmic/earth_info.html#:~:text=Both%20of%20these%20values%20are,been%20measured%20by%20orbiting%20spacecraft 

# IMPORT MODULES: *****************
from math import radians, sqrt, sin, cos, asin

# GLOBAL VARIABLES **************** (are capitalized)
Program_name = "GEO Distance Finder"
Location_1 = 0,0
Location_2 = 0,0
Distance = 0

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
