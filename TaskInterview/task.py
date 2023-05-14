import tkinter
from tkinter import *
import pandas as pd
from tkinter import messagebox

TaskList=[]

#============================================Function Part===========================
# Tasks File Function
def OpenTaskFile():
    try:
        with open("Tasks.csv", 'r') as file:
            # Read the file line by line
            for line in file:
                print(line)

                if line!="Tasks\n":
                    # Add each line to the Listbox
                    TaskList.append(line.strip()) # to save the list without the new line
                    listbox.insert(END, line.strip())

    except:
        file=open("Tasks.csv","w")     # to make a file if the file not exists
        file.close()

# Add Tasks
def AddTasks():

    task=TaskEntry.get()    # to get the value of the entry
    if task=="":
        messagebox.showerror("Error")
    else:

        TaskEntry.delete(0,END)  # to delele the entry
        if task:
            with open ("Tasks.csv","a") as TaskFile:
                TaskFile.write(f"\n{task}")
            TaskList.append(task)  # then insert the value to list
            listbox.insert(END,task)  # then insert the value to list box to view



# Delete Function
def DeleteTasks():
    global TaskList
    task=str(listbox.get(ANCHOR)) # to get the value that the user choose it
    if task in TaskList:
        TaskList.insert(0,"Tasks")
        TaskList.remove(task)  # to remove the task from Task list
        with open("Tasks.csv","w") as file:
            for task in TaskList:
                file.write(task+"\n")
        listbox.delete(ANCHOR)
#Update Function
def UpdateTaskGUI():
    UpdateWindows=Tk()
    UpdateWindows.geometry("200x100+200+100")
    Label(UpdateWindows,text="Updated value",font="arial 12 bold").place(x=30,y=10)
    UpdatedEntry=Entry(UpdateWindows,width=20)
    UpdatedEntry.place(x=30,y=35)

    def UpdateValue():
        task = (listbox.get(ANCHOR))  # to get the value that the user choose it
        task1=listbox.curselection()
        UpdatedEntryValue = UpdatedEntry.get()
        if UpdatedEntryValue =="":
            messagebox.showerror("Error","Enter value")
        else :
           # TaskList = list(map(lambda x: x.replace(task,UpdatedEntryValue), TaskList))
           df = pd.read_csv('Tasks.csv', delimiter='\t')
           index_list = df[df['Tasks'] == task].index.tolist()
           #=======================================
           def convert(list):
               # Converting integer list to string list
               s = [str(i) for i in list]
               # Join list items using join()
               res = int("".join(s))
               return (res)
           index=convert(index_list)
           colum = 'Tasks'
           #==========================================

           df.at[index,colum]=UpdatedEntryValue
           listbox.delete(task1)
           listbox.insert(task1, UpdatedEntryValue)
           df.to_csv('Tasks.csv', sep='\t', index=False)


    Button(UpdateWindows,text="update",command=UpdateValue,fg="#32405b").place(x=60,y=60)

def DoneCheck():
    if not listbox.curselection():
        messagebox.showerror("Error","Please choose the item")
    else:
        listbox.itemconfig(listbox.curselection(),fg="#84a3e1")
        listbox.select_clear(0,END)




#=========================================GUI Part=========================================
root=Tk()
root.title("To-Do-List-GUI")
root.geometry("400x700+400+700")  # this is the hight and width for the root frame
root.resizable(False,False) # to prevent change the root size
gui_icon=PhotoImage(file="to-do-list.png") # put the icon for the root
root.iconphoto(False,gui_icon)

# TOP BAR
TopBarImage=PhotoImage(file="topbar.png") # put the top bar for the application
Label(root,image=TopBarImage).pack()

# Home
Label(root,text="Home",bg= '#32405b',fg="#c1d0f0",font="arial 20 bold").place(x=160,y=25)

#heading
AllTaskLabel=Label(root,text="All Tasks",font="arial 20 bold",fg="black")
AllTaskLabel.place(x=130,y=120)

# Icons
TodoImage=PhotoImage(file="todoapp.png")
Label(root,image=TodoImage).place(x=70,y=110)

#Frame for Tasks
TaskFrame=Frame(root,width=400,height=50,bg="white")
TaskFrame.place(x=0,y=180)



# Task Entry
TaskEntry= Entry(TaskFrame,width=18,font="arial 20 bold",bd=0)
TaskEntry.place(x=10,y=7)
TaskEntry.focus()

# Add Button
AddButton=Button(TaskFrame,text="Add",font="arial 20 bold",bg="#c1d0f0",width=6,command=AddTasks)
AddButton.place(x=300,y=0)

# Frame for all Task
AllTaskFrame=Frame(root,width=700,height=280,bg="#32405b")
AllTaskFrame.pack(pady=(160,0))

#ListBox
listbox=Listbox(AllTaskFrame,font=('arial bold',12,),width=40,height=16,bg="#c1d0f0")
listbox.pack(side=LEFT,fill=BOTH,pady=2)

#Scrollbar
scollerbar=Scrollbar(AllTaskFrame)
scollerbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scollerbar.set)
scollerbar.config(command=listbox.yview)

# call the function
OpenTaskFile()
# delete
DeleteIcon=PhotoImage(file="trash.png")
Button(root,image=DeleteIcon,bd=0,command=DeleteTasks).place(x=160,y=580)

# update icons
UpdateIcons=PhotoImage(file="update.png")
Button(root,image=UpdateIcons,bd=0,command=UpdateTaskGUI).place(x=2,y=580)

# done incons

DoneIcons=PhotoImage(file="success.png")
Button(root,image=DoneIcons,bd=0,command=DoneCheck).place(x=340,y=580)

# Label
Label(root,text="Success is survival",font="arial 20 bold",fg="#32405b").place(x=60,y=650)

# start the main
root.mainloop()


