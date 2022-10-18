def hello():
    print("Бабл Квас")



hello()

neme = input("черкать тут:")


def hellouser(userneme):
    print("ривет", userneme)

hellouser(neme)

print("ти получил блеона")


def qwer(num1,num2,num3):
    return num1 * num2 + num3


print(qwer(int(input("число:")),int(input("число:")),(int(input("число:")))))

print("ти получил ящик")

#var_1 = 5
#def func_1():
#    var_1 = 10
#    print(var_1)

#func_1()
#print(var_1)

#var_1 = 5
#def func_1():
#    var_1 = 1
#    print(var_1)
#    var_1 = 1
#    print(var_1)
#    print(var_1)
#func_1()

#var_1 = 5
#def first():
#    var_1 = 10
#    def second():
#        print(var_1)
#    second()
#
#
#first()
#print(var_1)

from random import  randint

def coin_simulator():
    coin = randint(0, 2)
    if coin == 0:
        print("ти ворон")
    if coin == 1:
        print("ти ЕлЬ ПапА")
    if coin == 2:
        print("ти скала")

coin_simulator()



import random


def game(choice, result):
    print("")
    print("=====Start Game rock, paper, scissors == == = ")
    computer_choice = random.choice("rps")
    print("--------------------------------")
    print("Your select – ", str.capitalize(choice))
    print("Computer select —", str.capitalize(computer_choice))
    if str.lower(choice) == computer_choice:
        print("Result of game – Draw")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "r" and computer_choice == "p":
        result["computer"] += 1
        print("ти бот")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "r" and computer_choice == "s":
        result["player"] += 1
        print("ти ЕлЬ ПапА")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "p" and computer_choice == "s":
        result["computer"] += 1
        print("ти бот")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "p" and computer_choice == "r":
        result["player"] += 1
        print("ти ЕлЬ ПапА")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "s" and computer_choice == "r":
        result["computer"] += 1
        print("ти бот")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "s" and computer_choice == "p":
        result["player"] += 1
        print("ти ЕлЬ ПапА")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")

result = {"computer": 0, "player": 0}

choise = input("Select R / P / S – ")
game(choice=choise, result=result)

from tkinter import *
from tkinter import messagebox
import random

HEIGHT = 600
WIDTH = 600

tasks = ["заметки бабл квас"]

root = Tk()
root.title('My Super To-Do List')
root.geometry('%dx%d' % (WIDTH, HEIGHT))
root.resizable(False, False)

img = PhotoImage(file='todo_bg.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

root.option_add('*Font', '{Comic Sans MS} 10')
root.option_add('*Background', 'white')

frame = Frame(root, bd=10)
frame.place(relx=0.1, rely=0.1, relwidth=0.8,
            relheight=0.8)

label_title = Label(frame, text='заметки бабл квас', fg='dark blue', font='{Comic Sans MS} 16')
label_title.place(relx=0.3)
label_display = Label(frame, text='')
label_display.place(relx=0.3, rely=0.1)
text_input = Entry(frame, width=15)
text_input.place(relx=0.3, rely=0.15, relwidth=0.6)


def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

def add_task():
        task = text_input.get()
        if task != '':
            tasks.append(task)
            update_listbox()
        else:
            messagebox.showwarning('Warning', 'box')
            text_input.delete(0, END)

button_add_task = Button(frame, text='добавить заметку', command=add_task)
button_add_task.place(rely=0.15, relwidth=0.25)


def del_one():
        task = listbox.get('active')
        if task in tasks:
            tasks.remove(task)
        update_listbox()


button_del = Button(frame, text='удалить заметку', command=del_one)
button_del.place(rely=0.25, relwidth=0.25)


def del_all():
        confirmed = messagebox.askyesno('Please Confirm', 'Do you really want to delete all?')
        if confirmed:
            global tasks
            tasks = []
            update_listbox()


button_del_all = Button(frame, text='удалить всізаметки', command=del_all)
button_del_all.place(rely=0.35, relwidth=0.25)


def sort_asc(args):
    def sort_asc():
        tasks.sort()
        update_listbox()


button_sort_asc = Button(frame, text='сортировать (с-а)', command=sort_asc)
button_sort_asc.place(rely=0.45, relwidth=0.25)


def sort_desc(args):
    def sort_desc():
        tasks.sort()
        tasks.reverse()
        update_listbox()



button_sort_desc = Button(frame, text='сортировать (а-с)', command=sort_desc)
button_sort_desc.place(rely=0.55, relwidth=0.25)


def choose_random():
        if len(tasks) > 0:
            task = random.choice(tasks)
            label_display['text'] = task
        else:
            messagebox.showwarning('Warning', 'No tasks')


button_random = Button(frame, text='шукать заметку', command=choose_random)
button_random.place(rely=0.65, relwidth=0.25)


def show_number_of_tasks():
        number_of_tasks = len(tasks)
        message = 'Number of tasks: %s' % number_of_tasks
        label_display['text'] = message


button_number_of_tasks = Button(frame, text='номера заметок', command=show_number_of_tasks)
button_number_of_tasks.place(rely=0.75, relwidth=0.25)

button_exit = Button(frame, text='пока друг:(',
                     command=exit)
button_exit.place(rely=0.85, relwidth=0.25)

listbox = Listbox(frame)
listbox.place(relx=0.3, rely=0.24, relwidth=0.6,
              relheight=0.6)

mainloop()