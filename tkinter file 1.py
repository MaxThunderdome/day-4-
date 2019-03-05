from tkinter import *
Window = Tk()
Window.title("Assignment 3")
Window.minsize = "1000 x 1000"
Window.geometry("240x500+700+300")

#functions to handle button clicks
def button1_clicked():
    print("qwerty club rules")
def button2_clicked():
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
    location = input("Select file location")
    print("Open clicked")
#redundant for this code
def New_clicked():
    print("New clicked")

def Save_clicked():
    print("Save clicked")

def SaveAs_clicked():
    print("Save As clicked")

def Cut_clicked():
    print("Cut clicked")

def Copy_clicked():
    print("Copy clicked")

def Paste_clicked():
    print("Paste clicked")

def Delete_clicked():
    print("Delete clicked")

def Quit_clicked():
    raise SystemExit

main_menu = Menu(Window)

FileMenu = Menu(main_menu)
FileMenu.add_command(label="New",command = New_clicked)
FileMenu.add_separator()
FileMenu.add_command(label="Open",command = Open_clicked)
FileMenu.add_command(label="Save",command = Save_clicked)
FileMenu.add_command(label="Save As",command = SaveAs_clicked)
FileMenu.add_separator()
FileMenu.add_command(label="Quit Demo",command = Quit_clicked)

EditMenu = Menu(main_menu)
EditMenu.add_command(label="Cut",command = Cut_clicked)
EditMenu.add_command(label="Copy",command = Copy_clicked)
EditMenu.add_command(label="Paste",command = Paste_clicked)
EditMenu.add_command(label="Delete",command = Delete_clicked)


main_menu.add_cascade(label = "File", menu = FileMenu)
main_menu.add_cascade(label = "Edit", menu = EditMenu)

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

Window.mainloop()