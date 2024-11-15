from tkinter import *
root = Tk()

# {geometry -> 650x400} {location on x, y -> 300+300}
root.geometry("650x400+300+300")
root.title("Scientific Calculator")

# entry screen widget(for output)
disp = Entry(root, font = "Verdana 20", fg = "Black", bg = "mistyrose",bd = 4, justify=RIGHT ).pack(expand = True, fill = BOTH)


root.mainloop()