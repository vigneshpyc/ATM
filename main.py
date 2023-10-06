
from tkinter import*
from tkinter import messagebox as ms
import datetime as dt
import time
import random as r
root=Tk()
root.geometry("900x700")
root.title("ATM project")

#create a frame 1

f=Frame(root,width=700,height=600,highlightbackground="black",highlightthickness=2)
f.config(bg="gray")
f.pack(side=TOP)
date = dt.datetime.now()
format_date = f"{date:%a, %b %d %Y}"
w = Label(root, text=format_date, fg="black", bg="gray", font=("helvetica", 15)).place(x=330,y=15)

#creating pages

def withdraw_frame():

    time.sleep(3)
    wf=Frame(f,width=700,height=600,highlightbackground="black",highlightthickness=2)
    wf.config(bg="gray")
    wf.pack(side=TOP)

    show_info = Label(wf, text="!Dont Share Your Pin", font=("classic", 30), fg="red", bg="gray").place(x=150, y=30)
    a = StringVar()

    pa_lb=Label(wf,text="Enter your four digit pin",font=("classic",20,"bold"),fg="black",bg="gray").place(x=150,y=150)
    pa_entry=Entry(wf,show="x",textvariable=a,font=("classic",30,"bold")).place(x=100,y=200)
    crt_label1 = Label(wf, text="<< PRESS HERE IF CORRECT >>", font=("classic", 20, "bold"), fg="black",bg="gray").place(x=50, y=400)
    crt_label2= Label(wf, text="<< PRESS HERE IF INCORRECT >>", font=("classic", 20, "bold"), fg="black",bg="gray").place(x=50, y=500)
    def pin():

        if int(a.get())==1212:
            amt_fr=Frame(wf,width=700,height=600,highlightbackground="black",highlightthickness=2)
            amt_fr.config(bg="gray")
            amt_fr.pack(side=TOP)
            amt_label=Label(amt_fr,text="<<  Enter Your Amount  >>",font=("classic",30),fg="black",bg="gray").place(x=120,y=100)
            awarness_labe1 = Label(amt_fr, text="!your money", font=("classic", 20, "bold"), fg="cyan", bg="gray").place(x=10, y=50)
            awarness_labe2 = Label(amt_fr, text="!your responsibility", font=("classic", 20, "bold"), fg="cyan",bg="gray").place(x=400, y=50)
            crt_label3=Label(amt_fr,text="<< PRESS HERE IF CORRECT >>",font=("classic",20,"bold"),fg="black",bg="gray").place(x=50,y=400)
            crt_label4= Label(amt_fr, text="<< PRESS HERE IF INCORRECT >>", font=("classic", 20, "bold"), fg="black",bg="gray").place(x=50, y=500)
            b=IntVar()
            amt_entry=Entry(amt_fr,textvariable=b,font=("classic",30,"bold")).place(x=120,y=200)
            wamt_label = Label(amt_fr, text="!Please Wait Until Your Transaction is completed",font=("times", 20, "bold"), fg="black", bg="gray").place(x=70, y=300)


            def amt():
                if (b.get()) <= 5000:
                    tf=Frame(amt_fr,width=700,height=600,highlightbackground="black",highlightthickness=2)
                    tf.config(bg="gray")
                    tf.pack(side=TOP)
                    time.sleep(1)

                    time.sleep(10)
                    wamt_label1 = Label(tf, text="!Tranaction Completed\nThank You for Visiting MUVI  Bank of ATM",font=("times", 20, "bold"), fg="blue", bg="gray").place(x=100, y=200)

                else:
                    time.sleep(5)
                    invalid_label=Label(amt_fr,text="!sorry Not Enough Money in your Account       ",font=("times", 20, "bold"), fg="black", bg="gray").place(x=100, y=300)


            def cancel1():
                exit(amt)

            confirm_btn = Button(amt_fr, text="CONFIRM", font=("classic", 15, "bold"), fg="white", bg="blue",command=amt).place(x=550, y=400)
            cancel_btn = Button(amt_fr, text="CANCEL  ", font=("classic", 15, "bold"), fg="white", bg="blue",command=cancel1).place(x=550, y=500)


        else:
            ms.askretrycancel("atm info","incorrect password")


    def cancel():
       exit(pin)
    confirm_btn = Button(wf, text="CONFIRM", font=("classic", 15, "bold"), fg="white", bg="blue",command=pin).place(x=550, y=400)
    cancel_btn = Button(wf, text="CANCEL  ", font=("classic", 15, "bold"), fg="white", bg="blue",command=cancel).place(x=550, y=500)

def generate_otp():
    otp_frame= Frame(f, width=700, height=600, highlightbackground="black", highlightthickness=2)
    otp_frame.config(bg="gray")
    otp_frame.pack(side=TOP)
    date = dt.datetime.now()
    format_date = f"{date:%a, %b %d %Y}"
    ap=StringVar()
    w = Label(root, text=format_date, fg="black", bg="gray", font=("helvetica", 15)).place(x=330, y=15)
    pa_lb = Label(otp_frame, text="<<Enter your Account Number>>", font=("classic", 20, "bold"), fg="black", bg="gray").place(x=100, y=150)
    pa_entry = Entry(otp_frame,textvariable=ap, font=("classic", 30, "bold")).place(x=100, y=200)
    crt_label3 = Label(otp_frame, text="<< PRESS HERE IF CORRECT >>", font=("classic", 20, "bold"), fg="black",bg="gray").place(x=50, y=400)
    crt_label4 = Label(otp_frame, text="<< PRESS HERE IF INCORRECT >>", font=("classic", 20, "bold"), fg="black",bg="gray").place(x=50, y=500)
    confirm_btn = Button(otp_frame, text="CONFIRM", font=("classic", 15, "bold"), fg="white", bg="blue").place(x=550,y=400)
    cancel_btn = Button(otp_frame, text="CANCEL  ", font=("classic", 15, "bold"), fg="white", bg="blue").place(x=550,y=500)


    a="1234567890"
    b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c=a+b
    len=16
    d="".join(r.sample(c,len))
    acc_no=Label(otp_frame,text="acc_no:"+d,font=("classic",10,"bold"),fg="black",bg="gray").place(x=20,y=100)
    def accno():
        if (ap.get()) == acc_no:
            l=Label(otp_frame,text="correct",font=("times",15,"bold"),fg="black").place(x=40,y=100)
        else:
            ms.askretrycancel("bank infor","incorrect account number")
    confirm_btn = Button(otp_frame, text="CONFIRM", font=("classic", 15, "bold"), fg="white", bg="blue",command=accno).place(x=550, y=400)
    cancel_btn = Button(otp_frame, text="CANCEL  ", font=("classic", 15, "bold"), fg="white", bg="blue").place(x=550, y=500)



#labe a bank name and other details

bank_name=Label(f,text="MUVI",font=("times",40,"bold"),fg="blue",bg="gray",highlightcolor="black").place(x=250,y=100)
bank_add=Label(f,text="Bank of INDIA",font=("classic",10,"bold"),fg="black",bg="gray").place(x=270,y=170)
secure_label=Label(f,text="!Be safe",font=("classic",20,"bold"),fg="black",bg="gray").place(x=0,y=10)
secure_label2=Label(f,text="!!Be Happy",font=("classic",20,"bold"),fg="black",bg="gray").place(x=500,y=15)
wel_label=Label(f,text="Welcome to MUVI bank of india ATM",font=("classic",15,"bold"),fg="black",bg="gray").place(x=180,y=210)

#creating button
withdraw_btn=Button(f,text="WITHDRAW",font=("classic",15,"bold"),fg="white",bg="blue",command=withdraw_frame).place(x=550,y=300)
deposit_btn=Button(f,text="DEPOSIT",font=("classic",15,"bold"),fg="white",bg="blue").place(x=570,y=400)
acc_btn=Button(f,text="ACCOUNT DETAILS",font=("classic",15,"bold"),fg="white",bg="blue").place(x=480,y=500)
otp_btn=Button(f,text="GENERATE OTP",font=("classic",15,"bold"),fg="white",bg="blue",command=generate_otp).place(x=10,y=350)
password_btn=Button(f,text="CHANGE PASSWORD",font=("classic",15,"bold"),fg="white",bg="blue").place(x=10,y=450)
root.mainloop()