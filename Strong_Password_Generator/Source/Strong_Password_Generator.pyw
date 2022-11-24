import tkinter
from tkinter import messagebox
from random import choice
from pyperclip import copy

#---------

Window = tkinter.Tk()

#---------

characterslist = ['<', '>', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '~', '#', '{', '(', '[', '-', '|', '_', '@', ')', ']' '°', '=', '+', '}', '£', '$', '%', '*', '/', ';', ',', '?', '!', '§', '.']

#---------

def Clearer():
    PasswordOutput.delete(0, "end")
    MaxNumberEntry.delete(0, "end")

def Generator(maxnumber):
    passwd = ""
    for i in range(maxnumber):
        passwd += str(choice(characterslist))
    return passwd
    
def Copy():
    strtocopy = PasswordOutput.get()
    if strtocopy == "" or strtocopy == None:
        messagebox.showerror("Copy Error","Please generate a password to copy it.")
        return
    copy(strtocopy)
    messagebox.showinfo("Password Copied!","Your password has been copied to your clipboard.")
    return
    

def LetsGenerate():
    maxnumber = MaxNumberEntry.get()
    if maxnumber == "":
        messagebox.showerror("Values Error","Please enter a number of characters.")
        return
    try:
        maxnumber = int(maxnumber)
    except ValueError:
        messagebox.showerror("Values Error","The amount of characters must be a number.")
        return
    if maxnumber <= 6:
        messagebox.showerror("Values Error","The amount of characters must be above 6 characters.")
        return
    if maxnumber > 300:
        messagebox.showerror("Values Error","The amount of characters must be lower than 300 characters.")
        return
    password = Generator(maxnumber)
    password = str(password)
    PasswordOutput.delete(0, "end")
    PasswordOutput.insert(0, password)
    print("Password generated!")

CreditLabel = tkinter.Label(Window, text="Made by BloodAlibi", font=("Helvetica", 6), fg = "grey")
CreditLabel.place(x=0, y=0)

#---------

GenerateButton = tkinter.Button(Window, text="Generate", command=LetsGenerate)
GenerateButton.place(x=165, y=90)
ClearButton = tkinter.Button(Window, text="Clear", command=Clearer)
ClearButton.place(x=120, y=90)
CopyButton = tkinter.Button(Window, text="Copy", command=Copy)
CopyButton.place(x=230, y=90)

#---------

IndicationLabel = tkinter.Label(Window, text="Indicate the number of characters you want in your password.", font=("Helvetica", 10))
IndicationLabel.place(x=10, y=20)

#---------

MaxNumberEntry = tkinter.Entry(Window, text="", bd=2, width=4)
MaxNumberEntry.place(x=180, y=50)

PasswordOutput = tkinter.Entry(Window, text="", bd=2, width=30)
PasswordOutput.place(x=100, y=130)

#---------

Window.title('Strong Password Generator')
Window.iconbitmap("icon.ico")
Window.geometry("383x180")

Window.mainloop()