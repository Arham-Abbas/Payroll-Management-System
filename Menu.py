import tkinter
from tkinter import CENTER, ttk, messagebox
import Database as db
def login():
    def get():
        u=username.get()
        p=password.get()
        db.initialize(u,p)
        log.destroy()
    log=tkinter.Tk(screenName='Payroll Management System')
    log.title('Login')
    ttk.Label(log, text='Username').grid(column=0, row=0)
    ttk.Label(log, text='Password').grid(column=0, row=1)
    username=ttk.Entry(log)
    username.grid(column=1, row=0)
    password=ttk.Entry(log, show='*')
    password.grid(column=1, row=1)
    ttk.Button(log, text='Login', command=get).grid(column=0, row=2)
    ttk.Button(log, text='Cancel', command=log.destroy).grid(column=1, row=2)
    log.mainloop()
    if(db.connect != None):
        return True
    else:
        return False
def clean(x=0):
    children=frame2.winfo_children()
    for child in range(x, len(children)):   
        children[child].destroy()
def search(action):
    def get():
        clean(3)
        result=db.search(int(entries[0].get()))
        if result==None:
            messagebox.showinfo('Not Found','Could not find the specified ID in the database')
        elif action=='r':
            for i in range(5):
                ttk.Label(frame2, text=columns[i] + ': ' + str(result[i+1])).grid(column=0, row=i+2, padx=50)
            ttk.Label(frame2, text='Are you sure you want to delete the entry?').grid(column=0, row=7, padx=50, pady=10)
            def rem():
                clean(3)
                db.remove(result[0])
            ttk.Button(frame2, text='Remove', command=rem).grid(column=0, row=8)
            ttk.Button(frame2, text='Cancel', command=clean).grid(column=1, row=8)
        else:
            for i in range(5):
                ttk.Label(frame2, text=columns[i]).grid(column=0, row=i+2, padx=50)
                entries[i+1]=ttk.Entry(frame2, width=50)
                entries[i+1].grid(column=1, row=i+2)
                entries[i+1].insert(0,result[i+1])
            def mod():
                d=list()
                for i in range(5):
                    d.append(entries[i+1].get())
                d[2]=int(d[2])
                d[3]=int(d[3])
                d.append(result[0])
                clean(3)
                db.modify(d)
            ttk.Button(frame2, text='Save', command=mod).grid(column=0, row=8)
            ttk.Button(frame2, text='Cancel', command=clean).grid(column=1, row=8)
    clean()
    entries=[None]*6
    ttk.Label(frame2, text='Enter ID to search').grid(column=0, row=0, padx=50, pady=10)
    entries[0]=ttk.Entry(frame2)
    entries[0].grid(column=1, row=0, padx=50, pady=10)
    ttk.Button(frame2, text='SEARCH', command=get).grid(column=0, row=1, padx=50)
def show():
    clean()
    result=db.show()
    tree=ttk.Treeview(frame2, columns=['#1','#2','#3','#4','#5'], height=len(result))
    tree.grid(column=0, row=0, padx=20, pady=10)
    tree.column('#0',width=50)
    tree.heading('#0',text='ID')
    for i in range(1,6):
        tree.column('#' + str(i),anchor=CENTER)
        tree.heading('#' + str(i),text=columns[i-1])
    for i in result:
        tree.insert('',index=tkinter.END, iid=i[0], text=i[0], values=i[1:])
def add():
    def get():
        result=list()
        for i in range(5):
            result.append(entries[i].get())
            entries[i].delete(0,'end')
        db.add(result)
    clean()
    entries=[None]*5
    for i in range(5):
        ttk.Label(frame2, text=columns[i]).grid(column=0, row=i, padx=50, pady=5)
        entries[i]=ttk.Entry(frame2, width=50)
        entries[i].grid(column=1, row=i, pady=5)
    ttk.Button(frame2, text='ADD', command=get).grid(column=0, row=5, pady=10)
def remove():
    search('r')
def modify():
    search('m')
if(login()):
    columns=['Name','Email','Contact','Salary','Address']
    screen=tkinter.Tk(screenName='Payroll Management System')
    screen.attributes('-fullscreen',True)
    screen.title('Payroll Management System')
    frame=ttk.Frame(screen)
    frame.grid(column=0, row=0)
    frame2=ttk.Frame(screen)
    frame2.grid(column=1,row=0)
    ttk.Label(frame, text='M A I N  M E N U').grid(column=0, row=0, padx=10, pady=10)
    ttk.Button(frame, text='Show all Employees', command=show).grid(column=1, row=1)
    ttk.Button(frame, text='Add a new Employee', command=add).grid(column=1, row=2)
    ttk.Button(frame, text='Remove an Employee', command=remove).grid(column=1, row=3)
    ttk.Button(frame, text='Modify Details of an Employee', command=modify).grid(column=1, row=4)
    ttk.Button(frame, text='Exit', command=screen.destroy).grid(column=1, row=5)
    screen.mainloop()