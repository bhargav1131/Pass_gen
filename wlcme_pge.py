from tkinter import *

ws = Tk()
ws.geometry("363x800")
ws.title('Pass-Buildozer')
ws.resizable(False, False)

backg = PhotoImage(file="welcome-page.png")
label1 = Label(image=backg)
label1.image = backg
label1.pack()

def nextPage():
    ws.destroy()
    import main_code
    
# continue button
continue_img = PhotoImage(file="continue.png")
continue1 = Button(ws, image=continue_img, bd=0, command=nextPage, bg="white")
continue1.place(x=110, y=725)

ws.mainloop()