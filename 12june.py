#Storing text from a Textbox in a Python variable
import tkinter as tk

def get_text():
    text = textbox.get("1.0", "end-1c")
    print(text)   

root = tk.Tk()
root.title("Textbox Example")

textbox = tk.Text(root, width=40, height=10)
textbox.pack()

button = tk.Button(root, text="Get Text", command=get_text)
button.pack()

root.mainloop()

#Performing an action when a button is clicked
import tkinter as tk

def say_hello():
    print("Hello, World!")

root = tk.Tk()
root.title("Button Example")

button = tk.Button(root, text="Click me", command=say_hello)
button.pack()

root.mainloop()

#Practical example: Simple Calculator
import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Simple Calculator")

label1 = tk.Label(root, text="Number 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Number 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="Calculate", command=calculate)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()


