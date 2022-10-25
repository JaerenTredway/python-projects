from tkinter import *
from tkinter.scrolledtext import ScrolledText

# my file name is: /Users/jaeren/Desktop/local-git-repos/python-projects/labs-fall-2022/P10/five_points.txt"

def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())

def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))

top = Tk()
top.title("GeoPoint Distance Finder with GUI")

contents = ScrolledText()                                                                           
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)

mainloop()     