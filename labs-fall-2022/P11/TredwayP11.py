# TredwayP11
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: This program will make a GUI and ask for the file path
#   of the file that has a database of points, then it will get the 
#   coordinates of your home location, then it will tell you 
#   which of those locations you are closest to.
#
# example file path that I used on a mac:
# /Users/jaeren/Desktop/local-git-repos/python-projects/labs-fall-2022/P10/five_locations.txt

#**** IMPORT MODULES: ****
from math import radians, sqrt, sin, cos, asin
from operator import index, indexOf
from tkinter import *
import sqlite3

#**** GLOBAL VARIABLES: **** (are capitalized)
Program_name = "GeoFinder App"

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
        between two locations on a sphere (in km).
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

    def display_closest_point(self, location_list, distance_to_points_list):
        '''
        Finds the shortest distance in a list of distnaces, and displays 
        that indice's location from the location_list.
        '''
        shortest_distance = min(distance_to_points_list)
        index_of_closest_point = distance_to_points_list.index(shortest_distance)

        Label(main_window, text="").grid(row=15,column=0, sticky=W)

        Label(main_window, text="The closest point to you is:").grid(row=16,column=0, sticky=W)

        Label(main_window, text=f"{location_list[index_of_closest_point].get_description()}                ").grid(row=17,column=0, sticky=W)

        Label(main_window, text="Which is located at: ").grid(row=18,column=0, sticky=W)

        Label(main_window, text=f"({location_list[index_of_closest_point].get_lat()}, {location_list[index_of_closest_point].get_long()})").grid(row=19,column=0, sticky=W)

        Label(main_window, text="").grid(row=20,column=0, sticky=W)

        Label(main_window, text="You may resubmit new coordinates.").grid(row=21,column=0, sticky=W)

        Label(main_window, text="Thank you for using GeoFinder App!", font=('Arial', 20)).grid(row=22,column=0, sticky=W)

        Label(main_window, text="").grid(row=23,column=0, sticky=W)
#**** END Class GeoPoint ****


#**** FUNCTION DEFINITIONS: ****

def build_GUI():
    '''
    This function builds the main windoe=w of the GUI
    with text Labels and text Entry boxes.
    '''

    #create an instance of the Tk object and customize it:
    main_window = Tk()
    main_window.title("GeoFinder App")
    main_window.minsize(700,600)

    #display text labels:   
    '''
    use grid() or pack() to add the item to the GUI window
    use sticky=W to left justify (W means 'west')
    '''
    Label(main_window, text="Welcome to the GeoFinder App!", font=('Arial',25)).grid(row=0,column=0, sticky=W)
    Label(main_window, text="Enter the FULL PATH to your points list .txt file").grid(row=2,column=0, sticky=W)
    Label(main_window, text="Enter your current latitude:").grid(row=3,column=0, sticky=W)
    Label(main_window, text="Enter your current longitude: ").grid(row=4,column=0, sticky=W)

    #set default file location:
    default_file_loc = StringVar(main_window, value='five_locations.txt')

    #set default home coordinates:
    default_lat = StringVar(main_window, value='0.0')
    default_long = StringVar(main_window, value='0.0')

    #display text input boxes:
    file_location = Entry(main_window,width=75,borderwidth=5,textvariable=default_file_loc)
    file_location.grid(row=2,column=1, sticky=W)
    home_lat = Entry(main_window,width=10,borderwidth=5,textvariable=default_lat)
    home_lat.grid(row=3,column=1, sticky=W)
    home_long = Entry(main_window,width=10,borderwidth=5,textvariable=default_long)
    home_long.grid(row=4,column=1, sticky=W)
#**** END GUI BUILDER ****

def on_click():
    '''
    EVENT LISTENER 
    When the button is clicked, this function gets the user input, 
    gets the 5 other points from a file, makes the GeoPoint objects, finds the closest point to home, and reports it to the GUI.
    '''
    Label(main_window, text=f"Your current latitude is: {home_lat.get()}").grid(row=6,column=0, sticky=W)
    Label(main_window, text=f"Your current longitude is: {home_long.get()}").grid(row=7,column=0, sticky=W)

    #instatiate a home point and five other points:
    home = GeoPoint()
    location_1 = GeoPoint()
    location_2 = GeoPoint()
    location_3 = GeoPoint()
    location_4 = GeoPoint()
    location_5 = GeoPoint()

    #get user input for the value of the home point:
    try:
        if home_lat.get() == '':
            my_lat == 0.0
        else:
            my_lat = home_lat.get()
        home.set_lat(float(my_lat))
    except TypeError:
        print("Wrong type of input!")
    except SystemError:
        print("There was a system error!")
    except Exception as e:
        print("Something went wrong:", e)

    try:
        if home_long.get() == '':
            my_long = 0.0
        else:
            my_long = home_long.get()
        home.set_long(float(my_long))
    except TypeError:
        print("Wrong type of input!")
    except SystemError:
        print("There was a system error!")
    except Exception as e:
        print("Something went wrong:", e)

    #read in the five other points from a file:
    try:
        # f = open('five_locations.txt', 'r')
        # /Users/jaeren/Desktop/local-git-repos/python-projects/labs-fall-2022/P9/five_locations.txt
        temp_file_location = file_location.get()
        f = open(temp_file_location, 'r')
    except FileNotFoundError:
        Label(main_window, text="").grid(row=8,column=0, sticky=W)
        Label(main_window, text="ERROR: enter the correct full path to the file where you are storing the five points.").grid(row=9,column=0, sticky=W)
        print('\nERROR:You need to enter the')
        print('correct full path for the file where you')
        print('are storing the five locations.')
    except Exception as e:
        print("Something went wrong: ", e)
    location_list = []
    with f as filestream:
        for line in filestream:
            current_line = line.split(',')
            new_point = GeoPoint()
            new_point.set_lat(float(current_line[0]))
            new_point.set_long(float(current_line[1]))
            new_point.set_description(current_line[2][:-1])
            location_list.append(new_point)

    #report the five remote points that were read in from the file:
    Label(main_window, text="").grid(row=8,column=0, sticky=W)

    Label(main_window, text="The five remote locations that were read from the file are:                                         ").grid(row=9,column=0, sticky=W)

    Label(main_window, text=f"{location_list[0].get_description()}: ({location_list[0].get_lat()}, {location_list[0].get_long()})").grid(row=10,column=0, sticky=W)

    Label(main_window, text=f"{location_list[1].get_description()}: ({location_list[1].get_lat()}, {location_list[1].get_long()})").grid(row=11,column=0, sticky=W)

    Label(main_window, text=f"{location_list[2].get_description()}: ({location_list[2].get_lat()}, {location_list[2].get_long()})").grid(row=12,column=0, sticky=W)

    Label(main_window, text=f"{location_list[3].get_description()}: ({location_list[3].get_lat()}, {location_list[3].get_long()})").grid(row=13,column=0, sticky=W)

    Label(main_window, text=f"{location_list[4].get_description()}: ({location_list[4].get_lat()}, {location_list[4].get_long()})").grid(row=14,column=0, sticky=W)

    #calculate the distances from home to the five other points and store in a list:
    distances_to_five_points = []
    for x in range(5):
        distances_to_five_points.append(home.calc_distance(location_list[x].get_lat(),location_list[x].get_long()))

    #tell the user which point they are closest to:
    home.display_closest_point(location_list,distances_to_five_points)
#**** END EVENT LISTENER FUNCTION which runs every time the button is clicked****

def build_database():
    '''
    This function builds a database of locations with 
    each place's latitude, longitude, and description.
    '''
    #make connection to database:
    database_connection = sqlite3.connect("geopoint_database.db")

    #make a cursor to execute SQL querries:
    cursor_1 = database_connection.cursor()

    #creat a table in the database:
    cursor_1.execute('''
    CREATE TABLE geo_points(
        LatField FLOAT,
        LongField FLOAT,
        DescriptionField TEXT
    )
    ''')

    database_connection.commit()
    database_connection.close()
#**** END DATABASE BUILDER ****


#**** MAIN PROGRAM: ****

#build a database of locations:
build_database()

#build a GUI:
build_GUI()

#button for submitting the user input:
Button(main_window,text="submit",width=10, command = on_click).grid(row=5,column=1, sticky=W)

#button for quitting app:
Button(main_window,text="quit",width=10, command = quit).grid(row=23,column=1, sticky=E)

#run the event listener loop:
main_window.mainloop()

#**** END MAIN ****
