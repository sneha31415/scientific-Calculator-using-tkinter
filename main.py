from tkinter import *
root = Tk()

# {geometry -> 650x400} {location on x, y -> 300+300}
root.geometry("650x400+300+300")
root.title("Scientific Calculator")

# Entry screen widget (for output)
disp = Entry(root, font="Verdana 20", fg="Black", bg="mistyrose", bd=4, justify=RIGHT)
disp.pack(expand=True, fill=BOTH)

# Frames for buttons
row1 = Frame(root, bg="#000000")
row1.pack(expand=True, fill=BOTH)

row2 = Frame(root, bg="#000000")
row2.pack(expand=True, fill=BOTH)

# Row 1 Buttons
pibtn = Button(row1, text="π", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
pibtn.pack(side=LEFT, expand=True, fill=BOTH)

factbtn = Button(row1, text="x!", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
factbtn.pack(side=LEFT, expand=True, fill=BOTH)

sinbtn = Button(row1, text="sin", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
sinbtn.pack(side=LEFT, expand=True, fill=BOTH)

cosbtn = Button(row1, text="cos", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
cosbtn.pack(side=LEFT, expand=True, fill=BOTH)

tanbtn = Button(row1, text="tan", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
tanbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn1 = Button(row1, text="1", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(row1, text="2", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(row1, text="3", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=True, fill=BOTH)

plusBtn = Button(row1, text="+", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
plusBtn.pack(side=LEFT, expand=True, fill=BOTH)

# Row 2 Buttons
e_btn = Button(row2, text="e", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
e_btn.pack(side=LEFT, expand=True, fill=BOTH)

sqrrootbtn = Button(row2, text="√x", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
sqrrootbtn.pack(side=LEFT, expand=True, fill=BOTH)

sinhbtn = Button(row2, text="sinh", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
sinhbtn.pack(side=LEFT, expand=True, fill=BOTH)

coshbtn = Button(row2, text="cosh", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
coshbtn.pack(side=LEFT, expand=True, fill=BOTH)

tanhbtn = Button(row2, text="tanh", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
tanhbtn.pack(side=LEFT, expand=True, fill=BOTH)

btn4 = Button(row2, text="4", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=True, fill=BOTH)

btn5 = Button(row2, text="5", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=True, fill=BOTH)

btn6 = Button(row2, text="6", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=True, fill=BOTH)

plusBtn2 = Button(row2, text="+", font="segoe18", relief=GROOVE, fg="white", bg="#333333")
plusBtn2.pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()
