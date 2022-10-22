#Created on 21st october, 2022
#Author: Bhargav Pratim Sharma
#Contact: bhargavsarma173@gmail.com
# _________________________________________________________

from tkinter import *
import pyperclip
import random
import string

root = Tk()
root.geometry("365x800")
root.resizable(False, False)
passwrd = StringVar()
pass_len = IntVar()
pass_len.set(0)
root.title("Pass-Buildozer")

backg = PhotoImage(file="Android Large - 1.png")
label1 = Label(image=backg)
label1.image = backg
label1.pack()


def generate():
    """
    This is the main function of the program to generate secure passwords
    """
    # set of characters
    set1 = string.ascii_lowercase
    set2 = string.ascii_uppercase
    set3 = string.digits
    set4 = string.punctuation

    # concatenating all sets
    s = []
    s.extend(list(set1))
    s.extend(list(set2))
    s.extend(list(set3))
    s.extend(list(set4))

    # shuffling the list
    random.shuffle(s)
    password = ""
    for x in range(pass_len.get()):
        password = password + random.choice(s)
    passwrd.set(password)


# function to copy the passcode
def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)

# inputs
Entry(root, textvariable=pass_len, bd=0, width=30, border=2).place(x=28, y=350)
Entry(root, textvariable=passwrd, bd=0, width=30, border=2).place(x=28, y=440)

# generate button
gen_img = PhotoImage(file="generate.png")
gen = Button(root, image=gen_img, bd=0, command=generate, bg="white", font=("MS Serif", 18, "bold"))
gen.place(x=115, y=660)

# copy button
copy_img = PhotoImage(file="copy.png")
copy = Button(root, image=copy_img, bd=0, command=copyclipboard, bg="white", font=("MS Serif", 18, "bold"))
copy.place(x=115, y=730)

# main event loop
root.mainloop()
