# TredwayP12
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: This program will expand on previous labs. It will add a GUI class so
#   I can make a GUI object and get that out of the MAIN. I'll also make a 
#   Database class rather than just a database builder function. Then I will
#   populate the database with restaurants and use the GUI to find the nearest
#   restaurant of a certain type to the user. 
# database location URL for my system:
#   /Users/jaeren/Desktop/local-git-repos/python-projects/labs-fall-2022/P12/my_database.db

#**** IMPORT MODULES: ****
from math import radians, sqrt, sin, cos, asin
from tkinter import *
import sqlite3
from tkinter import font

#**** GLOBAL VARIABLES: **** 
# the full path url to the .db file, which will be input into the GUI:
database_location = ""
# the list of Restaurant objects that have the restaurant locations:
restaurant_list = []

#**** CLASS DEFINITIONS: ****
class Restaurant:
    #constructor to initialize class attributes:
    def __init__(self):
        self.lat = 0.00
        self.long = 0.00
        self.name = ""
        self.type = ""


    #class methods:    
    def set_lat(self,lat):
        self.lat = lat
    def set_long(self,long):
        self.long = long
    def set_name(self, name):
        self.name = name
    def set_type(self, type):
        self.type = type
    def get_lat(self):
        return (self.lat)
    def get_long(self):
        return(self.long)
    def get_point(self):
        return self.lat, self.long
    def get_name(self):
        return self.name
    def get_type(self):
        return self.type    

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

    def display_closest_restaurant(self, restaurant_list, distance_to_food_list):
        '''
        Finds the shortest distance in a list of distnaces, and displays 
        that indice's data from the restaurant_list onto the GUI.
        '''
        shortest_distance = min(distance_to_food_list)
        index_of_closest_food = distance_to_food_list.index(shortest_distance)

        Label(main_window, text="").grid(row=10,column=0, sticky=W)

        Label(main_window, text=f"The closest {restaurant_list[index_of_closest_food].get_type()} restaurant to you is:").grid(row=11,column=1, sticky=W)

        Label(main_window, text=f"{restaurant_list[index_of_closest_food].get_name()}                          ").grid(row=12,column=1, sticky=W)

        Label(main_window, text="Which is located at: ").grid(row=13,column=1, sticky=W)

        Label(main_window, text=f"({restaurant_list[index_of_closest_food].get_lat()}, {restaurant_list[index_of_closest_food].get_long()})    ").grid(row=14,column=1, sticky=W)

        Label(main_window, text="").grid(row=15,column=0, sticky=W)

        Label(main_window, text="You may resubmit new coordinates and type of food.").grid(row=16,column=1, sticky=W)

        Label(main_window, text="Thank you for using the ChowTime App!", font=('Phosphate', 20)).grid(row=17,column=1, sticky=W)

        Label(main_window, text="").grid(row=17,column=0, sticky=W)
#**** END Class Restaurant ****


#**** FUNCTION DEFINITIONS: ****

def build_database():
    '''
    This function builds a database of locations with 
    each place's latitude, longitude, and description.
    '''
    #make connection to database file:
    print("\nDATABASE LOCATION: ", database_location)
    database_connection = sqlite3.connect(database_location)

    #make a cursor to execute SQL querries:
    my_cursor = database_connection.cursor()

    #delete the old table:
    my_cursor.execute('''
    DROP TABLE IF EXISTS my_table
    ''')

    #creat a new table in the database:
    my_cursor.execute('''
    CREATE TABLE my_table(
        LatColumn FLOAT,
        LongColumn FLOAT,
        NameColumn TEXT,
        TypeColumn TEXT
    )
    ''')

    database_connection.commit()

    #insert data into the table:
    my_cursor.execute('''
    INSERT INTO my_table(
        LatColumn,
        LongColumn,
        NameColumn,
        TypeColumn
    )
    VALUES 
        (100.200, 123.456, "Chang's", 'Chinese'),
        (120.330, 142.345, 'East Ocean', 'Chinese'),
        (153.230, 322.345, 'Hunan', 'Chinese'),
        (133.230, 143.345, 'Qwon Wong', 'Chinese'),
        (153.420, 122.345, 'Spicy Wonton', 'Chinese'),
        (100.200, 123.456, "McDonald's", 'American'),
        (120.330, 142.345, 'Burger King', 'American'),
        (153.230, 322.345, "Wendy's", 'American'),
        (133.230, 143.345, 'Sonic', 'American'),
        (153.420, 122.345, "Carl's Jr.", 'American'),
        (100.200, 123.456, "Garcia's", 'Mexican'),
        (120.330, 142.345, 'Taco House', 'Mexican'),
        (153.230, 322.345, "Sadie's", 'Mexican'),
        (133.230, 143.345, 'Frontier', 'Mexican'),
        (153.420, 122.345, 'Green Chili Monster', 'Mexican')
    ''')

    database_connection.commit()
    
    #see if there is anything in the database:
    with database_connection:
        my_cursor.execute("SELECT * FROM my_table")
        print("Database contents: ")
        print(my_cursor.fetchall())
    database_connection.close()
#**** END build_database() ****

def on_click():
    '''
    EVENT LISTENER 
    When a button is clicked, this function gets the user input,
    builds the database, gets the data from the database, makes the Restaurant objects, 
    finds the closest restaurant to home, and reports it to the GUI.
    '''
    
    #make a string from the database location Entry:
    global database_location
    database_location = database_location_entry.get()
    build_database()

    #instantiate a home point and fifteen other points:
    home = Restaurant()
    location_1 = Restaurant()
    location_2 = Restaurant()
    location_3 = Restaurant()
    location_4 = Restaurant()
    location_5 = Restaurant()

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

#populate Restaurant objects from the database data:
    #make connection to the database file:
    database_connection = sqlite3.connect(database_location)

    #make a cursor to execute SQL querries:
    my_cursor = database_connection.cursor()
    
    #fetch the contents of the database into a local list:
    with database_connection:
        my_cursor.execute("SELECT * FROM my_table")
        raw_list = list(my_cursor.fetchall())

    database_connection.close()

    #make a second list with Restaurant objects from the local data dump:
    restaurant_list = []
    for line in raw_list:
        new_restaurant = Restaurant()
        new_restaurant.set_lat(float(line[0]))
        new_restaurant.set_long(float(line[1]))
        new_restaurant.set_name(line[2])
        new_restaurant.set_type(line[3])
        restaurant_list.append(new_restaurant)

    #example Label for reporting the restaurants that were read in from the database:
    #Label(main_window, text=f"{location_list[4].get_description()}: ({location_list[4].get_lat()}, {location_list[4].get_long()})").grid(row=14,column=0, sticky=W)

    #calculate the distances from 'home' to the restaurants and store them in a list:
    distances_to_restaurants = []
    for x in range(5):
        distances_to_restaurants.append(home.calc_distance(restaurant_list[x].get_lat(),restaurant_list[x].get_long()))

    #tell the user which restaurant they are closest to:
    home.display_closest_restaurant(restaurant_list,distances_to_restaurants)
#**** END EVENT LISTENER on_click() which runs every time the submit button is clicked****


#**** MAIN PROGRAM: ****

#**** build a GUI: ****
#create an instance of the Tk object and customize it:
main_window = Tk()
main_window.title("ChowTime App")
main_window.minsize(700,600)
# main_window.configure(background='green')

#show all available tkinter fonts in the terminal:
#print(font.families())

#display text labels:   
'''
use grid() or pack() to add the item to the GUI window
use sticky=W to left justify (W means 'west')
'''
Label(main_window, text="Welcome to the ChowTime App!", font=('Party LET',60, "bold italic")).grid(row=0,column=1, sticky=W)
Label(main_window, text="Tell us your location and what kind of food you want!", font=('Phosphate', 20)).grid(row=2,column=1, sticky=W)
Label(main_window, text="").grid(row=3,column=0)
Label(main_window, text="Enter the FULL PATH to your database .db file: ").grid(row=4,column=0, sticky=W)
Label(main_window, text="Enter your current latitude: ").grid(row=5,column=0, sticky=W)
Label(main_window, text="Enter your current longitude: ").grid(row=6,column=0, sticky=W)
Label(main_window, text="What kind of food do you want: ").grid(row=7,column=0, sticky=W)

#set default database file location:
default_file_loc = StringVar(main_window, value='/Users/jaeren/Desktop/local-git-repos/python-projects/labs-fall-2022/P12/my_database.db')

#set default home coordinates:
default_lat = StringVar(main_window, value='0.0')
default_long = StringVar(main_window, value='0.0')

#display the text input boxes:
database_location_entry = Entry(main_window,width=75,borderwidth=5,textvariable=default_file_loc)
database_location_entry.grid(row=4,column=1, sticky=W)
home_lat = Entry(main_window,width=10,borderwidth=5,textvariable=default_lat)
home_lat.grid(row=5,column=1, sticky=W)
home_long = Entry(main_window,width=10,borderwidth=5,textvariable=default_long)
home_long.grid(row=6,column=1, sticky=W)

#buttons for submitting the type of food wanted:
Button(main_window,text="Chinese",width=10, command = on_click).grid(row=7,column=1, sticky=W)
Button(main_window,text="American",width=10, command = on_click).grid(row=8,column=1, sticky=W)
Button(main_window,text="Mexican",width=10, command = on_click).grid(row=9,column=1, sticky=W)

#button for quitting app:
Button(main_window,text="quit",width=10, command = quit).grid(row=23,column=3, sticky=E)

#**** END GUI BUILDER ****

#run the event listener loop that listens for button clicks:
main_window.mainloop()

#**** END MAIN ****
