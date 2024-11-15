from tkinter import *
import math
import tkinter.messagebox

root = Tk()

# {geometry -> 650x400} {location on x, y -> 300+300}
root.geometry("650x400+300+300")
root.title("Scientific Calculator")
switch = None

# functions for buttons
def btn_1():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')

def btn_2():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')

def btn_3():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')

def btn_4():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')

def btn_5():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')

def btn_6():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')

def btn_7():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')

def btn_8():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')

def btn_9():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')

def btn_0():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')

# funcs for operators
def plus():
    pos = len(disp.get())
    disp.insert(pos, '+')

def minus():
    pos = len(disp.get())
    disp.insert(pos, '-')

def mul():
    pos = len(disp.get())
    disp.insert(pos, 'x')

def div():
    pos = len(disp.get())
    disp.insert(pos, '÷')

# trigo
def sin():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else :
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        disp.delete(0, END)
        disp.insert(0, '0')
        tkinter.messagebox.showerror("Value Error!")

def cos():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else :
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        disp.delete(0, END)
        disp.insert(0, '0')
        tkinter.messagebox.showerror("Value Error!")

def tan():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else :
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        disp.delete(0, END)
        disp.insert(0, '0')
        tkinter.messagebox.showerror("Value Error!")

# inverse trigo
def asin():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.asin(math.radians(ans))
        else :
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        disp.delete(0, END)
        disp.insert(0, '0')
        tkinter.messagebox.showerror("Value Error!")

def acos():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.acos(math.radians(ans))
        else :
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        disp.delete(0, END)
        disp.insert(0, '0')
        tkinter.messagebox.showerror("Value Error!")

def atan():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.atan(math.radians(ans))
        else :
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        disp.delete(0, END)
        disp.insert(0, '0')
        tkinter.messagebox.showerror("Value Error!")

# power btn
def pow():
    pos = len(disp.get())
    disp.insert(pos, "^")

def dot():
    pos = len(disp.get())
    disp.insert(pos, ".")

def insertOpenBkt():
    pos = len(disp.get())
    disp.insert(pos, "(")

def insertCloseBkt():
    pos = len(disp.get())
    disp.insert(pos, ")")
def evaluate():
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)
    except Exception:
        disp.delete(0, END)
        disp.insert(0, '0')
        tkinter.messagebox.showerror("Value Error!")

def clear():
    disp.delete(0, END)
    disp.insert(0, 0)

def modulo():
    pos = len(disp.get())
    disp.insert(pos, "%")

def pi():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))

def exp():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))

# Entry screen widget (for output)
disp = Entry(root, font="Verdana 20", fg="Black", bg="mistyrose", bd=4, justify=RIGHT)
disp.insert(0, '0')
disp.pack(expand=True, fill=BOTH)

# Frame for buttons
row1 = Frame(root, bg="#000000")
row1.pack(expand=True, fill=BOTH)

# Row 1 Buttons
pibtn = Button(row1, text="π", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
pibtn.pack(side=LEFT, expand=True, fill=BOTH)

factbtn = Button(row1, text="x!", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
factbtn.pack(side=LEFT, expand=True, fill=BOTH)

sinbtn = Button(row1, text="sin", font="segoe18", relief=GROOVE, bd = 0, command = sin, fg="white", bg="#333333")
sinbtn.pack(side=LEFT, expand=True, fill=BOTH)

cosbtn = Button(row1, text="cos", font="segoe18", relief=GROOVE, bd = 0, command= cos, fg="white", bg="#333333")
cosbtn.pack(side=LEFT, expand=True, fill=BOTH)

tanbtn = Button(row1, text="tan", font="segoe18", relief=GROOVE, bd = 0, command = tan, fg="white", bg="#333333")
tanbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn1 = Button(row1, text="1", font="segoe18", relief=GROOVE, bd = 0, command=btn_1, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(row1, text="2", font="segoe18", relief=GROOVE, bd = 0, command=btn_2, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(row1, text="3", font="segoe18", relief=GROOVE, bd = 0, command=btn_3, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=True, fill=BOTH)

plusBtn = Button(row1, text="+", font="segoe18", relief=GROOVE, bd = 0, command=plus, fg="white", bg="#333333")
plusBtn.pack(side=LEFT, expand=True, fill=BOTH)

# Row 2 Buttons
row2 = Frame(root, bg="#000000")
row2.pack(expand=True, fill=BOTH)

e_btn = Button(row2, text="e", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
e_btn.pack(side=LEFT, expand=True, fill=BOTH)

sqrrootbtn = Button(row2, text="√x", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
sqrrootbtn.pack(side=LEFT, expand=True, fill=BOTH)

sinhbtn = Button(row2, text="sinh", font="segoe18", relief=GROOVE, bd = 0, command=asin, fg="white", bg="#333333")
sinhbtn.pack(side=LEFT, expand=True, fill=BOTH)

coshbtn = Button(row2, text="cosh", font="segoe18", relief=GROOVE, bd = 0, command = acos, fg="white", bg="#333333")
coshbtn.pack(side=LEFT, expand=True, fill=BOTH)

tanhbtn = Button(row2, text="tanh", font="segoe18", relief=GROOVE, bd = 0, command = atan, fg="white", bg="#333333")
tanhbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn4 = Button(row2, text="4", font="segoe18", relief=GROOVE, bd = 0, command=btn_4, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=True, fill=BOTH)

btn5 = Button(row2, text="5", font="segoe18", relief=GROOVE, bd = 0, command=btn_5, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=True, fill=BOTH)

btn6 = Button(row2, text="6", font="segoe18", relief=GROOVE, bd = 0, command=btn_6, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=True, fill=BOTH)

minusBtn = Button(row2, text="-", font="segoe18", relief=GROOVE, bd = 0,command=minus, fg="white", bg="#333333")
minusBtn.pack(side=LEFT, expand=True, fill=BOTH)


# row 3 buttons
row3 = Frame(root, bg="#000000")
row3.pack(expand=True, fill=BOTH)

conv_btn = Button(row3, text="Rad", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
conv_btn.pack(side=LEFT, expand=True, fill=BOTH)

round_btn = Button(row3, text="round", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
round_btn.pack(side=LEFT, expand=True, fill=BOTH)

ln_btn = Button(row3, text="ln", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
ln_btn.pack(side=LEFT, expand=True, fill=BOTH)

log_btn = Button(row3, text="log", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
log_btn.pack(side=LEFT, expand=True, fill=BOTH)

powerbtn = Button(row3, text="x^y", font="segoe18", relief=GROOVE, bd = 0, command=pow, fg="white", bg="#333333")
powerbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn7 = Button(row3, text="7", font="segoe18", relief=GROOVE, bd = 0, command=btn_7, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=True, fill=BOTH)

btn8 = Button(row3, text="8", font="segoe18", relief=GROOVE, bd = 0, command=btn_8, fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=True, fill=BOTH)

btn9 = Button(row3, text="9", font="segoe18", relief=GROOVE, bd = 0, command=btn_9, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=True, fill=BOTH)

mulBtn = Button(row3, text="x", font="segoe18", relief=GROOVE, bd = 0, command=mul , fg="white", bg="#333333")
mulBtn.pack(side=LEFT, expand=True, fill=BOTH)



# row 4 buttons
row4 = Frame(root, bg="#000000")
row4.pack(expand=True, fill=BOTH)

mod_btn = Button(row4, text="%", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
mod_btn.pack(side=LEFT, expand=True, fill=BOTH)

openbkt_btn = Button(row4, text="(", font="segoe18", relief=GROOVE, bd = 0, command = insertOpenBkt, fg="white", bg="#333333")
openbkt_btn.pack(side=LEFT, expand=True, fill=BOTH)

closebkt_btn = Button(row4, text=")", font="segoe18", relief=GROOVE, bd = 0, command = insertCloseBkt, fg="white", bg="#333333")
closebkt_btn.pack(side=LEFT, expand=True, fill=BOTH)

dot_btn = Button(row4, text=".", font="segoe18", relief=GROOVE, bd = 0, command = dot, fg="white", bg="#333333")
dot_btn.pack(side=LEFT, expand=True, fill=BOTH)

clearbtn = Button(row4, text="C", font="segoe18", relief=GROOVE, bd = 0, command = clear, fg="white", bg="#333333")
clearbtn.pack(side=LEFT, expand=True, fill=BOTH)

del_btn = Button(row4, text="⌫", font="segoe18", relief=GROOVE, bd = 0, fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=True, fill=BOTH)

btn0 = Button(row4, text="0", font="segoe18", relief=GROOVE, bd = 0, command=btn_0, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=True, fill=BOTH)

equal_btn = Button(row4, text="=", font="segoe18", relief=GROOVE, bd = 0, command=evaluate, fg="white", bg="#333333")
equal_btn.pack(side=LEFT, expand=True, fill=BOTH)

divide_btn = Button(row4, text="÷", font="segoe18", relief=GROOVE, bd = 0, command=div, fg="white", bg="#333333")
divide_btn.pack(side=LEFT, expand=True, fill=BOTH)



root.mainloop()
