from tkinter import *
import math
import re
import tkinter.messagebox

root = Tk()

# {geometry -> 650x400} {location on x, y -> 300+300}
root.geometry("650x400+300+300")
root.title("Scientific Calculator")
switch = None

# Replace 'n!' with 'factorial(n)'
def preprocess(expression):
    expression = re.sub(r'(\d+)!', r'factorial(\1)', expression)
    return expression

safe_env = {
    "__builtins__": None,  # Disable access to Python's built-in functions
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "log": math.log,      
    "log10": math.log10,  
    "factorial": math.factorial,
    "pi": math.pi,        
    "e": math.e,   
    "round" : round        

}

# function for inserting '0 - 9', '+', '-', '*', '/', '.' , '**', '(' , ')', '%' , 'cos', 'sin', 'tan', 'acos', 'asin', 'atan', 'e', 'pi'
def insert_in_display(value : str):
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, value)


def conv():
    global switch
    if switch is None or not switch:
        switch = True
        conv_btn.config(text='Deg') 
    else :
        switch = False
        conv_btn.config(text='Rad')


def evaluate():
    try:
        result = disp.get()
        cleanedExpression = preprocess(result)
        result = eval(cleanedExpression, {"__builtins__": None}, safe_env)
        disp.delete(0, END)
        disp.insert(0, result)
    except Exception as e:
        tkinter.messagebox.showerror("Value Error!", f"Invalid input: {e}")



def delete():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '' or display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else :
        disp.delete(0, END)
        disp.insert(0, display[0 : pos - 1])

def clear():
    disp.delete(0, END)
    disp.insert(0, 0) 

# ---------------------------------------------------


# Entry screen widget (for output)
disp = Entry(root, font="Verdana 20", fg="Black", bg="mistyrose", bd=4, justify=RIGHT)
disp.insert(0, '0')
disp.pack(expand=True, fill=BOTH)

# Frame for buttons
row1 = Frame(root, bg="#000000")
row1.pack(expand=True, fill=BOTH)

# Row 1 Buttons
pibtn = Button(row1, text="π", font="segoe18", relief=GROOVE, bd = 0, command = lambda : insert_in_display("pi"), fg="white", bg="#333333")
pibtn.pack(side=LEFT, expand=True, fill=BOTH)

factbtn = Button(row1, text="x!", font="segoe18", relief=GROOVE, bd = 0, command = lambda : insert_in_display("!"), fg="white", bg="#333333")
factbtn.pack(side=LEFT, expand=True, fill=BOTH)
 
sinbtn = Button(row1, text="sin", font="segoe18", relief=GROOVE, bd = 0, command = lambda: insert_in_display("sin"), fg="white", bg="#333333")
sinbtn.pack(side=LEFT, expand=True, fill=BOTH)

cosbtn = Button(row1, text="cos", font="segoe18", relief=GROOVE, bd = 0, command = lambda: insert_in_display("cos"), fg="white", bg="#333333")
cosbtn.pack(side=LEFT, expand=True, fill=BOTH)

tanbtn = Button(row1, text="tan", font="segoe18", relief=GROOVE, bd = 0, command = lambda: insert_in_display("tan"), fg="white", bg="#333333")
tanbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn1 = Button(row1, text="1", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('1'), fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(row1, text="2", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('2'), fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(row1, text="3", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('3'), fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=True, fill=BOTH)

plusBtn = Button(row1, text="+", font="segoe18", relief=GROOVE, bd = 0, command = lambda: insert_in_display('+'), fg="white", bg="#333333")
plusBtn.pack(side=LEFT, expand=True, fill=BOTH)

# Row 2 Buttons
row2 = Frame(root, bg="#000000")
row2.pack(expand=True, fill=BOTH)

e_btn = Button(row2, text="e", font="segoe18", relief=GROOVE, bd = 0, command = lambda : insert_in_display("e"), fg="white", bg="#333333")
e_btn.pack(side=LEFT, expand=True, fill=BOTH)

sqrrootbtn = Button(row2, text="√x", font="segoe18", relief=GROOVE, command=lambda: insert_in_display("sqrt"), bd = 0, fg="white", bg="#333333")
sqrrootbtn.pack(side=LEFT, expand=True, fill=BOTH)

sinhbtn = Button(row2, text="sinh", font="segoe18", relief=GROOVE, bd = 0, command=lambda: insert_in_display("acos"), fg="white", bg="#333333")
sinhbtn.pack(side=LEFT, expand=True, fill=BOTH)

coshbtn = Button(row2, text="cosh", font="segoe18", relief=GROOVE, bd = 0, command=lambda: insert_in_display("acos"), fg="white", bg="#333333")
coshbtn.pack(side=LEFT, expand=True, fill=BOTH)

tanhbtn = Button(row2, text="tanh", font="segoe18", relief=GROOVE, bd = 0, command=lambda: insert_in_display("acos"), fg="white", bg="#333333")
tanhbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn4 = Button(row2, text="4", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('4'), fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=True, fill=BOTH)

btn5 = Button(row2, text="5", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('5'), fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=True, fill=BOTH)

btn6 = Button(row2, text="6", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('6'), fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=True, fill=BOTH)

minusBtn = Button(row2, text="-", font="segoe18", relief=GROOVE, bd = 0,command = lambda: insert_in_display('-'),  fg="white", bg="#333333")
minusBtn.pack(side=LEFT, expand=True, fill=BOTH)


# row 3 buttons
row3 = Frame(root, bg="#000000")
row3.pack(expand=True, fill=BOTH)

conv_btn = Button(row3, text="Rad", font="segoe18", relief=GROOVE, bd = 0, command = conv, fg="white", bg="#333333")
conv_btn.pack(side=LEFT, expand=True, fill=BOTH)

round_btn = Button(row3, text="round", font="segoe18", relief=GROOVE, bd = 0, command = lambda: insert_in_display("round"), fg="white", bg="#333333")
round_btn.pack(side=LEFT, expand=True, fill=BOTH)

ln_btn = Button(row3, text="ln", font="segoe18", relief=GROOVE, bd = 0, command = lambda: insert_in_display("log"), fg="white", bg="#333333")
ln_btn.pack(side=LEFT, expand=True, fill=BOTH)

log_btn = Button(row3, text="log", font="segoe18", relief=GROOVE, bd = 0, command = lambda:insert_in_display("log10"), fg="white", bg="#333333")
log_btn.pack(side=LEFT, expand=True, fill=BOTH)

powerbtn = Button(row3, text="x^y", font="segoe18", relief=GROOVE, bd = 0, command = lambda : insert_in_display('**'), fg="white", bg="#333333")
powerbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn7 = Button(row3, text="7", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('7'), fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=True, fill=BOTH)

btn8 = Button(row3, text="8", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('8'), fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=True, fill=BOTH)

btn9 = Button(row3, text="9", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('9'), fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=True, fill=BOTH)

mulBtn = Button(row3, text="x", font="segoe18", relief=GROOVE, bd = 0, command = lambda: insert_in_display('*'), fg="white", bg="#333333")
mulBtn.pack(side=LEFT, expand=True, fill=BOTH)



# row 4 buttons
row4 = Frame(root, bg="#000000")
row4.pack(expand=True, fill=BOTH)

mod_btn = Button(row4, text="%", font="segoe18", relief=GROOVE, bd = 0, command = lambda: insert_in_display('%'), fg="white", bg="#333333")
mod_btn.pack(side=LEFT, expand=True, fill=BOTH)

openbkt_btn = Button(row4, text="(", font="segoe18", relief=GROOVE, bd = 0, command = lambda : insert_in_display('('), fg="white", bg="#333333")
openbkt_btn.pack(side=LEFT, expand=True, fill=BOTH)

closebkt_btn = Button(row4, text=")", font="segoe18", relief=GROOVE, bd = 0, command = lambda : insert_in_display(')'), fg="white", bg="#333333")
closebkt_btn.pack(side=LEFT, expand=True, fill=BOTH)

dot_btn = Button(row4, text=".", font="segoe18", relief=GROOVE, bd = 0, command = lambda : insert_in_display('.'), fg="white", bg="#333333")
dot_btn.pack(side=LEFT, expand=True, fill=BOTH)

clearbtn = Button(row4, text="C", font="segoe18", relief=GROOVE, bd = 0, command = clear, fg="white", bg="#333333")
clearbtn.pack(side=LEFT, expand=True, fill=BOTH)

del_btn = Button(row4, text="⌫", font="segoe18", relief=GROOVE, bd = 0, command = delete, fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=True, fill=BOTH)

btn0 = Button(row4, text="0", font="segoe18", relief=GROOVE, bd = 0, command= lambda: insert_in_display('0'), fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=True, fill=BOTH)

equal_btn = Button(row4, text="=", font="segoe18", relief=GROOVE, bd = 0, command=evaluate, fg="white", bg="#333333")
equal_btn.pack(side=LEFT, expand=True, fill=BOTH)

divide_btn = Button(row4, text="÷", font="segoe18", relief=GROOVE, bd = 0, command = lambda: insert_in_display('/'), fg="white", bg="#333333")
divide_btn.pack(side=LEFT, expand=True, fill=BOTH)



root.mainloop()