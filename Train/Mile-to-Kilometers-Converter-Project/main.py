from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=900, height=500)

#label

my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack()
inp = Entry(width=29)
inp.pack()
def clicked():
    my_label.config(text=f"Hello {inp.get()}")
    print(inp.get())
    # print("Hello world")
btn = Button(text="Return", command=clicked)
# printbtn.get()
btn.pack()

window.mainloop()