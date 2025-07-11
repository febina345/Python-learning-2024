from tkinter import *


window=Tk()
window.geometry("500x500")
window.title("febs")
window.configure(bg='blue')

def hello():
    print("button clicked")

button1 =Button(window,text="ok",bg="yellow", fg="red",command=hello)
button2 =Button(window,text="ok",bg="yellow", fg="red",command=hello)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
label=Label(window,text="Welcome")






window.mainloop()

