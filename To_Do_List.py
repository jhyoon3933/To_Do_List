from tkinter import *
from tkinter import messagebox
import sys
import time

def raise_frame(frame):
    frame.tkraise()

window = Tk()
window.title('Stay on Top')
window.geometry('360x600')  # geometry of window
window.resizable(0, 0)

# Frames
list_frame = Frame(window, width = 360, height = 540)
list_frame.pack_propagate(0)    # widgets dont affect frame size
list_frame.place(x = 0, y = 60)
timer_frame = Frame(window, width = 360, height = 540)
timer_frame.pack_propagate(0)
timer_frame.place(x = 0, y  = 60)

# Menu Button
list_button = Button(window, text = 'TO-DO LIST', width = 17, height = 2, command = lambda: raise_frame(list_frame))
timer_button = Button(window, text = 'POMODORO TIMER', width = 17, height = 2, command = lambda: raise_frame(timer_frame))


# ToDoList Frame Buttons and Entry
listFrame_Name = Label(list_frame, text = 'To-Do List',font = ('Helvetica', 18))
task_entry = Entry(list_frame, width = 30, borderwidth = 3)
addTask = Button(list_frame, text = 'Add Task', width = 10, height = 3, command = lambda: addTask_func(task_entry.get()))
removeTask = Button(list_frame, text = 'Remove Task', width = 10, height = 3, command = lambda: removeTask_func())
toDoList = Listbox(list_frame, width = 30, height = 21)  # selectmode = EXTENDED --> multiple items can be chosen

# Clock Commands

def clock():
    curr_time = time.strftime('%H:%M:%S')
    clock_label.config(text = curr_time)
    clock_label.after(100, clock)

# Pomodoro Timer Commands

def signal():
    messagebox.showinfo('Pomodoro Session Begins', 'Pomodoro Study Session of 25 Minutes (1500 Seconds)')
    return count_down(1500)

def count_down(t):
    global x
    x = 1
    if x == 1:
        count.config(text = 'Time Remaining in Session: ' + str(t), font = ('Helvetica', 18, 'bold'))
        if t > 0:
            timer_frame.after(1000, count_down, t-1)
        elif t == 0:
            ask_user = messagebox.askyesno('Pomodoro Session Finished', 'Do you want to continue on with Another Session?')
            if ask_user == True:
                return count_down(1500)
            elif ask_user == False:
                messagebox.showinfo('Exiting Frame', 'Closing Pomodoro Session')
            
    
# Timer Frame Buttons and Entry
timerFrame_Name = Label(timer_frame, text = 'Pomodoro Timer',font = ('Helvetica', 18))
clock_label = Label(timer_frame, font = ('Helvetica', 50))
start_button = Button(timer_frame, text = 'START', width = 15, height = 4, font = ('Helvetica', 15), command = lambda: signal())
count = Label(timer_frame, text = '', font = ('Impact', 20))
#pomodoro = Label(timer_frame, text = 'Pomodoro Sessions: ' + str(pomodoro_count), font = ('Helvetica', 20))

# Button Commands

def addTask_func(input):
    toDoList.insert(END, input)
    task_entry.delete(0, END)

def removeTask_func():
    index = toDoList.curselection() # tuple with currently selected index values
    toDoList.delete(index)

# Menu Button Positions
list_button.place(x = 10, y = 10, bordermode = 'inside')  # inside bordermode considers size of rootframe in placing objct, while outside considers screensize
timer_button.place(x = 190, y = 10, bordermode = 'inside')

# ToDoList Widget Coordinate Positions
task_entry.place(x = 35, y = 40, bordermode = 'outside')
addTask.place(x = 77, y = 85, bordermode = 'outside')
listFrame_Name.place(x = 129, y = 10, bordermode = 'outside')
toDoList.place(x = 40, y = 150, bordermode = 'outside')
removeTask.place(x = 177, y = 85, bordermode = 'outside')

# Timer Widget Coordinate Positions
timerFrame_Name.place(x = 110, y = 10, bordermode = 'outside')
clock_label.place(x = 75, y = 60, bordermode = 'outside')
start_button.place(x = 105, y = 160, bordermode = 'outside')
count.place(x = 30, y = 300, bordermode = 'outside')


raise_frame(list_frame)
clock()
window.mainloop()
