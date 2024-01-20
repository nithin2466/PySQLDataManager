from tkinter import *
import mysql.connector as mysql
import sqlite3
import tkinter.messagebox as msgbox

n=Tk()
n.title("Student Registration")
n.geometry('500x500')
#insert function
def Insert():
    id=stid_entry.get()
    name=stname_entry.get()
    phno=stphno_entry.get()
    if(id=="" or name=="" or phno==""):
        msgbox.showinfo("Alert","fill all fields")
    else:
        con=mysql.connect(host="localhost",user="root",password="Hey123",database="student")
        con=sqlite3.connect("studentdb.db")
        cur=con.cursor()
        
        #cur.execute("create table person(id int,name varchar(20),phno int(11))")
        cur.execute("insert into person values('"+id+"','"+name+"','"+phno+"')")
        cur.execute("Commit")
        msgbox.showinfo("info","record inserted successfully")
#delete function
def Delete():
    id=stid_entry.get()
    if(id==""):
        msgbox.showinfo("Alert","Enter Student Id")
    else:
        con=sqlite3.connect("studentdb.db")
        cur=con.cursor()
        cur.execute("delete from person where id='"+id+"'")
        con.commit()
        msgbox.showinfo("info","record deleted successfully")

#reset function
def Reset():
    stid_entry.delete(0, 'end')
    stname_entry.delete(0, 'end')
    stphno_entry.delete(0, 'end')

#view function
#view function
def View():
    con=sqlite3.connect("studentdb.db")
    cur=con.cursor()
    cur.execute("select * from person")
    rows = cur.fetchall()
    result = '' 
    for row in rows:
        result += 'ID: ' + str(row[0]) + ', Name: ' + str(row[1]) + ', Phone: ' + str(row[2]) + '\n'
    msgbox.showinfo("Records", result)
#update function
def Update():
    id=stid_entry.get()
    name=stname_entry.get()
    phno=stphno_entry.get()
    if(id=="" or name=="" or phno==""):
        msgbox.showinfo("Alert","fill all fields")
    else:
        con=sqlite3.connect("studentdb.db")
        cur=con.cursor()
        cur.execute("update person set name='"+name+"', phno='"+phno+"' where id='"+id+"'")
        con.commit()
        msgbox.showinfo("info","record updated successfully")

#update button
updatebtn=Button(n,text="UPDATE",font=("Verdana",16),command=Update)
updatebtn.grid(row=7,column=1,padx=10,pady=10)


#delete button
deletebtn=Button(n,text="DELETE",font=("Verdana",16),command=Delete)
deletebtn.grid(row=4,column=1,padx=10,pady=10)

#reset button
resetbtn=Button(n,text="RESET",font=("Verdana",16),command=Reset)
resetbtn.grid(row=5,column=1,padx=10,pady=10)

#view button
viewbtn=Button(n,text="VIEW",font=("Verdana",16),command=View)
viewbtn.grid(row=6,column=1,padx=10,pady=10)

#student id field
stid=Label(n,text="Student Id:",font=("Verdana",16))
stid.grid(row=0,column=0)
stid_entry=Entry(n,font=("Verdana",16))
stid_entry.grid(row=0,column=1,padx=10,pady=10)
#student name field
stname=Label(n,text="Student Name:",font=("Verdana",16))
stname.grid(row=1,column=0)
stname_entry=Entry(n,font=("Verdana",16))
stname_entry.grid(row=1,column=1,padx=10,pady=10)
#student phno field
stphno=Label(n,text="Student phno:",font=("Verdana",16))
stphno.grid(row=2,column=0)
stphno_entry=Entry(n,font=("Verdana",16))
stphno_entry.grid(row=2,column=1,padx=10,pady=10)
#button
insertbtn=Button(n,text="INSERT",font=("Verdana",16),command=Insert)
insertbtn.grid(row=3,column=1,padx=10,pady=10)

n.mainloop()
