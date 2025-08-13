import mysql.connector
import csv
import random
from tabulate import tabulate
from datetime import timedelta, date
import tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
con=mysql.connector.connect(host='localhost',
                            password='Ryuzaki@2104',   
                            user='root',
                            database='FinalvaxDBMS')
#cur=con.cursor()
#query="Create table Doseonex(Token char(10),Name char(20),Address char(20),Gender char(10),Age int,Mobile int,DOB char(10),Dose1 char(10),Dose2 char(10),Vaccine char(11),Price int)"
#cur.execute(query)
#con.commit()

#query="Create table employee(Name char(20),Password char(8))"
#cur.execute(query)
#con.commit()

def display():
    def new_rec():
        root1=tkinter.Tk()
        root1.title("NEW RECORD")
        root1.maxsize(width=600,height=400)
        root1.minsize(width=600,height=400)
        lbx2=tkinter.Label(root1,text="NAME")
        lbx2.place(x=30,y=40)
        lbx3=tkinter.Label(root1,text="ADDRESS")
        lbx3.place(x=30,y=70)
        lbx4=tkinter.Label(root1,text="GENDER")
        lbx4.place(x=30,y=100)
        lbx5=tkinter.Label(root1,text="AGE")
        lbx5.place(x=30,y=130)
        lbx6=tkinter.Label(root1,text="MOBILE NO.")
        lbx6.place(x=30,y=160)
        lbx7=tkinter.Label(root1,text="ENTER DOB IN FORMAT")
        lbx7.place(x=30,y=190)
        lbx8=tkinter.Label(root1,text="ENTER DOSE 1 DATE")
        lbx8.place(x=30,y=220)
        lbx9=tkinter.Label(root1,text="ENTER VACCINE")
        lbx9.place(x=30,y=250)
        lbx10=tkinter.Label(root1,text="ENTER PRICE")
        lbx10.place(x=30,y=280)

        def onlynum(char):
            return char.isdigit()

        def onlychar(char):
            return char.isalpha()

    
        validation1=root1.register(onlychar)
        validation=root1.register(onlynum)
    
    
        ent2=tkinter.Entry(root1,validate="key",validatecommand=(validation1,'%S'),bd=5)
        ent2.place(x=300,y=40)
    
        ent3=tkinter.Entry(root1,bd=5)
        ent3.place(x=300,y=70)
    
        values1=['Male','Female','Others']
        ent4=ttk.Combobox(root1,values=values1)
        ent4.place(x=300,y=100)
    
    

        ent5=tkinter.Entry(root1,validate="key",validatecommand=(validation,'%S'),bd=5)
        ent5.place(x=300,y=130)
    
    
        ent6=tkinter.Entry(root1,validate="key",validatecommand=(validation,'%S'),bd=5)
        ent6.place(x=300,y=160)
        num=len(ent6.get())
        if num>10:
            messagebox.showerror('showerror','Invalid number')
        else:
            pass
        
    
        ent7=DateEntry(root1)
        ent7.place(x=300,y=190)
   
    
    
        ent8=DateEntry(root1)
        ent8.place(x=300,y=220)
    
    
        values2=['Covishield','Covaxin','Other (mention)']
        ent10=ttk.Combobox(root1,values=values2)
        ent10.place(x=300,y=250)

        ent11=tkinter.Entry(root1,validate="key",validatecommand=(validation,'%S'),bd=5)
        ent11.place(x=300,y=280)


        def delette():
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            ent6.delete(0,END)
            ent7.delete(0,END)
            ent8.delete(0,END)
            ent10.delete(0,END)
            ent11.delete(0,END)
        
        def getx():
            uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            digits='0123456789'
            lower='abcdefghijklmnopqrstuvwxyz'
            upper,nums,low=True,True,True
            allis=""
            if upper:
                allis+=uppercase
            if nums:
                allis+=digits
            if low:
                allis+=lower
            length=5
            for x in range(1):
                token="".join(random.sample(allis,length))
            Token=token
            text2=ent2.get()
            text3=ent3.get()
            text4=ent4.get()
            text5=ent5.get()
            text6=ent6.get()
            text8=ent8.get()
            text10=ent10.get()
            text11=ent11.get()
            text7=ent7.get()
            bod=str(text7)
            monx=bod[0:1]
            dayx=bod[2:4]
            yearx=bod[5:]
            bod1x=str(yearx) + "-" + str(monx) + "-" + str(dayx)
            zzx=str(bod1x)



        
        #MM/DD/YY
            vac=str(ent8.get())
            month=vac[0:1]
            day=vac[2:4]
            year=vac[5:]
            vac1=date(int(year),int(month),int(day))
            vac1x=str(year) + "-" + str(month) + "-" + str(day)
            vac2=vac1+ timedelta(days=42)
            a=str(vac2)
            zz=a[2:]
            query="insert into Doseonex values('%s','%s', '%s','%s', %s, %s, '%s', '%s', '%s', '%s',%s)"%(Token,text2,text3,text4,int(text5),int(text6),zzx,vac1x,zz,text10,int(text11))
            cur.execute(query)
            con.commit()
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            ent6.delete(0,END)
            ent7.delete(0,END)
            ent8.delete(0,END)
            ent10.delete(0,END)
            ent11.delete(0,END)
            messagebox.showinfo("showinfo","Record entered")

        
        btn=tkinter.Button(root1,text='Submit',command=getx)
        btn.place(x=30,y=350)
        btnx=tkinter.Button(root1,text='Clear',command=delette)
        btnx.place(x=100,y=350)
    
        root1.mainloop()
    
    def update():
        root2=tkinter.Tk()
        root2.title("UPDATE")
        root2.maxsize(width=800,height=700)
        root2.minsize(width=800,height=700)
        l=tkinter.Label(root2,text="UPDATE THE FIELDS AS REQUIRED")
        l.place(x=75,y=10)
        l1=tkinter.Label(root2,text="(ENTER ALPHABETICAL DATA IN DOUBLE QUOTES)",bg='red')
        l1.place(x=300,y=10)
        lbox=tkinter.Label(root2,text="ENTER OLD TOKEN NUMBER")
        lbox.place(x=30,y=50)
        lbx1=tkinter.Label(root2,text="TOKEN")
        lbx1.place(x=30,y=100)
        lbx2=tkinter.Label(root2,text="NAME")
        lbx2.place(x=30,y=150)
        lbx3=tkinter.Label(root2,text="ADDRESS")
        lbx3.place(x=30,y=200)
        lbx4=tkinter.Label(root2,text="GENDER")
        lbx4.place(x=30,y=250)
        lbx5=tkinter.Label(root2,text="AGE")
        lbx5.place(x=30,y=300)
        lbx6=tkinter.Label(root2,text="MOBILE NO.")
        lbx6.place(x=30,y=350)
        lbx7=tkinter.Label(root2,text="ENTER DOB IN FORMAT (YY-MM-DD)")
        lbx7.place(x=30,y=400)
        lbx8=tkinter.Label(root2,text="ENTER DOSE 1 DATE (YY-MM-DD)")
        lbx8.place(x=30,y=450)
        lbx9=tkinter.Label(root2,text="ENTER DOSE 2 DATE (YY-MM-DD)")
        lbx9.place(x=30,y=500)
        lbx10=tkinter.Label(root2,text="ENTER VACCINE")
        lbx10.place(x=30,y=550)
        lbx11=tkinter.Label(root2,text="ENTER PRICE")
        lbx11.place(x=30,y=600)

        def onlynum(char):
            return char.isdigit()

        def onlychar(char):
            return char.isalpha()

        validation1=root2.register(onlychar)
        validation=root2.register(onlynum)

        ento=tkinter.Entry(root2,bd=5)
        ento.place(x=300,y=50)
   
        ent1=tkinter.Entry(root2,bd=5)
        ent1.place(x=300,y=100)
    
        ent2=tkinter.Entry(root2,validate="key",validatecommand=(validation1,'%S'),bd=5)
        ent2.place(x=300,y=150)
    
        ent3=tkinter.Entry(root2,bd=5)
        ent3.place(x=300,y=200)

        values1=['Male','Female','Others']
        ent4=ttk.Combobox(root2,values=values1)
        ent4.place(x=300,y=250)
    
        ent5=tkinter.Entry(root2,validate="key",validatecommand=(validation,'%S'),bd=5)
        ent5.place(x=300,y=300)
    
        ent6=tkinter.Entry(root2,validate="key",validatecommand=(validation,'%S'),bd=5)
        ent6.place(x=300,y=350)
    
        ent7=tkinter.Entry(root2,bd=5)
        ent7.place(x=300,y=400)
    
        ent8=tkinter.Entry(root2,bd=5)
        ent8.place(x=300,y=450)

        ent9=tkinter.Entry(root2,bd=5)
        ent9.place(x=300,y=500)

        values2=['Covishield','Covaxin','Other (mention)']
        ent10=ttk.Combobox(root2,values=values2)
        ent10.place(x=300,y=550)

        ent11=tkinter.Entry(root2,validate="key",validatecommand=(validation,'%S'),bd=5)
        ent11.place(x=300,y=600)


        def cleartoup():
            ento.delete(0,END)

        def toup():
            oldt=ento.get()
            newt=ent1.get()
            query="update Doseonex set Token={} where Token={}".format(newt,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ento.delete(0,END)
            ent1.delete(0,END)
        
        def clear1():
            ent1.delete(0,END)


        def naup():
            oldt=ento.get()
            nam=ent2.get()
            query="update Doseonex set Name={} where Token={}".format(nam,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent2.delete(0,END)
        
        def clear2():
            ent2.delete(0,END)


        def adup():
            oldt=ento.get()
            adt=ent3.get()
            query="UPDATE Doseonex SET Address={} WHERE Token={}".format(adt,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent3.delete(0,END)
    
        
        def clear3():
            ent3.delete(0,END)



        def genup():
            oldt=ento.get()
            gent=ent4.get()
            query="UPDATE Doseonex SET Gender={} WHERE Token={}".format(gent,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent4.delete(0,END)
        
        def clear4():
            ent4.delete(0,END)
        

        def ageup():
            oldt=ento.get()
            aget=ent5.get()
            query="UPDATE Doseonex SET Age={} WHERE Token={}".format(aget,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent5.delete(0,END)
        
        def clear5():
            ent5.delete(0,END)



        def mobup():
            oldt=ento.get()
            mobt=ent6.get()
            query="UPDATE Doseonex SET Mobile={} WHERE Token={}".format(mobt,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent6.delete(0,END)
        
        def clear6():
            ent6.delete(0,END)



        def dobup():
            oldt=str(ento.get())
            dobt=ent7.get()
            query="UPDATE Doseonex SET DOB={} WHERE Token={}".format(dobt,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent7.delete(0,END)
        
        def clear7():
            ent7.delete(0,END)



        def dos1():
            oldt=str(ento.get())
            dos1t=ent8.get()
            query="UPDATE Doseonex SET Dose1={} WHERE Token={}".format(dos1t,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent8.delete(0,END)
        
        def clear8():
            ent8.delete(0,END)



        def dos2():
            oldt=str(ento.get())
            dos2t=ent9.get()
            query="UPDATE Doseonex SET Dose2={} WHERE Token={}".format(dos2t,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent9.delete(0,END)
        
        def clear9():
            ent9.delete(0,END)




        def vaxup():
            oldt=ento.get()
            vaxt=ent10.get()
            query="UPDATE Doseonex SET Vaccine={} WHERE Token={}".format(vaxt,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent10.delete(0,END)
        
        def clear10():
            ent1.delete(0,END)




        def priup():
            oldt=ento.get()
            prit=ent11.get()
            query="UPDATE Doseonex SET Price={} WHERE Token={}".format(prit,oldt)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","UPDATED")
            ent11.delete(0,END)
        
        def clear11():
            ent11.delete(0,END)

        

        btnxo=tkinter.Button(root2,text='CLEAR',command=cleartoup)
        btnxo.place(x=580,y=50)
        btnx1=tkinter.Button(root2,text='UPDATE',command=toup)
        btnx1.place(x=500,y=100)
        btcl1=tkinter.Button(root2,text='CLEAR',command=clear1)
        btcl1.place(x=580,y=100)
    
    
        btnx2=tkinter.Button(root2,text='UPDATE',command=naup)
        btnx2.place(x=500,y=150)
        btcl2=tkinter.Button(root2,text='CLEAR',command=clear2)
        btcl2.place(x=580,y=150)
    
    
        btnx3=tkinter.Button(root2,text='UPDATE',command=adup)
        btnx3.place(x=500,y=200)
        btcl3=tkinter.Button(root2,text='CLEAR',command=clear3)
        btcl3.place(x=580,y=200)
    
    
        btnx4=tkinter.Button(root2,text='UPDATE',command=genup)
        btnx4.place(x=500,y=250)
        btcl4=tkinter.Button(root2,text='CLEAR',command=clear4)
        btcl4.place(x=580,y=250)
    
    
        btnx5=tkinter.Button(root2,text='UPDATE',command=ageup)
        btnx5.place(x=500,y=300)
        btcl5=tkinter.Button(root2,text='CLEAR',command=clear5)
        btcl5.place(x=580,y=300)
    
    
        btnx6=tkinter.Button(root2,text='UPDATE',command=mobup)
        btnx6.place(x=500,y=350)
        btcl6=tkinter.Button(root2,text='CLEAR',command=clear6)
        btcl6.place(x=580,y=350)
    
    
        btnx7=tkinter.Button(root2,text='UPDATE',command=dobup)
        btnx7.place(x=500,y=400)
        btcl7=tkinter.Button(root2,text='CLEAR',command=clear7)
        btcl7.place(x=580,y=400)
    
    
        btnx8=tkinter.Button(root2,text='UPDATE',command=dos1)
        btnx8.place(x=500,y=450)
        btcl8=tkinter.Button(root2,text='CLEAR',command=clear8)
        btcl8.place(x=580,y=450)
    
    
        btnx9=tkinter.Button(root2,text='UPDATE',command=dos2)
        btnx9.place(x=500,y=500)
        btcl9=tkinter.Button(root2,text='CLEAR',command=clear9)
        btcl9.place(x=580,y=500)


        btnx10=tkinter.Button(root2,text='UPDATE',command=vaxup)
        btnx10.place(x=500,y=550)
        btcl10=tkinter.Button(root2,text='CLEAR',command=clear10)
        btcl10.place(x=580,y=550)


        btnx11=tkinter.Button(root2,text='UPDATE',command=priup)
        btnx11.place(x=500,y=600)
        btcl11=tkinter.Button(root2,text='CLEAR',command=clear11)
        btcl11.place(x=580,y=600)


        root2.mainloop()

    def DEL_REC():
        root3=tkinter.Tk()
        root3.title("DELETE")
        root3.maxsize(width=650,height=300)
        root3.minsize(width=650,height=300)
        lup=tkinter.Label(root3,text="ON THE BASIS OF TOKEN NUMBER THE RECORD WILL BE DELETED. Enter token in double quotes",fg='green')
        lup.place(x=10,y=20)
        lbe=tkinter.Label(root3,text="ENTER THE TOKEN")
        lbe.place(x=10,y=80)

        entt=tkinter.Entry(root3,bd=5)
        entt.place(x=150,y=80)

        def compdel():
            tox=entt.get()
            query="Delete from Doseonex where Token={}".format(tox)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("showinfo","Record Deleted !")
            entt.delete(0,END)
        def clearxt():
            entt.delete(0,END)

    
        btndx=tkinter.Button(root3,text='CLEAR',command=clearxt)
        btndx.place(x=350,y=80)
        btnd=tkinter.Button(root3,text='DELETE',command=compdel)
        btnd.place(x=150,y=150)

    
        root3.mainloop()

    def moreopt():
        root4=tkinter.Tk()
        root4.title("MORE OPTIONS")
        root4.maxsize(width=900,height=1000)
        root4.minsize(width=900,height=600)

        def myfunc():
            cur.execute("Select SUM(Price) from Doseonex")
            a=cur.fetchall()
            z=a[0][0]
            empl1=tkinter.Label(root4,text=("The sum is",z),fg='green')
            empl1.place(x=200,y=50)

        def myfunc1():
            cur.execute("Select count(Gender) from Doseonex WHERE Gender='F'")
            a=cur.fetchall()
            z=a[0][0]
            empl1=tkinter.Label(root4,text=("Total number of Female",z),fg='green')
            empl1.place(x=230,y=100)

        def myfunc2():
            cur.execute("Select count(Gender) from Doseonex WHERE Gender='M'")
            a=cur.fetchall()
            z=a[0][0]
            empl1=tkinter.Label(root4,text=("Total number of male",z),fg='green')
            empl1.place(x=200,y=150)

        def myfunc3():
            cur.execute("Select count(Gender) from Doseonex")
            a=cur.fetchall()
            z=a[0][0]
            empl1=tkinter.Label(root4,text=("Total number of vaccinated people",z),fg='green')
            empl1.place(x=300,y=200)

        def myfunc4():
            cur.execute("Select count(Age) from Doseonex WHERE Age>=18 OR Age<45")
            a=cur.fetchall()
            z=a[0][0]
            empl1=tkinter.Label(root4,text=("Total number of people above age 18",z),fg='green')
            empl1.place(x=300,y=250)

        def myfunc5():
            cur.execute("Select count(Age) from Doseonex WHERE Age>=45")
            a=cur.fetchall()
            z=a[0][0]
            empl1=tkinter.Label(root4,text=("People above age 45",z),fg='green')
            empl1.place(x=300,y=300)

        def myfunc6():
            cur.execute("Select count(Vaccine) from Doseonex WHERE Vaccine='Covishield'")
            a=cur.fetchall()
            z=a[0][0]
            empl1=tkinter.Label(root4,text=("Total dose of covishield",z),fg='green')
            empl1.place(x=300,y=350)

        def myfunc7():
            cur.execute("Select count(Vaccine) from Doseonex WHERE Vaccine='Covaxin'")
            a=cur.fetchall()
            z=a[0][0]
            empl1=tkinter.Label(root4,text=("Total dose of covaxin",z),fg='green')
            empl1.place(x=300,y=400)
    

    
        btn1=tkinter.Button(root4,text='SUM ',command=myfunc)
        btn1.place(x=100,y=50)
        btn2=tkinter.Button(root4,text='COUNT FEMALE',command=myfunc1)
        btn2.place(x=100,y=100)
        btn3=tkinter.Button(root4,text='COUNT MALE',command=myfunc2)
        btn3.place(x=100,y=150)
        btn4=tkinter.Button(root4,text='TOTAL VACCINATED PEOPLE',command=myfunc3)
        btn4.place(x=100,y=200)
        btn5=tkinter.Button(root4,text='PPL GREATER THAN AGE 18',command=myfunc4)
        btn5.place(x=100,y=250)
        btn6=tkinter.Button(root4,text='PPL LESS THAN AGE 45',command=myfunc5)
        btn6.place(x=100,y=300)
        btn7=tkinter.Button(root4,text='TOTAL DOSE OF COVISHIELD',command=myfunc6)
        btn7.place(x=100,y=350)
        btn8=tkinter.Button(root4,text='TOTAL DOSE OF COVAXIN',command=myfunc7)
        btn8.place(x=100,y=400)
        btns1=tkinter.Button(root4,text='CLICK ME TO EXIT !',command=root4.destroy)
        btns1.place(x=450,y=450)

        root4.mainloop()
    




    root=tkinter.Tk()
    root.title("VACCINATION DATABASE")
    root.maxsize(width=900,height=600)
    root.minsize(width=900,height=600)
    file=tkinter.PhotoImage(file="headingf.gif")
    label=tkinter.Label(root,image=file)
    label.place(x=0,y=0)
    filex=tkinter.PhotoImage(file="sts1.gif")
    labelx=tkinter.Label(root,image=filex)
    labelx.place(x=0,y=250)
#file2x=tkinter.PhotoImage(file="tube1.gif")
#labe2x=tkinter.Label(root,image=file2x)
#labe2x.place(x=0,y=500)

    btn1=tkinter.Button(root,text='ENTER NEW RECORD',command=new_rec)
    btn1.place(x=50,y=200)
    btn2=tkinter.Button(root,text='UPDATE RECORD',command=update)
    btn2.place(x=250,y=200)
    btn3=tkinter.Button(root,text='DELETE A RECORD',command=DEL_REC)
    btn3.place(x=430,y=200)
    btn4=tkinter.Button(root,text='MORE OPTIONS',command=moreopt)
    btn4.place(x=620,y=200)



    root.mainloop()


display()





