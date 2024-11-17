from tkinter import *
import tkinter.messagebox
import math, re


def preprocess(expression):
    #  to replace 'n!' with 'factorial(n)'
    expression = re.sub(r'(\(.*\))!', r'factorial(round(\1))', expression)
    expression = re.sub(r'(\d+)!', r'factorial(\1)', expression)

    return expression

safe_env = {
    "__builtins__": None,  # Disable access to Python's built-in functions
    "sin": lambda x: math.sin(math.radians(x)),  
    "cos": lambda x: math.cos(math.radians(x)),  
    "tan": lambda x: math.tan(math.radians(x)),  
    "sinh": lambda x: math.degrees(math.asin(x)), 
    "cosh": lambda x: math.degrees(math.acos(x)), 
    "tanh": lambda x: math.degrees(math.atan(x)), 
    "sqrt": math.sqrt,
    "ln": math.log,      
    "log": math.log10,  
    "factorial": math.factorial,     

}

# function for inserting '0 - 9', '+', '-', '*', '/', '.' , '**', '(' , ')', '%' , 'cos', 'sin', 'tan', 'acos', 'asin', 'atan', 'e', 'pi'
def insert_in_display(value, disp):
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, value)


def evaluate(disp):
    try:
        result = disp.get()
        cleanedExpression = preprocess(result)
        result = eval(cleanedExpression, {"__builtins__": None}, safe_env)
        disp.delete(0, END)
        disp.insert(0, result)
    except Exception as e:
        tkinter.messagebox.showerror("Value Error!", f"Invalid input: {e}")



def delete(disp):
    pos = len(disp.get())
    display = str(disp.get())
    if display == '' or display == ' ':
        disp.insert(0, '0')
    else :
        disp.delete(0, END)
        disp.insert(0, display[0 : pos - 1])

def clear(disp):
    disp.delete(0, END)
    disp.insert(0, 0) 