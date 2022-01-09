import pandas as pd
import mysql.connector as sql

con=sql.connect(host='localhost',user='root',passwd='abhay8055',database='railway')
if con.is_connected():
    print('successfully connected')


def menu():
    print()
    print("------------------")
    print("Railway managment system")

    print("1.create table passenger")
    print("2.add new pass")
    print("3.create table traindetails")
    print("4.add new in train detal")
    print("5.show from train")
    print("6.show all from pass")
    print("7.show pnr no.")
    print("8.reservation of ticket")
    print("9.cancellation of reservation")


menu()

def create_passengers():
    c1=con.cursor()
    c1.execute("CREATE TABLE if not exists `passengers` (pname varchar(30), age varchar(20), trainno varchar(30), noofpas varchar(25),cls varchar(25),destination varchar(30), amt varchar(20), status varchar(25),pnrno varchar(10))")
    print('table passengers created')

def add_passengers():
    c1=con.cursor()
    L=[]
    pname=input('Enter name:')
    L.append(pname)
    age=input('Enter age : ')
    L.append(age)
    trainno=input('Enter train no:')
    L.append(trainno)
    noofpas=input('Enter  no of passenger:')
    L.append(noofpas)
    cls=input("Enter class :")
    L.append(cls)
    destination=input("enter destination:")
    L.append(destination)
    amt=input("Enter fare:")
    L.append(amt)
    status=input("enter status:")
    L.append(status)
    pnrno=input("enter pnrno:")
    L.append(pnrno)
    pas=(L)
    sql="insert into passengers(pname,age,trainno,noofpas,cls,destination,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,pas)
    con.commit()
    print('Record of passenger inserted')
    df=pd.read_sql("select * from passengers",con)
    print(df)


def create_trainsdetail():
    c1=con.cursor()
    c1.execute('create table if not exists trainsdetail(tname varchar(30),tnum varchar(30),source varchar(30),destination varchar(30),fare varchar(30),ac1 varchar(25),ac2 varchar(25),slp varchar(30))')
    print('table trainsdetail created')


def add_traindetail():
    c1=con.cursor()
    df=pd.read_sql("select * from trainsdetail",con)
    print(df)
    L=[]
    tname=input('Enter train name:')
    L.append(tname)
    tnum=input('Enter train no : ')
    L.append(tnum)
    source=input('Enter source of train:')
    L.append(source)
    destination=input('Enter destination of train:')
    L.append(destination)
    fare=input("Enter fare :")
    L.append(fare)
    ac1=input("enter no of seatd for ac1:")
    L.append(ac1)
    ac2=input("Enter no of seat for ac2:")
    L.append(ac2)
    slp=input("enter no of seats for sleeper:")
    L.append(slp)
    f=(L)
    sql="insert into trainsdetail(tname,tnum,source,destination,fare,ac1,ac2,slp)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,f)
    con.commit()
    print('Record inserted in trains:')

def showtraindetail():
    print("ALL TRAIN DETAIL:")
    df=pd.read_sql("Select * from trainsdetail",con)
    print(df)


def showpassengers():
    print("all passengers detail")
    df=pd.read_sql("select * from passengers",con)
    print(df)

def disp_prnno():
    print("pnr status window")
    a=(input("enter train no : "))
    qry="select pname,status from passengers where trainno= %s;"%(a,)
    df=pd.read_sql(qry,con)
    print(df)

def ticketreservation():
    print("we have the foll")
    print("tname is 1 for goa express from new delhi:")
    print()
    print("1.first class ac rs 6000 per person")
    print("2.second class ac rs 5000 per person")
    print("3.third class ac rs 4000 per person")
    print("4.sleeper class ac rs 6000 per person")
    print()
    print("tname is 2 for jammu express from new delhi:")
    print()
    print("1.first class ac rs 10000 per person")
    print("2.second class ac rs 9000 per person")
    print("3.third class ac rs 8000 per person")
    print("4.sleeper class ac rs 7000 per person")

    tname=(input("enter your choice of train name please"))
    print(tname)
    x=int(input("enter your choice of ticket please"))
    n=int(input("how many ticket you need:"))

   
    if(x==1):
        print("you have chosen first class ac ticket")
        s=6000*n
    elif (x==2):
        print("you have chosen second class ac ticket")
        s=5000*n
    elif (x==3):
        print("you have chosen third class ac ticket")
        s=4000*n
    elif (x==4):
        print("you have chosen sleeper class ac ticket")
        s=3000*n
    else:
        print("invalid option")

        print("please choose a train")

    print("your total ticket price is = ",s,"\n")
    
   
    if(x==2):
        print("you have chosen first class ac ticket")
        s=10000*n
    elif (x==2):
        print("you have chosen second class ac ticket")
        s=9000*n
    elif (x==3):
        print("you have chosen third class ac ticket")
        s=8000*n
    elif (x==4):
        print("you have chosen sleeper class  ticket")
        s=7000*n
    else:
        print("invalid option")

        print("please choose a train")
    print("your total ticket price is =",s,"\n")

def cancel():
    print("before any changes in the status")
    df=pd.read_sql("select * from passengers",con)
    print(df)
    mc=con.cursor()
    mc.execute("update passengers set status='cancelled' where pnrno='G1003'")
    df=pd.read_sql("select * from passengers",con)
    print(df)

opt=""
opt=int(input("enter your choice: "))
if opt==1:
    create_passengers()
elif opt==2:
    add_passengers()
elif opt==3:
    create_trainsdetail()
elif opt==4:
    add_traindetail()
elif opt==5:
    showtraindetail()
elif opt==6:
    showpassengers()
elif opt==7:
    disp_prnno()
elif opt==8:
    ticketreservation()
elif opt==9:
    cancel()

else:
    print('invalid option')
