import tkinter
import get_title

def format_select():
    check = var.get()

    if check == 1:
        radio_2.configure(state='normal')
        radio_3.configure(state='normal')

    elif check == 2:
        radio_1.configure(state='normal')
        radio_3.configure(state='normal')

    elif check == 3:
        radio_1.configure(state='normal')
        radio_2.configure(state='normal')

def convert():
    url = url_form.get()
    summary.insert(tkinter.END,get_title.get_title(url))

# Generate Window
window = tkinter.Tk()
window.title('Tlooks url2form')
window.geometry('480x200')

# UI form
url_form = tkinter.Entry(width=60)
url_form.pack()

# Run Button
run_button = tkinter.Button(text='Run',width = 30,command=convert)
run_button.pack()

# Output Entry
summary = tkinter.Entry(width=60)
summary.pack()

# format select
var = tkinter.IntVar()
var.set(1)
radio_1 = tkinter.Radiobutton(text='Author:"title",url,(yyyy,mm,dd閲覧)',value=1, variable=var, command=format_select)
radio_1.pack()
radio_2 = tkinter.Radiobutton(text='Author(Update Date).「title」.URL.(yyyy,mm,dd閲覧)',value=2, variable=var, command=format_select)
radio_2.pack()
radio_3 = tkinter.Radiobutton(text='HTML Format for Markdown(<a href="URL" title="title">title</a>)',value=3, variable=var, command=format_select)
radio_3.pack()



window.mainloop()
