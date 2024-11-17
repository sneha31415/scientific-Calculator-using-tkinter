from tkinter import *
from  functions import *

root = Tk()

# {geometry -> 650x400} {location on x, y -> 300+300}
root.geometry("650x400+300+300")
root.title("Scientific Calculator")



# Entry screen widget (for output)
disp = Entry(root, font="Verdana 20", fg="white", bg="black", bd=10, justify=RIGHT)
disp.insert(0, '0')
disp.pack(expand=True, fill=BOTH)

# Frame for buttons
row1 = Frame(root, bg="#000000")
row1.pack(expand=True, fill=BOTH)

# Row 1 Buttons

Button(row1, text="π", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display(math.pi, disp), fg="white", bg="#333333").pack(side=LEFT, expand=True, fill=BOTH)

factbtn = Button(row1, text="x!", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display("!", disp), fg="white", bg="#333333")
factbtn.pack(side=LEFT, expand=True, fill=BOTH)
 
sinbtn = Button(row1, text="sin", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: insert_in_display("sin", disp), fg="white", bg="#333333")
sinbtn.pack(side=LEFT, expand=True, fill=BOTH)

cosbtn = Button(row1, text="cos", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: insert_in_display("cos", disp), fg="white", bg="#333333")
cosbtn.pack(side=LEFT, expand=True, fill=BOTH)

tanbtn = Button(row1, text="tan", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: insert_in_display("tan", disp), fg="white", bg="#333333")
tanbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn1 = Button(row1, text="1", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('1', disp), fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(row1, text="2", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('2', disp), fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(row1, text="3", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('3', disp), fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=True, fill=BOTH)

plusBtn = Button(row1, text="+", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: insert_in_display('+', disp), fg="white", bg="#333333")
plusBtn.pack(side=LEFT, expand=True, fill=BOTH)


# Row 2 Buttons
row2 = Frame(root, bg="#000000")
row2.pack(expand=True, fill=BOTH)

e_btn = Button(row2, text="e", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display(math.e, disp), fg="white", bg="#333333")
e_btn.pack(side=LEFT, expand=True, fill=BOTH)

sqrrootbtn = Button(row2, text="√x", font="segoe 14", relief=GROOVE, command=lambda: insert_in_display("sqrt", disp), bd = 0, fg="white", bg="#333333")
sqrrootbtn.pack(side=LEFT, expand=True, fill=BOTH)

sinhbtn = Button(row2, text="sinh", font="segoe 12", relief=GROOVE, bd = 0, command=lambda: insert_in_display("asin", disp), fg="white", bg="#333333")
sinhbtn.pack(side=LEFT, expand=True, fill=BOTH)

coshbtn = Button(row2, text="cosh", font="segoe 12 bold", relief=GROOVE, bd = 0, command=lambda: insert_in_display("acos", disp), fg="white", bg="#333333")
coshbtn.pack(side=LEFT, expand=True, fill=BOTH)

tanhbtn = Button(row2, text="tanh", font="segoe 12", relief=GROOVE, bd = 0, command=lambda: insert_in_display("acos", disp), fg="white", bg="#333333")
tanhbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn4 = Button(row2, text="4", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('4', disp), fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=True, fill=BOTH)

btn5 = Button(row2, text="5", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('5', disp), fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=True, fill=BOTH)

btn6 = Button(row2, text="6", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('6', disp), fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=True, fill=BOTH)

minusBtn = Button(row2, text="-", font="segoe 14", relief=GROOVE, bd = 0,command = lambda: insert_in_display('-', disp),  fg="white", bg="#333333")
minusBtn.pack(side=LEFT, expand=True, fill=BOTH)


# row 3 buttons
row3 = Frame(root, bg="#000000")
row3.pack(expand=True, fill=BOTH)

# currently not functional
conv_btn = Button(row3, text="rad", font="segoe 11", relief=GROOVE, bd = 0,  fg="white", bg="#333333")
conv_btn.pack(side=LEFT, expand=True, fill=BOTH)

inverse = Button(row3, text="1/x", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: insert_in_display("/", disp), fg="white", bg="#333333")
inverse.pack(side=LEFT, expand=True, fill=BOTH)

ln_btn = Button(row3, text="ln", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: insert_in_display("ln", disp), fg="white", bg="#333333")
ln_btn.pack(side=LEFT, expand=True, fill=BOTH)

log_btn = Button(row3, text="log", font="segoe 14", relief=GROOVE, bd = 0, command = lambda:insert_in_display("log", disp), fg="white", bg="#333333")
log_btn.pack(side=LEFT, expand=True, fill=BOTH)

powerbtn = Button(row3, text="x^y", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display('**', disp), fg="white", bg="#333333")
powerbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn7 = Button(row3, text="7", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('7', disp), fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=True, fill=BOTH)

btn8 = Button(row3, text="8", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('8', disp), fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=True, fill=BOTH)

btn9 = Button(row3, text="9", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('9', disp), fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=True, fill=BOTH)

mulBtn = Button(row3, text="x", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: insert_in_display('*', disp), fg="white", bg="#333333")
mulBtn.pack(side=LEFT, expand=True, fill=BOTH)



# row 4 buttons
row4 = Frame(root, bg="#000000")
row4.pack(expand=True, fill=BOTH)

mod_btn = Button(row4, text="mod", font="segoe 12", relief=GROOVE, bd = 0, command = lambda: insert_in_display('%', disp), fg="white", bg="#333333")
mod_btn.pack(side=LEFT, expand=True, fill=BOTH)

openbkt_btn = Button(row4, text="(", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display('(', disp), fg="white", bg="#333333")
openbkt_btn.pack(side=LEFT, expand=True, fill=BOTH)

closebkt_btn = Button(row4, text=")", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display(')', disp), fg="white", bg="#333333")
closebkt_btn.pack(side=LEFT, expand=True, fill=BOTH)

dot_btn = Button(row4, text=".", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display('.', disp), fg="white", bg="#333333")
dot_btn.pack(side=LEFT, expand=True, fill=BOTH)

clearbtn = Button(row4, text="C", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: clear(disp), fg="white", bg="#333333")
clearbtn.pack(side=LEFT, expand=True, fill=BOTH)

del_btn = Button(row4, text="⌫", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : delete(disp), fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=True, fill=BOTH)

btn0 = Button(row4, text="0", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('0', disp), fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=True, fill=BOTH)

equal_btn = Button(row4, text="=", font="segoe 14",bg = "yellow", relief=GROOVE, bd = 0, command=lambda : evaluate(disp), fg="black")
equal_btn.pack(side=LEFT, expand=True, fill=BOTH)

divide_btn = Button(row4, text="÷", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: insert_in_display('/', disp), fg="white", bg="#333333")
divide_btn.pack(side=LEFT, expand=True, fill=BOTH)



root.mainloop()
