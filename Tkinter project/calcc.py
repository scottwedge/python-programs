from tkinter import *
q=Tk()
q.title("calulator")
b=Label(q,text="",width=20)
b.grid(row=0,column=0,columnspan=5)
b1=Button(q,text='0',command=lambda : show(0),width=5)
b1.grid(row=1,column=0)
b2=Button(q,text='1',command=lambda : show(1),width=5)
b2.grid(row=1,column=1)
b3=Button(q,text='2',command=lambda : show(2),width=5)
b3.grid(row=1,column=2)
b4=Button(q,text='3',command=lambda : show(3),width=5)
b4.grid(row=1,column=3)
b5=Button(q,text='4',command=lambda : show(4),width=5)
b5.grid(row=1,column=4)
b6=Button(q,text='5',command=lambda : show(5),width=5)
b6.grid(row=2,column=0)
b7=Button(q,text='6',command=lambda : show(6),width=5)
b7.grid(row=2,column=1)
b8=Button(q,text='7',command=lambda : show(7),width=5)
b8.grid(row=2,column=2)
b9=Button(q,text='8',command=lambda : show(8),width=5)
b9.grid(row=2,column=3)
b10=Button(q,text='9',command=lambda : show(9),width=5)
b10.grid(row=2,column=4)

#for operators
ad=Button(q,text='+',command=lambda  : show("+"),width=5)
ad.grid(row=3,column=0)
su=Button(q,text='-',command=lambda : show("-"),width=5)
su.grid(row=3,column=1)
mu=Button(q,text='*',command=lambda : show("*"),width=5)
mu.grid(row=3,column=2)
di=Button(q,text='/',command=lambda : show("/"),width=5)
di.grid(row=3,column=3)
clr=Button(q,text='C',command=lambda  :b.configure(text=""),width=5)
clr.grid(row=1,column=5)
def equa():
    st=b['text']
    if "+" in st:
        li=st.split("+")
        s=int(li[0])+int(li[1])
        b.configure(text=str(s))
    elif "-" in st:
        li=st.split("-")
        s=int(li[0])-int(li[1])
        b.configure(text=str(s))
    elif "*" in st:
        li=st.split("*")
        s=int(li[0])*int(li[1])
        b.configure(text=str(s))
    elif "/" in st:
        li=st.split("/")
        s=int(li[0])/int(li[1])
        b.configure(text=str(s))
eq=Button(q,text='=',command=equa,width=11,)
eq.grid(row=3,column=4,columnspan=2,)
def show(a):
    t=a
    b.configure(text=b['text']+str(t))
q.mainloop()