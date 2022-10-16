# TredwayP_not
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: Class examples
# Notes: 
# Reference/ research: 
#   

#**** IMPORT MODULES: ****
from math import radians, sqrt, sin, cos, asin

#**** GLOBAL VARIABLES: **** (are capitalized)
Program_name = "Class Examples"

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
    
    # use the superclass's method:
    #def get_stuff(self):
        #return super().get_description()


# FUNCTION DEFINITIONS *************


# MAIN PROGRAM *****************************

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

