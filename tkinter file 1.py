from tkinter import *
Window = Tk()
Window.title("Assignment 3")
Window.minsize = "1000 x 1000"
Window.geometry("260x500+400+300")

location = None

#functions to handle button clicks
def button1_clicked():
    print("qwerty club rules")
def button2_clicked():
    location = input("Select file location")
    TextfromFile = open(location, "r")
    contents = TextfromFile.readlines()
    print(contents)
    print("button 2 clicked")
def button3_clicked():
    print("button 3 clicked")
    button3.config(text="Guess again")
def button4_clicked():
    Window.configure(background='blue')
    print("button 4 clicked")

def Open_clicked():
    command = button2_clicked()
    print("Open clicked")
def Quit_clicked():
    raise SystemExit

main_menu = Menu(Window)

FileMenu = Menu(main_menu)
FileMenu.add_separator()
FileMenu.add_command(label="Open",command = button2_clicked)
FileMenu.add_command(label="Quit Demo",command = Quit_clicked)

main_menu.add_cascade(label = "File", menu = FileMenu)

#Create Buttons
button1 = Button(Window,text = "button1", command = button1_clicked, height = 4, width=16)
button2 = Button(Window,text = "button2", command = button2_clicked, height = 4, width=16)
button3 = Button(Window,text = "button3", command = button3_clicked, height = 4, width=16)
button4 = Button(Window,text = "button4", command = button4_clicked, height = 4, width=16)
#Locate Buttons on grid
button1.grid(column = 0,row = 2)
button2.grid(column = 1,row = 2)
button3.grid(column = 0,row = 3)
button4.grid(column = 1,row = 3)

Window.config(menu=main_menu)
Window.mainloop()
#TopLevel.grid_propagate(0)
