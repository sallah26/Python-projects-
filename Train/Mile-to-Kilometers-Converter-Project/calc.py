from tkinter import *

window = Tk()
window.title("My Data size with GUI Converter program")
window.minsize(width=1200, height=700)

#label

my_label = Label(text="Hello africians and also those", font=("Arial", 24, "bold"))
my_label.pack()



# #listbox

input = Entry(width=23)
# inp = input.get()
input.pack()

def Vals():
    print("Btn has been clicked")
    inp = input.get()
    print(inp)
    print("😂😂😂😂😂", listed)
    
    def listbox_used(event):
        listed = listbox.get(listbox.curselection())
        # print("this", listed)
        if listed == "Giga-Byte":
            print("Hello, Giga clicked😂😂😂😂😂")

        listbox = Listbox(height=6, font=("Arial", 14, ))
        fruits = ["Byte", "Kilo-Byte", "Mega-Byte", "Giga-Byte", "Tera-Byte", "Bit"]
        for item in fruits:
            listbox.insert(fruits.index(item), item)
        listbox.bind("<<ListboxSelect>>", listbox_used)
        listbox.pack()   





# print(inp)

#button
btn = Button(text="CONVERT",command=Vals)

# printbtn.get()
btn.pack()
# side="bottom"

window.mainloop()








# #Scale 
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()


