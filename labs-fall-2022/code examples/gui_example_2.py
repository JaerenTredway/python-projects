# example GUI from:
# https://www.youtube.com/watch?v=_PHJvjQJa3w&t=338s

#import a Python GUI library:
from tkinter import *

#create instance of Tk object and customize it:
main_window = Tk()
main_window.title("GeoFinder App")
main_window.minsize(700,700)

#display labels:   (use grid() or pack() to add the item to the GUI window)
Label(main_window, text="Welcome to the GeoFinder App!").grid(row=0,column=0)
Label(main_window, text="Enter your current latitude:").grid(row=1,column=0)
Label(main_window, text="Enter your current longitude: ").grid(row=2,column=0)

#display text input boxes:
Entry(main_window, width=10,borderwidth=5).grid(row=1,column=1)
Entry(main_window, width=10,borderwidth=5).grid(row=2,column=1)

#buttons:
Button(main_window, text="submit lat", width=10).grid(row=1,column=2)
Button(main_window, text="submit long", width=10).grid(row=2,column=2)

#run the event listener loop:
main_window.mainloop()



# #make a GUI class:
# class Root(Tk):
#     def __init__(self):
#         super(Root,self).__init__()
 
#         self.title("GeoFinder App Object")
#         self.minsize(700,700)
 
# #make a Root object and run it: 
# root = Root()
# root.mainloop()

