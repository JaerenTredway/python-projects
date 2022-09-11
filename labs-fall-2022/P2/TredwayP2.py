# TredwayP2
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: takes user input of a U.S. state, and returns
#     the state capital, number of congressional districts,
#     and the order that state joined the union.


# build data structure with names of states, state capitals,
# number of districts per state, and order number the
# state joined the union:
states_list = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')
capitals_list = ('Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'Saint Paul', 'Jackson', 'Jefferson city', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne')
districts_list = (7, 1, 9, 4, 53, 7, 5, 1, 27, 14, 2, 2, 18, 9, 4, 4, 6, 6, 2, 8, 9, 14, 8, 4, 8, 1, 3, 4, 2, 12, 3, 27, 13, 1, 16, 5, 5, 18, 2, 7, 1, 9, 36, 4, 1, 11, 10, 3, 8, 1)             
order_joined_list = ('22nd', '49th', '48th', '25th', '31st', '38th', '5th', '1st', '27th', '4th', '50th', '43rd', '21st', '19th', '29th', '34th', '15th', '18th', '23rd', '7th', '6th', '26th', '32nd', '20th', '24th', '41st', '37th', '36th', '9th', '3rd', '47th', '11th', '12th', '39th', '17th', '46th', '33rd', '2nd', '13th', '8th', '40th', '16th', '28th', '45th', '14th', '10th', '42nd', '35th', '30th', '44th')
database = (states_list, capitals_list, districts_list, order_joined_list)

# introduction for the user:
print("\nUnited States Database of State Information\n")
print("This program will tell you information about any")
print("State you choose.\n")

# get user input:
state = ""
while state not in database[0]:
    state = input("Enter the name of a U.S. State: ")
    if state not in database[0]:
        print("\nYou entered: {}, which is not a valid state name.\n".format(state))      

# find index of that state's name:
state_index = states_list.index(state)

# output the state's information:
print("The capital of {} is {},".format(state, database[1][state_index]))
print("its number of Congressional Districts is {},".format(database[2][state_index]))
print("and it was the {} state to join the union.".format(database[3][state_index]))
