# Importing the modules
import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox
from tkinter import ttk

# Initializing global unit selections
result_from = ""
result_to = ""

# Creating the window
window = tk.Tk()
window.geometry('500x600')
window.title('Unit Converter')
window.configure(bg='gray')

# Creating fonts
font1 = font.Font(family='helvetica', size='30')
font2 = font.Font(family='helvetica', size='15')
font3 = font.Font(family='helvetica', size='20')

# The text variable
number_from = tk.StringVar()

# The answer function
def compute_answer(n1):
    global result_from, result_to
    num1 = n1.get()
    try:
        number1 = float(num1)
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid number.')
        return

    if result_from == 'Cubic meters' and result_to == 'Cubic meters':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic meters' and result_to == 'Cubic foot':
        calculate = number1*35.3147
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic meters' and result_to == 'Liters':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic meters' and result_to == 'Gallons':
        calculate = number1*264.172
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic meters' and result_to == 'Cubic Centimeters':
        calculate = number1*1000000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")  

    elif result_from == 'Cubic foot' and result_to == 'Cubic meters':
        calculate = number1*0.02831
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic foot' and result_to == 'Cubic foot':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic foot' and result_to == 'Liters':
        calculate = number1*28.3168
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic foot' and result_to == 'Gallons':
        calculate = number1*7.4805
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic foot' and result_to == 'Cubic Centimeters':
        calculate = number1*28316.8
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Liters' and result_to == 'Cubic meters':
        calculate = number1*0.001
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Liters' and result_to == 'Cubic foot':
        calculate = number1*0.0353147
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Liters' and result_to == 'Liters':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Liters' and result_to == 'Gallons':
        calculate = number1*0.264172
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Liters' and result_to == 'Cubic Centimeters':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Gallons' and result_to == 'Cubic meters':
        calculate = number1*0.00378541
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Gallons' and result_to == 'Cubic foot':
        calculate = number1*0.133681
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Gallons' and result_to == 'Liters':
        calculate = number1*3.78541
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Gallons' and result_to == 'Cubic Centimeters':
        calculate = number1*3785.41
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic Centimeters' and result_to == 'Cubic meters':
        calculate = number1*0.000001
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic Centimeters' and result_to == 'Cubic foot':
        calculate = number1*0.0000353147
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic Centimeters' and result_to == 'Liters':
        calculate = number1*0.001
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic Centimeters' and result_to == 'Gallons':
        calculate = number1*0.000264172
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Cubic Centimeters' and result_to == 'Cubic Centimeters':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Millimeters' and result_to == 'Centimeters':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Millimeters' and result_to == 'Millimeters':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Millimeters' and result_to == 'Centimeters':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Millimeters' and result_to == 'Decimeters':
        calculate = number1 / 100
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Millimeters' and result_to == 'Meters':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Millimeters' and result_to == 'Kilometers':
        calculate = number1 / 1e6
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centimeters' and result_to == 'Millimeters':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centimeters' and result_to == 'Centimeters':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centimeters' and result_to == 'Decimeters':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centimeters' and result_to == 'Meters':
        calculate = number1 / 100
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centimeters' and result_to == 'Kilometers':
        calculate = number1 / 100000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decimeters' and result_to == 'Millimeters':
        calculate = number1 * 100
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decimeters' and result_to == 'Centimeters':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decimeters' and result_to == 'Decimeters':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decimeters' and result_to == 'Meters':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decimeters' and result_to == 'Kilometers':
        calculate = number1 / 10000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Meters' and result_to == 'Millimeters':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Meters' and result_to == 'Centimeters':
        calculate = number1 * 100
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Meters' and result_to == 'Decimeters':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Meters' and result_to == 'Meters':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Meters' and result_to == 'Kilometers':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilometers' and result_to == 'Millimeters':
        calculate = number1 * 1e6
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilometers' and result_to == 'Centimeters':
        calculate = number1 * 100000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilometers' and result_to == 'Decimeters':
        calculate = number1 * 10000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilometers' and result_to == 'Meters':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilometers' and result_to == 'Kilometers':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")
    
    elif result_from == 'Milligrams' and result_to == 'Milligrams':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Milligrams' and result_to == 'Centigrams':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Milligrams' and result_to == 'Grams':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Milligrams' and result_to == 'Decigrams':
        calculate = number1 / 100
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Milligrams' and result_to == 'Kilograms':
        calculate = number1 / 1e6
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centigrams' and result_to == 'Milligrams':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centigrams' and result_to == 'Centigrams':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centigrams' and result_to == 'Grams':
        calculate = number1 / 100
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centigrams' and result_to == 'Decigrams':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Centigrams' and result_to == 'Kilograms':
        calculate = number1 / 100000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Grams' and result_to == 'Milligrams':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Grams' and result_to == 'Centigrams':
        calculate = number1 * 100
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Grams' and result_to == 'Grams':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Grams' and result_to == 'Decigrams':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Grams' and result_to == 'Kilograms':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decigrams' and result_to == 'Milligrams':
        calculate = number1 * 100
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decigrams' and result_to == 'Centigrams':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decigrams' and result_to == 'Grams':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decigrams' and result_to == 'Decigrams':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Decigrams' and result_to == 'Kilograms':
        calculate = number1 / 10000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilograms' and result_to == 'Milligrams':
        calculate = number1 * 1e6
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilograms' and result_to == 'Centigrams':
        calculate = number1 * 100000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilograms' and result_to == 'Grams':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilograms' and result_to == 'Decigrams':
        calculate = number1 * 10000
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")

    elif result_from == 'Kilograms' and result_to == 'Kilograms':
        calculate = number1
        result.cget('text')
        result.configure(text = f"{calculate} {result_to}")




# Fromfunc function
def fromfunc(event):
    global result_from
    result_from = event.widget.get()

# Tofunc function
def tofunc(event):
    global result_to
    result_to = event.widget.get()

# Unit selection function
def selected(event):
    unit = event.widget.get()
    if unit == 'Volume':
        values = ('Cubic meters', 'Cubic foot', 'Liters', 'Gallons', 'Cubic Centimeters')
    elif unit == 'Length':
        values = ('Millimeters', 'Centimeters', 'Decimeters', 'Meters', 'Kilometers')
    elif unit == 'Mass':
        values = ('Milligrams', 'Centigrams', 'Grams', 'Decigrams', 'Kilograms')
    else:
        values = ()

    fromdd['values'] = values
    todd['values'] = values

# Creating the UI components
main = tk.Label(window, text='Unit Converter', bg='gray', fg='blue')
main['font'] = font1
main.place(relx=0.53, rely=0.1, anchor='center')

unit = tk.Label(window, text='Unit -:', bg='gray')
unit['font'] = font2
unit.place(relx=0.20, rely=0.28)

n = tk.StringVar()
unitdd = ttk.Combobox(window, width=35, textvariable=n)
unitdd['values'] = ('Volume', 'Length', 'Mass')
unitdd.place(relx=0.57, rely=0.3, anchor='center')
unitdd.bind('<<ComboboxSelected>>', selected)

label_from = tk.Label(window, text='From -:', bg='gray')
label_from['font'] = font2
label_from.place(relx=0.20, rely=0.37)

f = tk.StringVar()
fromdd = ttk.Combobox(window, width=35, textvariable=f)
fromdd.place(relx=0.57, rely=0.39, anchor='center')
fromdd.bind('<<ComboboxSelected>>', fromfunc)

num_from = tk.Entry(window, width=15, textvariable=number_from)
num_from.place(relx=0.46, rely=0.52)

to = tk.Label(window, text='Type Here', bg='gray')
to['font'] = font2
to.place(relx=0.26, rely=0.51)

# Wrap the function with partial to pass the entry box
get_result = partial(compute_answer, num_from)

to = tk.Label(window, text='To -:', bg='gray')
to['font'] = font2
to.place(relx=0.20, rely=0.45)

t = tk.StringVar()
todd = ttk.Combobox(window, width=35, textvariable=t)
todd.place(relx=0.57, rely=0.47, anchor='center')
todd.bind('<<ComboboxSelected>>', tofunc)

result = tk.Label(window, text='', bg='white', width=20)
result['font'] = font3
result.place(relx=0.21, rely=0.6)

get_answer = tk.Button(window, text='Get Answer', bg='coral', command=get_result)
get_answer['font'] = font2
get_answer.place(relx=0.43, rely=0.75)

art = tk.Label(window, text='Tharshan', bg='gray', fg='blue')
art['font'] = font3
art.place(relx=0.42, rely=0.9)

# Mainloop
window.mainloop()
