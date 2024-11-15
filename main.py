from tkinter import *
root = Tk()

# {geometry -> 650x400} {location on x, y -> 300+300}
root.geometry("650x400+300+300")
root.title("Scientific Calculator")

# entry screen widget(for output). We need this entry on root
disp = Entry(root, font = "Verdana 20", fg = "Black", bg = "mistyrose",bd = 4, justify=RIGHT ).pack(expand = True, fill = BOTH)

# buttons
# for button we need frames
row1 = Frame(root, bg = "#000000").pack(expand=TRUE, fill = BOTH)


# these buttons are in row1 frame
pibtn = Button(row1, text = "π", font = "segoe18", relief=GROOVE, fg = "white", bg = "#333333").pack(side = LEFT, expand=TRUE, fill = BOTH)

factbtn = Button(row1, text = "x!", font = "segoe18", relief=GROOVE, fg = "white", bg = "#333333").pack(side = LEFT, expand=TRUE, fill = BOTH)

sinbtn = Button(row1, text = "sin", font = "segoe18", relief=GROOVE, fg = "white", bg = "#333333").pack(side = LEFT, expand=TRUE, fill = BOTH)

cosbtn = Button(row1, text = "cos", font = "segoe18", relief=GROOVE, fg = "white", bg = "#333333").pack(side = LEFT, expand=TRUE, fill = BOTH)

btn1 = Button(row1, text = "1", font = "segoe18", relief=GROOVE, fg = "white", bg = "#333333").pack(side = LEFT, expand=TRUE, fill = BOTH)

btn2 = Button(row1, text = "2", font = "segoe18", relief=GROOVE, fg = "white", bg = "#333333").pack(side = LEFT, expand=TRUE, fill = BOTH)

btn3 = Button(row1, text = "3", font = "segoe18", relief=GROOVE, fg = "white", bg = "#333333").pack(side = LEFT, expand=TRUE, fill = BOTH)

plusBtn = Button(row1, text = "+", font = "segoe18", relief=GROOVE, fg = "white", bg = "#333333").pack(side = LEFT, expand=TRUE, fill = BOTH)

root.mainloop()