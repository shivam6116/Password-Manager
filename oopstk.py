from tkinter import *
import tkinter.messagebox as tmsg
import  random
import sys
import datetime
from tkinter import ttk
import re
import pyttsx3

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class Manager(Tk):
    def __init__(self):
        super().__init__()

    pd=""
    n=[]
    count = 0
    ln = ["0","1","2","3","4","5","6","7","8","9"]
    la = ["A", "B", "C", "D", "E", 'F', 'G', 'H', 'I',
         'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ls= ['@', '#', '$',"/","!","%","*"]
    lsa=['a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def Window1(self):
        root=Toplevel()
        root.geometry("800x555")
        root.title("New Password")
        self.speaking('New Password Window Is opening')

        label6 = ttk.Label(root, image=pic1).grid(row=0, column=0, rowspan=15, columnspan=10)
        Label(root,text="Name",font=" arieal 13 bold").grid(row=1,column=4)
        Label(root, text="Phone Number",font=" arieal 13 bold").grid(row=2, column=4)
        Label(root, text="Email",font=" arieal 13 bold").grid(row=3, column=4,ipadx=10)

        Entry(root, textvariable=namev,font=" arieal 13 ").grid(row=1, column=5,sticky=E)
        Entry(root, textvariable=roll,font=" arieal 13 ").grid(row=2, column=5,sticky=E)
        Entry(root, textvariable=email,font=" arieal 13 bold").grid(row=3, column=5,sticky=E)
        namev.set("")

        roll.set("")
        email.set("")
        password.set("")
        pin.set("")
        che1.set(0)
        che2.set(0)
        che3.set(0)
        che4.set(0)

        Label(root,text="Password Choice...",font="lucida 15 bold",fg='red').grid(row=1,column=0)

        Radiobutton(root,text="Random Password",padx=14,variable=radio1,value=1,background='Yellow',foreground='red',font=" arieal 17 bold").grid(sticky=W,row=2,column=0)
        Radiobutton(root,text="you want to enter",padx=14,variable=radio1,value=2,background='yellow',foreground='red',font=" arieal 17 bold").grid(sticky=W,row=3,column=0)

        Checkbutton(root, text="Numeric ", variable=che1,bd=4,font=" arieal 15 bold").grid(row=6, column=0,sticky=W)
        Checkbutton(root, text="Upper case",variable=che2,font=" arieal 15 bold").grid(row=7, column=0,sticky=W)
        Checkbutton(root, text="Lower case",variable=che3,font=" arieal 15 bold").grid(row=8, column=0,sticky=W)
        Checkbutton(root, text="Special Character",variable=che4,font=" arieal 15 bold").grid(row=9, column=0,sticky=W)

        Button(root,text="Save", command=self.saving,font=" arieal 15 bold").grid(row=13, column=5)
        Button(root, text="Generate", command=self.create,font=" arieal 15 bold").grid(row=13, column=4)
        Button(root,text="Strength", command=self.strength,font=" arieal 15 bold").grid(row=13, column=3)

        Label(root, text="",textvariable=text, font="calibre 15 bold",fg='orange').grid(row=12, column=0)
        Label(root, text="Password should \n contain...",font="lucida 15 bold",fg='red').grid(row=5, column=0)

        Label(root, text="Password",font=" arieal 13 bold").grid(row=11, column=4)
        Label(root, text="Verification pin",font=" arieal 13 bold").grid(row=12, column=4)
        Entry(root, textvariable=password,font=" arieal 10 ").grid(row=11, column=5)
        Entry(root, textvariable=pin,font=" arieal 10").grid(row=12, column=5)

        root.mainloop()



    def Window2(self):
        root1=Toplevel()
        root1.geometry("666x444")
        root1.title("Save your Password")
        self.speaking('New save Window Is opening')
        namev.set("")
        roll.set("")
        email.set("")
        password.set("")
        pin.set("")
        label2 = ttk.Label(root1, image=pic5).grid(row=0, column=0, rowspan=13, columnspan=10)

        Label(root1, text="User Name",font=" arieal 15 bold").grid(row=2, column=0,ipadx=16,ipady=6)
        Label(root1, text="Phone Number",font=" arieal 15 bold").grid(row=3, column=0,ipadx=6,ipady=6)
        Label(root1, text="Email ID",font=" arieal 15 bold").grid(row=4, column=0,ipadx=16,ipady=6)
        Label(root1, text="Password",font=" arieal 15 bold").grid(row=5, column=0,ipadx=16,ipady=6)
        Label(root1, text="Your Pin",font=" arieal 15 bold").grid(row=6, column=0,ipadx=16,ipady=6)

        Entry(root1, textvariable=namev,font=" arieal 15 ").grid(row=2, column=1,ipady=3)
        Entry(root1, textvariable=roll,font=" arieal 15 ").grid(row=3, column=1,ipady=3)
        Entry(root1, textvariable=email,font=" arieal 15 ").grid(row=4, column=1,ipady=3)
        Entry(root1, textvariable=password,show="*",font=" arieal 15 ").grid(row=5, column=1,ipady=3)
        Entry(root1, textvariable=pin,font=" arieal 15 ").grid(row=6, column=1)

        Button(root1,text="Save The Data", command=self.saving,font=" arieal 12 bold").grid(row=6, column=5,ipadx=6,ipady=3)
        Button(root1,text="Generate Pin", command=self.randompin,font=" arieal 12 bold").grid(row=5, column=5,ipadx=6,ipady=3)

        root1.mainloop()

    def Resetwindow(self):
        root3 = Toplevel()
        root3.geometry("444x222")
        root3.title("RESET")
        self.speaking('Reset Window Is opening')
        lab = ttk.Label(root3, image=pic4).grid(row=0, column=0, rowspan=10, columnspan=10)

        Label(root3, text="Name",font=" arieal 15 bold").grid(row=1, column=0,ipadx=2,ipady=3)
        Label(root3, text="PIN",font=" arieal 15 bold").grid(sticky=W,row=2, column=0,ipadx=8,ipady=3)

        namev.set("")
        pin.set("")
        Entry(root3, textvariable=namev,font=" arieal 15 ",bg='yellow').grid(row=1, column=1)
        Entry(root3, textvariable=pin, show="*",font=" arieal 15 ",bg='yellow').grid(row=2, column=1)

        Button(root3, text="  Reset  ",command=self.reset,font=" arieal 13 bold").grid(row=7, column=1,ipadx=5,ipady=3)
        Button(root3, text="  Next  ",command=self.Window1,font=" arieal 13 bold").grid(row=7, column=3,ipadx=2,ipady=3)

    def gamewindow(self):
        root2 = Toplevel()
        root2.geometry("555x370")
        root2.title("GAME")
        self.speaking('Game Window Is opening')
        label9 = ttk.Label(root2, image=pic6).grid(row=0, column=0, rowspan=12, columnspan=15)
        Radiobutton(root2,bg='pink', text="Are You Challanging\n me", padx=14, variable=radio1, value=1,font=" lucida 10 bold").grid(
            row=2, column=2,columnspan=2,sticky=W,ipadx=5)
        radio1.set(0)
        Label(root2, font="lucida 12 bold",fg='red',text="Remember!.. You will get only \n7 chances... ").grid(
            columnspan=3,row=1, column=3,ipadx=3,ipady=2)
        Label(root2, text="Name",font=" arieal 15 bold",bg='Yellow',bd=5).grid(row=3, column=3)
        Label(root2, text="Our Password",font=" arieal 15 bold",bg='yellow').grid(row=4, column=3)
        Entry(root2, textvariable=namev,font=" arieal 15 bold").grid(sticky=E,row=3, column=4)
        Entry(root2, textvariable=password, show="*",font=" arieal 15 bold").grid(sticky=E,row=4, column=4)

        che2.set(0)
        che3.set(0)
        che4.set(0)
        che1.set(0)
        namev.set("")
        roll.set("")
        email.set("")
        password.set("")
        pin.set("")
        Checkbutton(root2, text="Numeric ", variable=che1,bg='red').grid(row=8, column=2)
        Checkbutton(root2, text="Upper case", variable=che2,bg='red').grid(row=8, column=3)
        Checkbutton(root2, text="Lower case", variable=che3,bg='red').grid(row=8, column=4)
        Checkbutton(root2, text="Special Character", variable=che4,bg='red').grid(row=8, column=5)

        Button(root2, text="Start", command=self.create,font=" arieal 10 bold").grid(row=10, column=3)
        Button(root2, text="Guess", command=self.guess,font=" arieal 10 bold").grid(row=10, column=4)

        root2.mainloop()

    def create(self):
        self.pd=""
        if radio1.get()==1:
            pin1=""
            length=8
            self.n=self.checkbox()
            for i in range(0, length) :
                a=random.choice(self.n)
                self.pd=self.pd+a
            password.set(self.pd)
            for i in range(0, 4) :
                b=random.choice(self.ln)
                pin1=pin1+b
            pin.set(int(pin1))
            self.speaking('Random Password Is Generated.')
        elif radio1.get()==2:
            text1="Please Enter your Password"
            text.set(text1)
        else:
            text1 = "Firstly select option"
            text.set(text1)

    def checkbox(self):
        if che1.get() == 1 and che2.get() == 0 and che3.get() == 0 and che4.get() == 0:
            self.n = self.ln
        elif che1.get() == 0 and che2.get() == 1 and che3.get() == 0 and che4.get() == 0:
            self.n = self.la
        elif che1.get() == 0 and che2.get() == 0 and che3.get() == 1 and che4.get() == 0:
            self.n = self.la
        elif che1.get() == 0 and che2.get() == 0 and che3.get() == 0 and che4.get() == 1:
            self.n = self.lsa
        elif che1.get() == 1 and che2.get() == 1 and che3.get() == 0 and che4.get() == 0:
            self.n = self.ln + self.la
        elif che1.get() == 1 and che2.get() == 0 and che3.get() == 1 and che4.get() == 0:
            self.n = self.ln + self.ls
        elif che1.get() == 1 and che2.get() == 0 and che3.get() == 0 and che4.get() == 1:
            self.n = self.ln + self.lsa
        elif che1.get() == 0 and che2.get() == 1 and che3.get() == 1 and che4.get() == 0:
            self.n = self.la + self.ls
        elif che1.get() == 0 and che2.get() == 1 and che3.get() == 0 and che4.get() == 1:
            self.n = self.la + self.lsa
        elif che1.get() == 0 and che2.get() == 0 and che3.get() == 1 and che4.get() == 1:
            self.n = self.ls + self.lsa
        else:
            self.n = self.ln + self.lsa + self.ls + self.la
        return self.n


    def guess(self):
        guess=""
        p=self.pd
        if self.count<7:
            self.count +=1
            for i in range(1):
                guess = ""
                for letter in range(len(p)):
                    guess_pass = random.choice(self.n)
                    guess = guess + guess_pass
            if guess == p:
                print("You Win",namev.get())
                v="You Win",namev.get()
                self.speaking(v)
            else:
                print("NOT found!,Your guess is", guess, "take another chance")
                v="NOT found!,Your guess is", guess, "take another chance"
                self.speaking(v)
        else:
            print("I win ",namev.get(),"... Passsword was..",password.get())
            s="I win ",namev.get()," Passsword was",password.get()
            self.speaking(s)


    def reset(self):
        find = str(pin.get())
        user= namev.get()
        f = open("Password manager.text", "r+")
        c = 0
        d = 0
        n = 6
        vari = 0
        mylist = []
        for i in range(0, n):
            p = ""
            stri = f.readline()
            mylist.append(stri)
            c += 1

            for i in stri:
                if len(p) < 4:
                    if i in self.ln:
                        p = p + i

            if p==find:
                temp = self.search(user, stri)
                if temp=='1':
                    vari = c
                    d = 1
                else:
                    print("Invalid User name...\n OR...")
                    self.speaking("Invalid User name...\n OR...")
        f.close()

        if d == 1:
            f1 = open("Password manager.text", "r")
            data = f1.readlines()
            del data[vari - 1]
            f1.close()

            with open("Password manager.text", 'w') as f:
                for lines in data:
                    f.write(str(lines))
                self.speaking('Your Previous data is eraised ,now click on next button to continue')
        else:
            print("Not saved in file....")
            self.speaking("Not saved in file....")

    def search(self,user,stri):
        patt = re.compile(user)
        st = '0'
        matches = patt.finditer(stri)
        for match in matches:
            st = match
            if st == '0':
                print('please Enter correct name')
            else:
                st = '1'
                return st

    def strength(self):
        def upper(check) :
            u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for i in u:
              for j in check:
                if i==j:
                    return 1

        def lower(check):
            low="abcdefghijklmnopqrstuvwxyz"
            for i in low:
                for j in check:
                    if i==j:
                        return 1

        def num(check):
            val="0123456789"
            for i in val:
                for j in check:
                    if i==j:
                        return 1

        def special(check):
            z="@#&$"
            for i in z:
                for j in check:
                    if i==j:
                        return 1

        def length(check):
            c=0
            for i in check:
                c=c+1
            if c>6 and c<16:
                return 1

        g= upper(self.pd)
        h= lower(self.pd)
        e=num(self.pd)
        j= special(self.pd)
        k= length(self.pd)
        if g==1 and  h==1 and e==1 and j==1 and k==1:
            print("valid password")
        else:
            if g!=1:
                print("upper case is not available")
                self.speaking("upper case is not available")
            elif h!=1:
                print("lower case is not available")
                self.speaking("lower case is not available")
            elif e!=1:
                print("Integer is not available")
                self.speaking("Integer is not available")
            elif j!=1:
                print("special case is not available")
                self.speaking("special case is not available")
            elif k!=1:
                print("Minimum length 6 characters.Maximum length 16 characters.")
                self.speaking("Minimum length 6 characters.Maximum length 16 characters.")
            else:
                print('Your Password is very very strong')
                self.speaking('Your Password is very very strong')

    def saving(self):
        with open("Password manager.text", 'a') as f:
            f.write(f"{[pin.get(),namev.get(),roll.get() , email.get(), password.get()]}\n")
        tmsg.showinfo("Saved","Your data is stored. THANKS")
        self.speaking('Your Data is saved and Thanks for saving ')

    def randompin(self):
        self.pd=""
        Mylist=[]
        for i in range(0,4):
            a=random.choice(self.ln)
            self.pd=a+self.pd
        if self.pd not in Mylist and len(self.pd)==4:
            Mylist.append(self.pd)
            pin.set(self.pd)
            self.speaking('This is your pin. this will help you in reset your Password')
        else:
            self.randompin()

    def Discription(self):
        self.clear()
        msg="This is Password Manager."
        msg2="This Mini Python project is capable in performing Four Main task." \
             "\nWhich are as follow:-"
        msg1='''
        1-> Can Generate Random Password
        2-> User can save his/her user USER ID and Password
        3-> User can "Reset" his/her Saved Password.
        4-> User can play a "Guess Password" game'''
        can.create_text(300,100,text=msg,tags=6,font=" arieal 22 bold",fill='red')
        can.create_text(300,150,text=msg2,tags=6,font=" arieal 13 bold")
        can.create_text(280,250,text=msg1,tags=5,font=" arieal 15 bold")

    def Module(self):
        self.clear()
        msg='''Module's imported in Project are as follows:-'''
        msg1=''' 
        1-> tkinter Module 
        2-> Random Module
        3-> sys Module
        4-> DateTime Module
        5-> re Module
        6-> pyttsx3 Module'''
        can.create_text(350,50,text=msg,tags=4,font=" arieal 17 bold",fill='dark blue')
        can.create_text(250,200,text=msg1,tags=3,font=" arieal 20 bold")

    def Widgets(self):
        self.clear()
        msg = '''Widget's of tkinter class \nused  in this Project are as follows:-'''
        msg1 = ''' 
                1-> Label Widget
                2-> Frame Widget
                3-> canvas Widget
                4-> Button Widget
                5-> Radiobutton Widget
                6-> Checkbox Widget
                7-> Entry Widget
                8-> Toplevel Widget'''
        can.create_text(350, 100, text=msg,tags=1,font=" arieal 22 bold",fill='Purple')
        can.create_text(210, 230, text=msg1,tags=2,font=" arieal 15 bold")

    def Feature(self):
        self.clear()
        msg = ''' Feature's.......'''
        msg1 = ''' 
                1-> The most important feature this projects provides is that, User can 
                    Generate a random password(user can choose the character of Password from Upper case,
                    lower case, Number , special character)and also can make his own Password 
                
                2-> Second Feature, User can check Strength Of the password.
                
                3-> Third Feature, User can save his/her USER ID and PASSWORD.
                
                4-> Fourth Feature,User can Reset his/her saved Password
                
                5-> Fifth, User can Play a "GAME" with us, in which we generate a randow password
                    and now,user have to guess the password.Hw/She will get 5 chances to guess.'''
        can.create_text(300, 80, text=msg, tags=7,font=" arieal 30 bold",fill='red')
        can.create_text(330, 200, text=msg1, tags=7,font=" arieal 10 bold")

    def clear(self):
        for i in range(1,3):
            can.delete(1,2,3,4,5,6,7,8)

    def Exit(self):
        tmsg.showinfo("Thank You", "PLEASE! Visit again..... THANKS")
        sys.exit("Thank you")

    def speaking(self,audio):
        speak(audio)


window=Manager()
window.title("Password Manager")
window.geometry("1170x577")

# pic=PhotoImage(file='C:\\Users\\shiva\\Pictures\\Ncc.png')
# eve=PhotoImage(file='C:\\Users\\shiva\\Pictures\\even.png')
# noon=PhotoImage(file='C:\\Users\\shiva\\Pictures\\noo.png')
# pic1=PhotoImage(file='C:\\Users\\shiva\\Pictures\\pic pro.png')
# pic2=PhotoImage(file='C:\\Users\\shiva\\Pictures\\pic3.png')
# pic4=PhotoImage(file='C:\\Users\\shiva\\Pictures\\pic4.png')
# pic5=PhotoImage(file='C:\\Users\\shiva\\Pictures\\pic5.png')
# pic6=PhotoImage(file='C:\\Users\\shiva\\Pictures\\pic2.png')
label=ttk.Label(window).grid(row=0,column=0,rowspan=10,columnspan=10)
Label(window,text="WELCOME!\n We keep your Password safe....",font=" arieal 19 bold").grid(row=0,column=0,columnspan=3)

hour=int(datetime.datetime.now().hour)
minute=int(datetime.datetime.now().minute)
date=datetime.datetime.now().date()
Label(window,text='Time = ',font=" arieal 19 bold").grid(row=0,column=5,sticky=E,columnspan=2)
Label(window,text='Date = ',font=" arial 19 bold").grid(row=1,column=5,sticky=NE,columnspan=2)
Label(window,text=hour,font=" arial 19 bold").grid(row=0,column=7,sticky=E)
Label(window,text=':',font=" arial 19 bold").grid(row=0,column=8,ipadx=10)
Label(window,text=minute,font=" arial 19 bold").grid(row=0,column=9,sticky=W)
Label(window,text=date,font=" arial 19 bold").grid(ipadx=3,ipady=1,row=1,column=8,columnspan=2,sticky=NW)

namev=StringVar()
roll=StringVar()
phone = StringVar()
email = StringVar()
pin = StringVar()
password = StringVar()
text = StringVar()
text2 = StringVar()
che1 = IntVar()
che2 = IntVar()
che3 = IntVar()
che4 = IntVar()
radio1=IntVar()
radio2=IntVar()

f1=Frame(window,bg="black",borderwidth=10,relief="ridge")
f1.grid(row=3 ,column=4,rowspan=5)

can=Canvas(window,width=600,height=420,relief=SUNKEN,borderwidth=10,bg='white')
can.grid(row=1,column=0,columnspan=7,rowspan=5,sticky=W)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

if hour>=0 and hour<12:
    can.create_image(18, 20, image=pic, anchor=NW)
    window.speaking('Good Morning')
elif hour>=12 and hour<17:
    can.create_image(18, 20, anchor=NW)
    window.speaking('Good Afternoon')
else:
    can.create_image(10, 15, image=eve, anchor=NW)
    window.speaking('Goooood Evening ')

Button(f1,text="Discription",command=window.Discription).grid(row=3 ,column=0,ipadx=3,ipady=3,padx=3,pady=3)
Button(f1,text="  Modules  ",command=window.Module).grid(row=4 ,column=0,ipadx=3,ipady=3,padx=3,pady=3)
Button(f1,text="  Features  ",command=window.Feature).grid(row=5 ,column=0,ipadx=4,ipady=4,padx=3,pady=3)
Button(f1,text="    Widget  ",command=window.Widgets).grid(row=6 ,column=0,ipadx=4,ipady=4,padx=3,pady=3)
Button(f1,text="     Clear     ",command=window.clear).grid(row=7 ,column=0,ipadx=4,ipady=4,padx=3,pady=3)

Button(window,text="New Passsword",command=window.Window1).grid(row=8 ,column=0,ipadx=3)
Button(window,text="New Save",command=window.Window2).grid(row= 8,column=1,ipadx=3)
Button(window,text="Play Game",command=window.gamewindow).grid(row=8 ,column=2,ipadx=2)
Button(window,text="Reset Password",command=window.Resetwindow).grid(row=8 ,column=3,ipadx=3)
Button(window,text="Exit",command=window.Exit).grid(row=8 ,column=4,ipadx=13)

window.mainloop()
