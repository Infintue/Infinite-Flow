from tkinter import *
import tkinter.font
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile, asksaveasfilename
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askokcancel
from tkinter import messagebox
import os
import webbrowser

root = Tk()
root.title("Infinite Flow")
root.state('zoomed')




def saveText(event=None):
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File",".txt"), ("Python",(".py"))])


    fileText = str(textField.get(1.0,END))
    file.write(fileText)
    file.close()

def openText(event=None):
    openedName = askopenfilename(title="Open a file", filetypes = (("Text File","*.txt"), ("C++","*.c++"), ("Java","*.java"), ("JavaScript","*.js"), ("Python","*.py"), ("all files","*.*")))
    file = open(openedName, "r")
    openContent = file.read()
    textField.insert(1.0, openContent)

def dth():
    textField.config(bg="white", fg="black")
def dbth():
    textField.config(bg="dodgerblue4", fg="white")
def mbth():
    textField.config(bg="midnightblue", fg="white")
def owth():
    textField.config(bg="goldenrod", fg="black")
def lchth():
    textField.config(bg="lemonchiffon", fg="black")
def df():
     textField.config(font='16')
def rf():
    textField.config(font=("Roman", '16'))
def tf():
    textField.config(font="Terminal")
def chronst():
    textField.config(font="Times")


main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=False)
theme_menu = Menu(main_menu, tearoff=False)
font_menu = Menu(main_menu, tearoff=False)
vm_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Themes", menu=theme_menu)
main_menu.add_cascade(label="Fonts", menu=font_menu)
main_menu.add_cascade(label="Version Control", menu=vm_menu)
file_menu.add_command(label="Save", command= saveText)
file_menu.add_command(label="Open", command= openText)

theme_menu.add_command(label="Default", command=dth)
theme_menu.add_separator()
theme_menu.add_command(label="Dodger Blue", command=dbth)
theme_menu.add_command(label="Midnight Blue", command=mbth)
theme_menu.add_separator()
theme_menu.add_command(label="Oak Wood", command=owth)
theme_menu.add_command(label="Lemon Chiffon", command=lchth)

font_menu.add_command(label="Default", command=df)
font_menu.add_command(label="Terminal", command=tf)
font_menu.add_command(label="Roman", command=rf)
font_menu.add_command(label="Times", command=chronst)

vm_menu.add_command(label="Visit the Infinite webiste", command=lambda: webbrowser.open("https://sites.google.com/view/infinitue"))
vm_menu.add_separator()
vm_menu.add_command(label="Version Checker", command=lambda: webbrowser.open("https://sites.google.com/view/infinitue/products/software/saturn/downloadwithout-numberline/version-status-1-1"))


textField = Text(root, wrap="word", font='16', undo=True)
textField.bind('<Control-s>', saveText)
textField.bind('<Control-o>', openText)
textField.pack(expand="yes", fill="both")


root.mainloop()

