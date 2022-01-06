from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="prasanna",database="dbmsproject")
check=0

def enter():
    def addcar():

        e1=ent1.get()
        e2=ent2.get()
        e3=ent3.get()
        cur=con.cursor()
        x='y'
        cur.execute("insert into cars(car_id,brand,rent,available) values(%s,%s,%s,%s)",(e1,e2,e3,x))
        con.commit()
        carid.delete(0,END)
        brand.delete(0,END)
        price.delete(0,END)
        messagebox.showinfo('success',"car inserted!")
    #frame2add()

#function for deleting a car
    def delcar():
        e1=ent1.get()
        e2=ent2.get()
        e3=ent3.get()
        cur=con.cursor()
        x='y'
        cur.execute("delete from cars where car_id=%s and available=%s",(e1,x))
        con.commit()
        carid.delete(0,END)
        brand.delete(0,END)
        price.delete(0,END)
        messagebox.showinfo('success','car deleted!!')

#creating the main window
    root=Toplevel()
    root.geometry("500x500")
    root.title("DBMS PROJECT by PRASANNA,PRITISH,PREMKANNA")

    #creating a notebook for tabs(admin,book,return)
    notebook=ttk.Notebook(root)
    notebook.pack()

    #creating 3 frames 
    frame1=Frame(notebook,width=500,height=500)
    frame2=Frame(notebook,width=500,height=500)  
    frame3=Frame(notebook,width=500,height=500)

    frame1.pack(fill="both",expand=1)
    frame2.pack(fill="both",expand=1)
    frame3.pack(fill="both",expand=1)

    notebook.add(frame1,text="admin")
    notebook.add(frame2,text="book")
    notebook.add(frame3,text="return")

    #notebook.hide(1)

    # def show():
    #    notebook.add(frame2,text="book")


    ent1=IntVar()
    ent2=StringVar()
    ent3=IntVar()

    #adding and droping car window
    lab=Label(frame1,text="WELCOME TO CAR RENTAL SYSTEM").pack()

    lab1=Label(frame1,text="CARID").place(x=150,y=50)
    carid=Entry(frame1,textvariable=ent1)
    carid.place(x=200,y=50)

    lab2=Label(frame1,text="BRAND").place(x=150,y=80)
    brand=Entry(frame1,textvariable=ent2)
    brand.place(x=200,y=80)

    lab3=Label(frame1,text="RENT").place(x=150,y=110)
    price=Entry(frame1,textvariable=ent3)
    price.place(x=200,y=110)

    but1=Button(frame1,text="ADD CAR",command=addcar).place(x=200,y=200)
    but2=Button(frame1,text="DROP CAR",command=delcar).place(x=300,y=200)

    #butshow=Button(frame1,text="GO TO BOOK",command=show).place(x=250,y=400)
    # def frame2add():
    #displaying available cars
    labf=Label(frame2,text="AVAILABLE CARS").pack()

    treescroll=Frame(frame2)
    treescroll.pack()

    scroll=Scrollbar(frame2)
    scroll.pack(side=RIGHT,fill=Y)
    tree=ttk.Treeview(frame2,yscrollcommand=scroll.set) #yscrollcommand=scroll.set)
    scroll.config(command=tree.yview)

    #vsb=Scrollbar(root,orient="vertical")
    #vsb.configure(command=tree.yview)
    #tree.configure(yscrollcommand=vsb.set)
    #vsb.pack(fill=Y,side=RIGHT)

    tree['show']='headings'
    s=ttk.Style(root)
    s.theme_use("clam")
    tree.pack()

    tree['columns']=("car_id","brand","rent")
    cur=con.cursor()
    y='y'
    cur.execute("select car_id,brand,rent from cars where available='y'")
        #con.commit()
        #cur.close()
    tree.column("car_id",width=50,minwidth=50,anchor=CENTER)
    tree.column("brand",width=100,minwidth=100,anchor=CENTER)
    tree.column("rent",width=150,minwidth=150,anchor=CENTER)

        #headings
    tree.heading("car_id",text="carid",anchor=CENTER)
    tree.heading("brand",text="brand",anchor=CENTER)
    tree.heading("rent",text="rent",anchor=CENTER)

    i=0
    for row in cur:
        tree.insert('',i,text='',values=(row[0],row[1],row[2]))
        i+=1

    con.commit()

    #vsb=Scrollbar(root,orient="vertical")
    #vsb.configure(command=tree.yview)
    #tree.configure(yscrollcommand=vsb.set)
    #vsb.pack(fill=Y,side=RIGHT)

    ent4=IntVar()
    ent5=StringVar()
    ent6=StringVar()
    ent7=StringVar()
    ent8=StringVar()

    #function to book a car
    def bookcar():
        a=ent4.get()
        b=ent5.get()
        c=ent6.get()
        d=ent7.get()
        e=ent8.get()
        cur=con.cursor()
        cur.execute("insert into users(name,email,startdate,loc) values(%s,%s,%s,%s)",(b,c,d,e))
        con.commit()
        cur=con.cursor()
        cur.execute("select user_id from users where name=%s and email=%s",(b,c))
        ac=0
        for r in cur:
            ac=r[0]
        con.commit()
        cur=con.cursor()
        n='n'
        cur.execute("insert into manages(user_id,car_id) values(%s,%s)",(ac,a))
        x='n'
        cur.execute("update cars set available=%s where car_id=%s",(x,a))
        con.commit()
        #cur.execute("update manages set user_id = (select user_id from users natural join cars where name=%s and email=%s)",(b,c))
        #con.commit()
        #cur.execute("delete from users where user_id not in (select  user_id from manages)")
        #con.commit()
        #messagebox.showinfo("success","car booked")
        #cur.execute("delete from manages where manages.car_id=%s in (select car_id from cars where available='n')",(a))
        #con.commit()
        cur.execute("delete from manages where car_id not in (select car_id from cars)")
        con.commit()
        cur.execute("delete from users where user_id not in (select user_id from manages)")
        con.commit()
        messagebox.showinfo("success","car booked")
        carbook.delete(0,END)
        carname.delete(0,END)
        carmail.delete(0,END)
        cardate.delete(0,END)
        carloc.delete(0,END)


    #under development!!!
    def returncar():
        root1=Toplevel()
        root1.geometry("600x600")
        root1.title("RETURN CAR")
        lab=Label(root1,text="CARS TO BE RETURNED").pack()
        tree1=ttk.Treeview(root1)
        tree1["show"]="headings"
        s=ttk.Style(root1)
        s.theme_use("clam")
        tree1["columns"]=("carid","userid","name","email")
        tree1.column("carid",width=70,minwidth=70,anchor=CENTER)
        tree1.column("userid",width=70,minwidth=70,anchor=CENTER)
        tree1.column("name",width=150,minwidth=150,anchor=CENTER)
        tree1.column("email",width=150,minwidth=150,anchor=CENTER)

        tree1.heading("carid",text="carid",anchor=CENTER)
        tree1.heading("userid",text="userid",anchor=CENTER)
        tree1.heading("name",text="name",anchor=CENTER)
        tree1.heading("email",text="email",anchor=CENTER)

        cur=con.cursor()
        cur.execute("select car_id,user_id,name,email from manages natural join users natural join cars where available='n'")
        i=0
        for row in cur:
            tree1.insert('',i,text='',values=(row[0],row[1],row[2],row[3]))
            i+=1
        con.commit()

        
        def rccar():
            s1=bt1.get()
            s2=bt2.get()
            s3=bt3.get()
            cur=con.cursor()
            y='y'
            cur.execute("update cars set available=%s where car_id=%s",(y,s1))
            con.commit()
            cur.execute("delete from manages where car_id=%s and user_id=%s",(s1,s2))
            con.commit()
            messagebox.showinfo("car returned","thank u come again!")
            b1.delete(0,END)
            b2.delete(0,END)
            b3.delete(0,END)
            
        bt1=IntVar()
        bt2=IntVar()
        bt3=StringVar()
        
        
        
        l1=Label(root1,text="CARID").place(x=210,y=270)
        b1=Entry(root1,textvariable=bt1)
        b1.place(x=260,y=270)

        l2=Label(root1,text="USERID").place(x=210,y=300)
        b2=Entry(root1,textvariable=bt2)
        b2.place(x=260,y=300)
        
        l3=Label(root1,text="NAME").place(x=210,y=330)
        b3=Entry(root1,textvariable=bt3)
        b3.place(x=260,y=330)

        b4=Button(root1,text="RETURN CAR",command=rccar).place(x=250,y=370)

        vsb=ttk.Scrollbar(root1,orient="vertical")
        vsb.configure(command=tree1.yview)
        tree1.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side=RIGHT)
        
        
        tree1.pack()    
        root1.mainloop()



    lab4=Label(frame2,text="CARID").place(x=150,y=270)
    carbook=Entry(frame2,textvariable=ent4)
    carbook.place(x=200,y=270)

    lab5=Label(frame2,text="NAME").place(x=150,y=300)
    carname=Entry(frame2,textvariable=ent5)
    carname.place(x=200,y=300)

    lab6=Label(frame2,text="EMAIL").place(x=150,y=330)
    carmail=Entry(frame2,textvariable=ent6)
    carmail.place(x=200,y=330)

    lab7=Label(frame2,text="DATE").place(x=150,y=360)
    cardate=Entry(frame2,textvariable=ent7)
    cardate.place(x=200,y=360)

    lab8=Label(frame2,text="LOCATION").place(x=150,y=390)
    carloc=Entry(frame2,textvariable=ent8)
    carloc.place(x=220,y=390)

    but3=Button(frame2,text="BOOK CAR",command=bookcar).place(x=200,y=420)
    b10=Button(frame2,text="REFRESH",command=enter).place(x=290,y=420)

    la=Label(frame3,text="RETURN CAR PORTAL").place(x=190,y=10)
    but4=Button(frame3,text="GO TO RETURN CAR",command=returncar).place(x=200,y=100)


    #tree.pack()
    frame2.mainloop()
    root.mainloop()



def submit():
    c=0
    username=a.get()
    password=b.get()
    cur.execute("select *from admin")
    for i in cur:
        if i[0]==username and i[1]==password:
            global check
            c=1
            check=1
    if c==1:
        messagebox.showinfo("valid!","welcome!")
        enter()
    else:
        messagebox.showwarning("not valid!!","try again!")

    
r=Tk()
r.title("LOGIN CAR RENTAL SYSTEM")
r.geometry("500x500")
s=ttk.Style(r)
s.theme_use("clam")
cur=con.cursor()
a=StringVar()
b=StringVar()
t=Label(r,text="CAR RENTAL ADMIN LOGIN").pack()
user=Label(r,text="USERNAME").place(x=150,y=150)
g=Entry(r,textvariable=a)
g.place(x=220,y=150)
passw=Label(r,text="PASSWORD").place(x=150,y=180)
h=Entry(r,textvariable=b)
h.place(x=220,y=180)
bo=Button(r,text="SUBMIT",command=submit)
bo.place(x=250,y=220)
#b5=Button(r,text="REFRESH",command=enter)
#b5.place(x=250,y=250)
con.commit()
r.mainloop()