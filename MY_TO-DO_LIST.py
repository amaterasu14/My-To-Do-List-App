# Importing all the necessary modules
from tkinter import *
import time
from tkinter import messagebox

# Creating the tasks.txt file
with open("tasks.txt", "w") as tasks_file_create:
    tasks_file_create.write("")

# Adding and Deleting items functions
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()
    if new_task != "":
        if new_task != "Type your task here":
            listbox.insert(END, new_task)
            entry.delete(0, "end")
            with open('tasks.txt', 'a') as tasks_list_file:
                tasks_list_file.write(f'{new_task}')
                tasks_list_file.write(f'\n')

    if new_task == "Type your task here":
        messagebox.showwarning("warning", "Please, enter a task.")

    else:
        messagebox.showwarning("warning", "Please, enter a task.")


def delete_item(listbox: Listbox):
    anchor = listbox.get(ANCHOR)
    items_list = enumerate(listbox.get(0, END))

    file = open('tasks.txt', 'w')
    file.truncate()

    for i, listb in items_list:
        if listb == anchor:
            listbox.delete(i)
        else:
            file.writelines(listb)

    file.close()

# Initializing the GUI window
root = Tk()
root.title('My To-Do List Application')
root.geometry('400x500')
root.resizable(0, 0)
root.config(bg="PaleVioletRed")

# Heading Label
Label(root, text='My To-Do List Application', fg= "purple", bg='black', font=("Verdana", 16), wraplength=300).place(
    x=70, y=10)

# Listbox with all the tasks with a Scrollbar
tasks = Listbox(root, selectbackground='Purple', bg='Pink', font=('Verdana', 12), height=12, width=33)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=368, y=50, height=232)

tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=50)


#horizontal scroller
scroller2 = Scrollbar(root, orient=HORIZONTAL, command=tasks.xview)
scroller2.place(x=35, y=282, width=350)

tasks.config(xscrollcommand=scroller.set)
tasks.place(x=35, y=50)

# Adding items to the Listbox
with open('tasks.txt', 'r+') as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()

# Creating the Entry widget where the user can enter a new item
def temp_text(e):
    new_item_entry.delete(0, "end")

new_item_entry = Entry(root, width=57)
new_item_entry.place(x=35, y=310)
new_item_entry.insert(0, "Type your task here")

new_item_entry.bind("<FocusIn>", temp_text)

# Creating the Buttons
add_btn = Button(root, text='Add Item', fg= 'black', bg='purple', width=10, font=('Verdana', 12),
                 command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=60, y=350)

delete_btn = Button(root, text='Delete Item', fg= 'black', bg='purple', width=10, font=('Verdana', 12),
                 command=lambda: delete_item(tasks))
delete_btn.place(x=240, y=350)

# Adding a clock to the application
def set_clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    clock_label.config(text= hour + ":" + minute + ":" + second)
    clock_label.after(1000, set_clock)

clock_label = Label(root, text="", font=("Verdana", 18), fg="purple", bg="black")
clock_label.pack(anchor=SW)
clock_label.place(x=145,y=430)


set_clock()


# Finalizing the window
root.update()
root.mainloop()

