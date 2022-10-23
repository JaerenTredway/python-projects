# TredwayP9
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: This program will get the coordinates of your home location,
#   then read in five other locations from a file, then tell you which
#   of those locations you are closest to.

#**** IMPORT MODULES: ****
from math import radians, sqrt, sin, cos, asin

#**** GLOBAL VARIABLES: **** (are capitalized)
Program_name = "GeoPoint Distance Finder WITH Error Handling"

#**** CLASS DEFINITIONS: ****
class GeoPoint:
    #constructor to initialize class attributes:
    def __init__(self):
        self.lat = 0.00
        self.long = 0.00
        self.description = ""

    #class methods:    
    def set_lat(self,lat):
        self.lat = lat
    def set_long(self,long):
        self.long = long
    def set_description(self, description):
        self.description = description
    def get_lat(self):
        return (self.lat)
    def get_long(self):
        return(self.long)
    def get_point(self):
        return self.lat, self.long
    def get_description(self):
        return self.description
    def calc_distance(self,other_lat,other_long):
        '''
        Uses the Haversine Formula to find the distance 
        between two locations in km.
        '''
        # assign decimal degrees from args:
        lat1 = self.lat
        long1 = self.long
        lat2 = other_lat
        long2 = other_long
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
    def input_location(self,ordinal):
        '''
        Asks the user for a location's latitiude and longitude,
        and sets the object's lat and long. 'ordinal' is the 
        location's order in the sequnce (first, second).
        '''
        print(f"\n(Enter your {ordinal} data set in decimal degrees:)")
        self.set_lat(float(input(f"Enter {ordinal} location's latitude: ")))
        self.set_long(float(input(f"Enter {ordinal} location's longitude: ")))
        return self.lat,self.long
    def display_closest_point(self, first_location_name, second_location_name, distance_to_first, distance_to_second):
        if distance_to_first < distance_to_second:
            print(f"You are closest to {first_location_name}")
            print(f"which is {distance_to_first} km away")
        else:
            print(f"You are closest to {second_location_name}")
            print(f"which is {distance_to_second} km away")


#**** FUNCTION DEFINITIONS FOR USER INTERFACE: ****
def display_header():
    '''
    Displays program introduction for the user.
    '''
    print("\n*****************************")
    print(Program_name.upper())
    print("This program will get the coordinates of your home location,")
    print("and two other remote locations,")
    print("and tell you which one you are closest to.")

def continue_loop():
    '''
    Asks user if they want to continue.
    '''
    user_input = input("\nDo you want to continue? ")
    # this cleans the input so that any version of 'yes' works:
    if len(user_input) > 0:
        return user_input.strip()[0].lower() == 'y'
    else: return False

def display_distance(first_location, second_location, distance):
    '''
    Displays two locations and the distance between them.
    '''
    print(f"\nThe distance between {first_location} and {second_location} is {distance} km.")  

def display_footer(program):
    '''
    Displays a farewell at the end of the program.
    '''
    print(f"\nThanks for using {program}!")


#**** MAIN PROGRAM: ****
display_header()

# Create an infinite while-loop, which the user can
#   continue or break out of:
while True:
    #instatiate a home point and five other points:
    home = GeoPoint()
    location_1 = GeoPoint()
    location_2 = GeoPoint()
    location_3 = GeoPoint()
    location_4 = GeoPoint()
    location_5 = GeoPoint()

    #get user input for the value of the home point:
    try:
        home.input_location("home")
    except TypeError:
        print("Wrong type of input!")
        continue
    except SystemError:
        print("There was a system error!")
        continue
    except Exception as e:
        print("Something went wrong:", e)
        continue

    #read in the five other points from a file:
    try:
        open('/Users/jaeren/Desktop/local-git-repos/python-projects/labs-fall-2022/P9/five_locations.txt')
    except FileNotFoundError:
        print('You need to change the code at line 130 to have the')
        print('correct full path and file name for the file where you')
        print('are storing the five locations.')
        continue
    except Exception as e:
        print("Something went wrong: ", e)
        continue

    #report the remote points that were entered:
    print(f"\nYou entered:")
    print(f"{location_1.get_description()}: ({location_1.get_lat()}, {location_1.get_long()}) and")
    print(f"{location_2.get_description()}: ({location_2.get_lat()}, {location_2.get_long()})\n")

    #calculate the distrances from home to the two other points:
    distance_to_one = home.calc_distance(location_1.get_lat(),location_1.get_long())
    distance_to_two = home.calc_distance(location_2.get_lat(),location_2.get_long())

    #tell the user which point they are closest to:
    home.display_closest_point(location_1.get_description(),location_2.get_description(),distance_to_one,distance_to_two)
    
    #continue or stop:
    if not continue_loop(): break

display_footer(Program_name)
