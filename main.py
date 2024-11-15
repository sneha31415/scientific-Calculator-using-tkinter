from tkinter import *
root = Tk()

# {geometry -> 650x400} {location on x, y -> 300+300}
root.geometry("650x400+300+300")
root.title("Scientific Calculator")

# entry screen widget(for output)
disp = Entry(root).pack(expand = True, fill = BOTH)


root.mainloop()