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


# ---------Row 1 Buttons-----------
row1 = Frame(root, bg="#000000")
row1.pack(expand=True, fill=BOTH)

row1_mapping = {
    "π": math.pi,
    "x!": "!", 
    "sin": "sin",
    "cos": "cos",
    "tan": "tan",
    "1": "1",
    "2": "2",
    "3": "3",
    "+": "+"
}

for text, display in row1_mapping.items():
    Button(row1, text=text, font="segoe 14", relief=GROOVE, bd = 0, command = lambda display=display: insert_in_display(display, disp), fg="white", bg="#333333").pack(side=LEFT, expand=True, fill=BOTH)



# -----------Row 2 Buttons-----------
row2 = Frame(root, bg="#000000")
row2.pack(expand=True, fill=BOTH)

row2_mapping = {
    "e": math.e,
    "√x": "sqrt", 
    "sinh": "sinh",
    "cosh": "cosh",
    "tanh": "tanh",
    "4": "4",
    "5": "5",
    "6": "6",
    "-": "-"
}

for text, display in row2_mapping.items():
    Button(row2, text=text, font="segoe 14", relief=GROOVE, bd = 0, command = lambda display=display: insert_in_display(display, disp), fg="white", bg="#333333").pack(side=LEFT, expand=True, fill=BOTH)


#  -----------Row 3 Buttons-----------
row3 = Frame(root, bg="#000000")
row3.pack(expand=True, fill=BOTH)

row3_mapping = {
    "rad": "rad",  
    "1/x": "/",  
    "ln": "ln",  
    "log": "log",
    "x^y": "**", 
    "7": "7",
    "8": "8",
    "9": "9",
    "x": "*"  
}

for text, display in row3_mapping.items():
    Button(row3, text=text, font="segoe 14", relief=GROOVE, bd=0,
           command=lambda display=display: insert_in_display(display, disp),
           fg="white", bg="#333333").pack(side=LEFT, expand=True, fill=BOTH)


# ----------row 4 buttons----------
row4_mapping = {
    "mod": "%",
    "(": "(",
    ")": ")",
    ".": ".",
    "C": "clear",
    "⌫": "delete",
    "0": "0",
    "=": "evaluate",
    "/": "/"
}
row4 = Frame(root, bg="#000000")
row4.pack(expand=True, fill=BOTH)


for text, display in row4_mapping.items():
    bgColor = "#333333"
    fontColor = "white"
    
    if text == "=":
        bgColor = "yellow"
        fontColor = "black"
        command = lambda: evaluate(disp) 
    elif text == "C":
        command = lambda: clear(disp)  
    elif text == "⌫":
        command = lambda: delete(disp)  
    else:
        command = lambda display=display: insert_in_display(display, disp)  
    
    Button(row4, text=text, font="segoe 14", relief=GROOVE, bd=0,
           command=command, fg=fontColor, bg=bgColor).pack(side=LEFT, expand=True, fill=BOTH)


# mod_btn = Button(row4, text="mod", font="segoe 12", relief=GROOVE, bd = 0, command = lambda: insert_in_display('%', disp), fg="white", bg="#333333")
# mod_btn.pack(side=LEFT, expand=True, fill=BOTH)

# openbkt_btn = Button(row4, text="(", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display('(', disp), fg="white", bg="#333333")
# openbkt_btn.pack(side=LEFT, expand=True, fill=BOTH)

# closebkt_btn = Button(row4, text=")", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display(')', disp), fg="white", bg="#333333")
# closebkt_btn.pack(side=LEFT, expand=True, fill=BOTH)

# dot_btn = Button(row4, text=".", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : insert_in_display('.', disp), fg="white", bg="#333333")
# dot_btn.pack(side=LEFT, expand=True, fill=BOTH)

# clearbtn = Button(row4, text="C", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: clear(disp), fg="white", bg="#333333")
# clearbtn.pack(side=LEFT, expand=True, fill=BOTH)

# del_btn = Button(row4, text="⌫", font="segoe 14", relief=GROOVE, bd = 0, command = lambda : delete(disp), fg="white", bg="#333333")
# del_btn.pack(side=LEFT, expand=True, fill=BOTH)

# btn0 = Button(row4, text="0", font="segoe 14", relief=GROOVE, bd = 0, command= lambda: insert_in_display('0', disp), fg="white", bg="#333333")
# btn0.pack(side=LEFT, expand=True, fill=BOTH)

# equal_btn = Button(row4, text="=", font="segoe 14",bg = "yellow", relief=GROOVE, bd = 0, command=lambda : evaluate(disp), fg="black")
# equal_btn.pack(side=LEFT, expand=True, fill=BOTH)

# divide_btn = Button(row4, text="/", font="segoe 14", relief=GROOVE, bd = 0, command = lambda: insert_in_display('/', disp), fg="white", bg="#333333")
# divide_btn.pack(side=LEFT, expand=True, fill=BOTH)



root.mainloop()
