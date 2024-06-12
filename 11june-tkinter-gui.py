#button widget
from tkinter import *

root = Tk()
root.title("Tk Example")
root.minsize(200, 200) 
root.geometry("300x300+50+50")

def say_hello():
    print("Hello, World!")

button = Button(root, text="Click me", command=say_hello)
button.pack()
root.mainloop()

#message widget
from tkinter import *
main = Tk()
ourMessage = 'This is our Message'
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop()