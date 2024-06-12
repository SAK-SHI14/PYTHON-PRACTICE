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

#Label Widget
from tkinter import *

root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")

text = Label(root, text="Nothing will work unless you do.")
text.pack()
text2 = Label(root, text="- Maya Angelou")
text2.pack()
root.mainloop()

#entry widget
from tkinter import *

root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")

e1 = Entry(root)
e1.pack()
root.mainloop()

#checkoutbutton widget
from tkinter import *

master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()

#radiobutton widget
from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
mainloop()

#Listbox Widget
from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()

#scrollbar widget
from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()

#menu widget
from tkinter import *
master = Tk()
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master.quit)
menubar.add_cascade(label="File", menu=filemenu)
master.config(menu=menubar)
mainloop()

#text widget
from tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, 'GeeksforGeeks\nBEST WEBSITE\n')
mainloop()

#canvas widget
from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()

#Spinbox Widget
from tkinter import *
master = Tk()
w = Spinbox(master, from_=0, to=10)
w.pack()
mainloop()
#TopLevel Widget
from tkinter import *
root = Tk()
root.title('GfG')
top = Toplevel()
top.title('Python')
top.mainloop()

#message widget
from tkinter import *
main = Tk()
ourMessage = 'This is our Message'
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop()

#frame widget
import tkinter as tk

root = tk.Tk()
root.title("Frame Example")

# Create a frame with a border
frame = tk.Frame(root, bd=2, relief="ridge")
frame.pack(fill="both", expand=True)

# Add some widgets to the frame
label = tk.Label(frame, text="Hello, World!")
label.pack()

button = tk.Button(frame, text="Click me")
button.pack()

root.mainloop()

# grid widget
import tkinter as tk

window = tk.Tk()
window.title("Python Grid Example")
window.geometry("480x360") 

text1 = tk.Label(window, text="Label 1")
text2 = tk.Label(window, text="Label 2")
text3 = tk.Label(window, text="Label 3")
text4 = tk.Label(window, text="Label 4")

text1.grid(row=0, column=0)
text2.grid(row=1, column=0)
text3.grid(row=0, column=1)
text4.grid(row=1, column=1)

window.mainloop()

#geometry management
import tkinter as tk

root = tk.Tk()
root.title("Place Geometry Manager")

label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")

label1.place(x=10, y=10)
label2.place(x=10, y=50)
label3.place(x=10, y=90)

root.mainloop()

#combining geometry managers
import tkinter as tk

root = tk.Tk()
root.title("Combining Geometry Managers")

frame1 = tk.Frame(root, bg="red")
frame2 = tk.Frame(root, bg="blue")

frame1.pack()
frame2.pack()

label1 = tk.Label(frame1, text="Label 1")
label2 = tk.Label(frame2, text="Label 2")

label1.grid(row=0, column=0)
label2.place(x=10, y=10)

root.mainloop()

#event handling 
import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click me!", command=button_clicked)
button.pack()
root.mainloop()