from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image
#creating a window 
win=Tk()
win.title("to-do list")
win.iconbitmap('C:/Users/DELL/hello/to-do-list.ico')
win.geometry('500x500')
win.configure(bg='#56667A')
title_label=Label(win,text="to-do-list",bg="#ea8091",font=("sans",20)).grid(row=0,column=1,pady=20,ipadx=10,ipady=10)
#connection with db
conn=sqlite3.connect('todolistdb.db')

c=conn.cursor()

######create a table inside the db
'''
c.execute(""" create table todotable(
    stuff_to_do text)
    """)
'''    

###
#once the table is created once, there's no need to create it again>
# that's we comment it out!!

###
#insert button:
def insert():
    conn=sqlite3.connect('todolistdb.db')
    c=conn.cursor()
    if (name_entry.get()!= ''):
        c.execute("insert into todotable values (:todostuff)",
        {
            'todostuff': name_entry.get()
        })
        messagebox.showinfo("inserted successfully"," you have a thing to do,hehe!!")
    else:
        messagebox.showinfo("warning!","dude type something,dont waste memory in my db!!!!!!!!!!")    
    conn.commit()

    conn.close()

    name_entry.delete(0,END)
    


def show_all():
    conn=sqlite3.connect('todolistdb.db')
    c=conn.cursor()

    c.execute('select *,oid from todotable')
    allstuff=c.fetchall()
    #print(allstuff)
    #messagebox.showinfo("everything ig", allstuff)
    print_allstuff=''
    for stuff in allstuff:
        #print_allstuff += str(stuff[1]) + " " + str(stuff[0]) + "\n" this statement prints them with a numbered system.
        print_allstuff += str(stuff[0]) + "\n"
        #messagebox.showinfo("everything ig", stuff)
    query_label=Label(win,text=print_allstuff,bg="#D9E5D6",fg="#007EA7")
    query_label.grid(row=6,column=1,columnspan=2)    

    conn.commit()
    conn.close()
#entry boxes
name=Label(win,text="enter stuff to do:",bg='#FFCAD4')
name.grid(row=1,column=0,padx=10,pady=10)
name_entry=Entry(win,width=50,bg='#5F4B66')
name_entry.grid(row=1,column=1,padx=10,pady=10)



#show topmost button
def show_top():
    conn=sqlite3.connect('todolistdb.db')
    c=conn.cursor()

    c.execute('select stuff_to_do from todotable')
    
    messagebox.showinfo("topmost",c.fetchone())    

    conn.commit()
    conn.close()



#delete topmost

def delete_top():
    conn=sqlite3.connect('todolistdb.db')
    c=conn.cursor()
    #count=0
    #count=(c.execute('select count(*) from todotable'))
    
    #if (count!=''):

    c.execute('delete from todotable where rowid in (select rowid from todotable limit 1)')
    messagebox.showinfo("deleted","deleted topmost thing successfully")
    #else:
        #messagebox.showinfo("delete error","dude you don't have anything left to delete")

    conn.commit()
    conn.close()



##buttons
#insert button
insert_btn=Button(win,text="insert stuff into your list!!",command=insert,bg='#FFCAD4')
insert_btn.grid(row=2,column=1,padx=10,pady=10)
#show your list button.
show_btn=Button(win,text="show all things,pwease",command=show_all,bg='#FFCAD4')
show_btn.grid(row=3,column=1,padx=10,pady=10)
#show topmost entry button.
top_btn=Button(win,text="show the first thing,pwease",command=show_top,bg='#FFCAD4')
top_btn.grid(row=4,column=1,padx=10,pady=10)
#
delete_btn=Button(win,text="delete top entry",command=delete_top,bg='#FFCAD4')
delete_btn.grid(row=5,column=1,padx=10,pady=10)




#
conn.commit()

#closing connection between db and app
conn.close()

#
win.mainloop()

