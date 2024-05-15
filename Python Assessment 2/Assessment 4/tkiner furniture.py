from tkinter import *
import mysql.connector
import tkinter.messagebox as msg


def create_conn():
    return mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="python_10_30_tts"
       )

#TOTAL

def total_data():
    total = 0
    quantity_entry = e_quantity.get()
    price_entry = e_price.get()

    if quantity_entry.isdigit() and price_entry.replace('.', '', 1).isdigit():
        
        quantity = int(quantity_entry)
        price = float(price_entry)
        total = quantity * price
        e_total.delete(0, 'end')
        e_total.insert(0, total)
    else:
        msg.showinfo("Error", "Please enter valid numbers for quantity and price")

#INSERT DATA

def insert_data():
    if e_id.get()=="" or e_pname.get()=="" or e_quantity.get()=="" or e_price.get()=="" or e_total.get()=="":
        msg.showinfo("Insert Status","All Field are Mandatory")

    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into furniture(id,pname,quantity,price,total) values(%s,%s,%s,%s,%s)"
        args=(e_id.get(),e_pname.get(),e_quantity.get(),e_price.get(),e_total.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_pname.delete(0,'end')
        e_quantity.delete(0,'end')
        e_price.delete(0,'end')
        e_total.delete(0,'end')
        msg.showinfo("Insert Status","Insert data successfully")

#SEARCH DATA

def search_data():
    
    e_pname.delete(0,'end')
    e_quantity.delete(0,'end')
    e_price.delete(0,'end')
    e_total.delete(0,'end')
    if e_id.get()=="" :
        msg.showinfo("Search Status","Id is  Mandatory")

    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from furniture where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
             #e_id.insert(0,row[0][1])
             e_pname.insert(0,row[0][1])
             e_quantity.insert(0,row[0][2])
             e_price.insert(0,row[0][3])
             e_total.insert(0,row[0][4])
        else:
            msg.showinfo("Search Status","Id not found")
            
        conn.close()

#UPDATE DATA

def update_data():
    if e_id.get()=="" or e_pname.get()=="" or e_quantity.get()=="" or e_price.get()=="" or e_total.get()=="":
        msg.showinfo("Update Status","All Field are Mandatory")

    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update furniture set pname=%s,quantity=%s,price=%s,total=%s where id=%s"
        args=(e_pname.get(),e_quantity.get(),e_price.get(),e_total.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_pname.delete(0,'end')
        e_quantity.delete(0,'end')
        e_price.delete(0,'end')
        e_total.delete(0,'end')
        msg.showinfo("Update Status","Update data successfully")

#DELETE DATA

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","ID is Mandatory")

    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from furniture where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_pname.delete(0,'end')
        e_quantity.delete(0,'end')
        e_price.delete(0,'end')
        e_total.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")

        
root=Tk()
root.geometry("500x500")
root.title("Furniture Shop")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_pname=Label(root,text="PRODUCT NAME")
l_pname.place(x=50,y=100)

l_quantity=Label(root,text="QUANTITY")
l_quantity.place(x=50,y=150)

l_price=Label(root,text="PRICE")
l_price.place(x=50,y=200)

l_total=Label(root,text="TOTAL PRICE")
l_total.place(x=50,y=250)

l_Info=Label(root,text="ID Info")
l_Info.place(x=350,y=50)

l_Chair=Label(root,text="101.Chair")
l_Chair.place(x=350,y=80)

l_Table=Label(root,text="102.Table")
l_Table.place(x=350,y=105)

l_Sofa=Label(root,text="103.Sofa")
l_Sofa.place(x=350,y=130)

l_Bed=Label(root,text="104.Bed")
l_Bed.place(x=350,y=155)

l_Desks=Label(root,text="105.Desks")
l_Desks.place(x=350,y=180)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_pname=Entry(root)
e_pname.place(x=150,y=100)

e_quantity=Entry(root)
e_quantity.place(x=150,y=150)

e_price=Entry(root)
e_price.place(x=150,y=200)

e_total=Entry(root)
e_total.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial",12),command=insert_data)
insert.place(x=21,y=365)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial",12),command=search_data)
search.place(x=92,y=365)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial",12),command=update_data)
update.place(x=174,y=365)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial",12),command=delete_data)
delete.place(x=254,y=365)

total=Button(root,text="TOTAL",bg="black",fg="white",font=("Arial",12),command=total_data)
total.place(x=171,y=300)

root.mainloop()
