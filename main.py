import tkinter
from tkinter import scrolledtext
import get_title

def format_select():
    check = var.get()


def convert():
    url = url_form.get()
    summary.delete("0.0", tkinter.END) 
    summary.insert(tkinter.END,get_title.get_title(url,var.get())) 

def clear():
    url_form.delete(0,tkinter.END)
    summary.delete("0.0", tkinter.END)


# Generate Window
window = tkinter.Tk()
window.title('Tlooks url2form')
window.geometry('480x250')

# UI form
url_form = tkinter.Entry(width=60)
url_form.pack()

# Run Button
run_button = tkinter.Button(text='Run',width = 30,command=convert)
run_button.pack()

# clear Button
clear_button = tkinter.Button(text='Clear',width = 30,command=clear)
clear_button.pack()

# Output Entry
summary = scrolledtext.ScrolledText(
    width=60, 
    height=3)
summary.pack()

# format select
var = tkinter.IntVar()
var.set(0)
radio_0 = tkinter.Radiobutton(text='title only',value=0, variable=var, command=format_select)
radio_0.pack()
radio_1 = tkinter.Radiobutton(text='Author:"title",url,(yyyy,mm,dd閲覧)',value=1, variable=var, command=format_select)
radio_1.pack()
radio_2 = tkinter.Radiobutton(text='Author(Update Date).「title」.URL.(yyyy,mm,dd閲覧)',value=2, variable=var, command=format_select)
radio_2.pack()
radio_3 = tkinter.Radiobutton(text='HTML Format for Markdown(<a href="URL" title="title">title</a>)',value=3, variable=var, command=format_select)
radio_3.pack()



window.mainloop()
