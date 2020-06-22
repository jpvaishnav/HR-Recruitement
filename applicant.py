import os
import pickle
import sys
from subprocess import call
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
details_list=[]

#saving attributes in database
def file_save():
    NAME_PRO = details_list[0]
    EMAIL_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    PRICE=details_list[3]
    f = open("database/applicant.dat", "ab")
    a=save(NAME_PRO,EMAIL_PRO,MOBILE_NO_PRO,PRICE)
    pickle.dump(a,f,protocol=2)
    f.close()
    restart_program()


u = list()

m = [9]
G = []
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


class save:
    def __init__(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,PRICE):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.price=PRICE
        



class applicant:
    #define consttuctor
    def __init__(self):
        #define data members
        self.NAME=""
        self.ADDERESS=""
        self.MOBILE=""
        self.DAYS=0
        self.price=0
        self.room=0
        #define method fucntion
        def chk_name():
            while True:

                self.k = str(self.name.get())

                a = self.k.isdigit()
                if len(self.k) != 0 and a != True:
                    self.NAME=self.k
                    self.Text1.insert(INSERT, "NAME ENTERED""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "INVALID NAME, PLEASE TRY AGAIN!""\n")

                    break

        def chk_add():
            while True:
                self.g = str(self.addr.get())


                ak = self.g.isdigit()
                if len(self.g)!= 0 and ak!=True and '@' in self.g:
                    self.ADDERESS=self.g
                    self.Text1.insert(INSERT, "EMAIL ENTERED""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "INVALID ADDRESS , PLEASE TRY AGAIN!""\n")

                    break

        def chk_mo():
            while True:

                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    self.MOBILE = self.h
                    self.Text1.insert(INSERT, "MOBILE NUMBER ENTERED""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "INVALID MOBILE NO. , PLEASE TRY AGAIN!""\n")
                break

        def chk_price():
            while True:

                self.l = str(self.price)

                if len(self.l)!=0 and self.l.isdigit:
                    self.PRICE = int(self.l)
                    self.Text1.insert(INSERT, "MARKS ENTERED""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input ""\n")
                    break

        def enter(self):
            self.name = self.NAME
            self.address = self.ADDERESS
            self.mobile_no = self.MOBILE
            self.price=self.price
            self.no_of_days = int(self.DAYS)


        def submit_clicked():
            details_list.append(self.NAME)
            details_list.append(self.ADDERESS)
            details_list.append(self.MOBILE)
            details_list.append(self.room)
            details_list.append(self.price)
            file_save()



        root = Tk()


        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: '#d9d9d9'
        _fgcolor = '#000000'  # X11 color: '#d9d9d9'
        _compcolor = '#d9d9d9' # X11 color: '#d9d9d9'
        _ana1color = '#d9d9d9' # X11 color: '#d9d9d9'
        _ana2color = '#d9d9d9' # X11 color: '#d9d9d9'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 19 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1069x742")
        root.title("PRESENTATION IN SEMINAR")
        root.configure(background="#272727")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="#d9d9d9")

        self.Text1 = Text(root)
        self.Text1.place(relx=0.03, rely=0.65, relheight=0.29, relwidth=0.93)
        self.Text1.configure(background="#272727")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="#d9d9d9")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="#d9d9d9")
        self.Text1.configure(insertbackground="#d9d9d9")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="#d9d9d9")
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=WORD)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#272727")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#d9d9d9")
        self.Frame1.configure(width=995)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.5)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="#d9d9d9")
        self.Message1.configure(text='''SEMINAR REGISTRATION''')
        self.Message1.configure(width=496)

        self.Message2 = Message(self.Frame1)
        self.Message2.place(relx=0.54, rely=0.19, relheight=0.74, relwidth=0.07)
        self.Message2.configure(background="#272727")
        self.Message2.configure(font=font11)
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="#d9d9d9")
        self.Message2.configure(text=''':''')
        self.Message2.configure(width=66)

        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.57, rely=0.11, relheight=0.84, relwidth=0.35)
        self.Message3.configure(background="#d9d9d9")
        self.Message3.configure(font=font11)
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="#d9d9d9")
        self.Message3.configure(text='''APPLICANT ''')
        self.Message3.configure(width=347)

        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.03, rely=0.18, relheight=0.46, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#272727")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="#d9d9d9")
        self.Frame2.configure(width=995)

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.05, rely=0.03, height=44, width=330)
        self.Label3.configure(activebackground="#d9d9d9")
        self.Label3.configure(activeforeground="#d9d9d9")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#bfbfbf")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="#d9d9d9")
        self.Label3.configure(text='''ENTER NAME''')

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.05, rely=0.29, height=44, width=330)
        self.Label4.configure(activebackground="#d9d9d9")
        self.Label4.configure(activeforeground="#d9d9d9")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#bfbfbf")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="#d9d9d9")
        self.Label4.configure(text='''ENTER CONTACT NUMBER''')



        self.Entry3 = Entry(self.Frame2)
        self.name=StringVar()
        self.Entry3.place(relx=0.47, rely=0.05,height=34, relwidth=0.43)
        self.Entry3.configure(background="#d9d9d9")
        self.Entry3.configure(disabledforeground="#bfbfbf")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="#d9d9d9")
        self.Entry3.configure(insertbackground="#d9d9d9")
        self.Entry3.configure(selectbackground="#e6e6e6")
        self.Entry3.configure(selectforeground="#d9d9d9")
        self.Entry3.configure(textvariable=self.name)


        self.Entry4 = Entry(self.Frame2)
        self.mobile=StringVar()
        self.Entry4.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
        self.Entry4.configure(background="#d9d9d9")
        self.Entry4.configure(disabledforeground="#bfbfbf")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="#d9d9d9")
        self.Entry4.configure(insertbackground="#d9d9d9")
        self.Entry4.configure(selectbackground="#e6e6e6")
        self.Entry4.configure(selectforeground="#d9d9d9")
        self.Entry4.configure(textvariable=self.mobile)


        self.Entry5 = Entry(self.Frame2)
        self.addr = StringVar()
        self.Entry5.place(relx=0.47, rely=0.18,height=34, relwidth=0.43)
        self.Entry5.configure(background="#d9d9d9")
        self.Entry5.configure(disabledforeground="#bfbfbf")
        self.Entry5.configure(font=font10)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="#d9d9d9")
        self.Entry5.configure(insertbackground="#d9d9d9")
        self.Entry5.configure(selectbackground="#e6e6e6")
        self.Entry5.configure(selectforeground="#d9d9d9")
        self.Entry5.configure(textvariable=self.addr)

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.05, rely=0.16, height=44, width=330)
        self.Label5.configure(activebackground="#272727")
        self.Label5.configure(activeforeground="#d9d9d9")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#bfbfbf")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="#d9d9d9")
        self.Label5.configure(text='''ENTER EMAIL: ID''')

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.05, rely=0.43, height=44, width=330)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ENTER EVALUATION MARKS''')

        


        self.Message4 = Message(self.Frame2)
        self.Message4.place(relx=0.41, rely=0.04, relheight=0.1, relwidth=0.05)
        self.Message4.configure(background="#272727")
        self.Message4.configure(font=font13)
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="#d9d9d9")
        self.Message4.configure(text=''':''')
        self.Message4.configure(width=46)

        self.Message5 = Message(self.Frame2)
        self.Message5.place(relx=0.42, rely=0.17, relheight=0.12, relwidth=0.03)
        self.Message5.configure(background="#272727")
        self.Message5.configure(font=font13)
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="#d9d9d9")
        self.Message5.configure(text=''':''')
        self.Message5.configure(width=26)

        self.Message6 = Message(self.Frame2)
        self.Message6.place(relx=0.415, rely=0.3, relheight=0.09, relwidth=0.04)
        self.Message6.configure(background="#272727")
        self.Message6.configure(font=font13)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="#d9d9d9")
        self.Message6.configure(text=''':''')
        self.Message6.configure(width=36)

        self.Message6 = Message(self.Frame2)
        self.Message6.place(relx=0.415, rely=0.43, relheight=0.09, relwidth=0.04)
        self.Message6.configure(background="#272727")
        self.Message6.configure(font=font13)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="#d9d9d9")
        self.Message6.configure(text=''':''')
        self.Message6.configure(width=36)


        

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.91, rely=0.05, height=33, width=43)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#d9d9d9")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')
        self.Button1.configure(command=chk_name)

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.18, height=33, width=43)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="#d9d9d9")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')
        self.Button2.configure(command=chk_add)

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.91, rely=0.31, height=33, width=43)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="#d9d9d9")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''OK''')
        self.Button3.configure(command=chk_mo)

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.91, rely=0.43, height=33, width=43)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="#d9d9d9")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''OK''')
        self.Button5.configure(command=chk_price)

        self.Entry1 = Entry(self.Frame2)
        self.days=StringVar()
        self.Entry1.place(relx=0.47, rely=0.43, height=34, relwidth=0.43)
        self.Entry1.configure(background="#d9d9d9")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="#d9d9d9")
        self.Entry1.configure(width=424)
        self.Entry1.configure(textvariable=self.price)

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.76, rely=0.66, height=44, width=156)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font16)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="#d9d9d9")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''SUBMIT''')
        self.Button4.configure(command=submit_clicked)
        root.mainloop()

if __name__ == '__main__':
    apl=applicant()






