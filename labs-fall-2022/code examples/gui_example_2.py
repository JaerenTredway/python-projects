# example GUI from:
# https://www.youtube.com/watch?v=_PHJvjQJa3w&t=338s

#import a Python GUI library:
from tkinter import *

#create an instance of the Tk object and customize it:
main_window = Tk()
main_window.title("GeoFinder App")
main_window.minsize(500,500)

#display text labels:   (use grid() or pack() to add the item to the GUI window)
Label(main_window, text="Welcome to the GeoFinder App!").grid(row=0,column=0)
Label(main_window, text="Enter your current latitude:").grid(row=1,column=0)
Label(main_window, text="Enter your current longitude: ").grid(row=2,column=0)

#display text input boxes:
home_lat = Entry(main_window,width=10,borderwidth=5)
home_lat.grid(row=1,column=1)
home_long = Entry(main_window,width=10,borderwidth=5)
home_long.grid(row=2,column=1)

#callback function:
def on_click():
    print(f"Your home latitude is {home_lat.get()}, ")
    print(f"and your home longitude is {home_long.get()}")
    Label(main_window, text=f"Your home latitude is: {home_lat.get()}").grid(row=4,column=0)
    Label(main_window, text=f"Your home longitude is: {home_long.get()}").grid(row=5,column=0)

#button for submitting the user input:
Button(main_window,text="submit",width=10, command = on_click).grid(row=3,column=1)


#run the event listener loop:
main_window.mainloop()


# #make a GUI class:
# class Root(Tk):
#     #constructor:
#     def __init__(self):
#         super(Root,self).__init__()
#         self.title("GeoFinder App Object")
#         self.minsize(700,700)
 
# #create a Root object and run it: 
# root = Root()
# root.mainloop()

