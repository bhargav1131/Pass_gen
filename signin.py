from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
# import pymysql
import mysql.connector
from mysql.connector import Error


def clear():
    username.delete(0, END)
    password.delete(0,END)
    confirm.delete(0, END)


def connect_database():
    if username.get() == '' or password.get() == '' or confirm.get() == '':
        messagebox.showerror("Error", "All fields are required")
    elif password.get() != confirm.get():
        messagebox.showerror('Error', 'Password does not match')
    else:
        try:
            con = mysql.connector.connect(host='localhost',user='root',password='bhargav')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database connectivity issue')
            return
        
        try:
            query = 'CREATE DATABASE userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'CREATE table data(id int auto_increment primary key not null, username varchar(21), password varchar(23))'
            mycursor.execute(query)
        except:
            mycursor.execute(query)


        query = 'SELECT * from data WHERE username = %s'
        mycursor.execute(query,(username.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username already exists')
        else:
            query = 'INSERT into data(username, password) values(%s, %s)'
            mycursor.execute(query,(username.get(), password.get())) 
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successfull')
            clear()
            base.destroy()
            import signin


#_______________________________________________________________________________________
base = Tk()  
base.geometry('600x500')  
base.title("Registration Form")  
username = StringVar()
password = StringVar()
confirm = StringVar()

labl_0 = Label(base, text="Registration form",width=20,font=("bold", 20))  
labl_0.place(x=90,y=53)  
    
    
labl_1 = Label(base, text="User Name",width=20,font=("bold", 10))  
labl_1.place(x=80,y=100)     
usernameEntry = Entry(base, textvariable=username, bd=0, width=20, border=2).place(x=48, y=130)
    
labl_2 = Label(base, text="Password",width=20,font=("bold", 10))  
labl_2.place(x=68,y=160)  
passwordEntry = Entry(base, textvariable=password, bd=0, width=30, border=2).place(x=48, y=180)  
    
labl_3 = Label(base, text="Confirm \nPassword",width=20,font=("bold", 10))  
labl_3.place(x=70,y=220)  
confirmEntry = Entry(base, textvariable=confirm, bd=0, width=30, border=2).place(x=48, y=270)  
    
Button(base, text='Submit',width=20,bg='brown',fg='white', command=connect_database).place(x=180,y=380)  

base.mainloop()  
