from tkinter import *
from tkinter import messagebox
from datetime import date 
from tkinter.ttk import Combobox
import pyrecord, pycategory
def init_money_upgrade():   
    t = init_money_entry.get()
    try:
        if int(t) == records._initial_money:
            return
        if messagebox.askquestion("WARNING", "Are you sure to update \nthe init money?"):
            global sum, changed
            sum = int(t)
            records._initial_money = int(t)
            for i in records._records:
                sum += int(i.amount)
            cur_money_lb.config(text = f"Now you have {sum} money.")
            changed = True
    except:
        messagebox.showwarning("FAIL", "The format of initial money is invalid!")
def add_record():
    a = date_entry.get()
    b1 = category_entry.get()
    b2 = ''
    for i in b1:
        if i.isalpha():
            b2 += i
    c = description_entry.get()
    d = amount_entry.get()
    try:
        date.fromisoformat(a)
    except:
        messagebox.showwarning("FAIL", "The format of date is invalid!\nIt should be YYYY/MM/DD\nTry again!")
        return
    try:
        assert categories.is_category_valid(b2) == True
    except:
        messagebox.showwarning("FAIL", "The format of category is invalid!\nTry again!")
        return
    for i in c:
        if i == ' ':
            messagebox.showwarning("FAIL", "The description should not contain space!\nTry again!")
            return
    try:
        int(d)
    except:
        messagebox.showwarning("FAIL", "The format of amount is invalid!\nTry again!")
        return
    messagebox.showinfo("SUCCESS", "Add Successfully!")
    records.add(a, b2, c, d)
    global sum, changed
    tmp_str = a + ' '*15
    tmp_str += b2 + " "*(30-len(b2))
    tmp_str += c + " "*(30-len(c))
    tmp_str += d + " "*(30-len(d))
    sum += int(d)
    changed = True
    my_listbox.insert("end", tmp_str)
    cur_money_lb.config(text = f"Now you have {sum} money.")
def delete_item():
    try:
        global sum
        selected_item = my_listbox.selection_get()
        for cnt, i in enumerate(records._records):
            tmp_str = i.date + ' '*15
            tmp_str += i.category + " "*(30-len(i.category))
            tmp_str += i.item + " "*(30-len(i.item))
            tmp_str += i.amount + " "*(30-len(i.amount))
            if(tmp_str == selected_item):
                if messagebox.askokcancel("WARNING", f"Are you sure to delete\n[({i.date}) {i.category} {i.item} {i.amount}]?"):
                    sum-=int(i.amount)
                    records.delete(cnt)
                    cur_money_lb.config(text = f"Now you have {sum} money.")
                    my_listbox.delete(cnt)
                    global changed
                    changed = True
                    return
    except:
        pass
def find_specific_category():
    a = find_category_entry.get()
    if not a:
        return
    find_ls = categories.find_subcategories(a)
    my_listbox.delete(0, END)
    sum_tmp = 0
    for i in records._records:
        if i.category in find_ls:
            tmp_str = i.date + ' '*15
            tmp_str += i.category + " "*(30-len(i.category))
            tmp_str += i.item + " "*(30-len(i.item))
            tmp_str += i.amount + " "*(30-len(i.amount))
            sum_tmp += int(i.amount)
            my_listbox.insert("end", tmp_str)
    cur_money_lb.config(text = f"Total amount above is {sum_tmp} dollars.")
def reset_origin():
    my_listbox.delete(0, END)
    for i in records._records:
        tmp_str = i.date + ' '*15
        tmp_str += i.category + " "*(30-len(i.category))
        tmp_str += i.item + " "*(30-len(i.item))
        tmp_str += i.amount + " "*(30-len(i.amount))
        my_listbox.insert("end", tmp_str)
    cur_money_lb.config(text = f"Now you have {sum} money.")
def on_closing():
    if not changed:
        win.destroy()
        return
    if messagebox.askquestion("QUIT", "Do you want to save the changes?"):
        records.save()
        win.destroy()
    else:
        pass
categories = pycategory.Categories()
records = pyrecord.Records(categories)
cates = categories.view()
win = Tk()
win.geometry("800x300+400+300")
# win.config(bg = "white")
win.resizable(False, False)
win.title("PyMoney") 

sum = records._initial_money
changed = False
add_record_btn = Button(text = "Add a record", width=15, height=1, bg = "lightgray", font = "10", command = add_record)
find_category_btn = Button(text = "Find", width=5, height=1, bg = "lightgray", command = find_specific_category)
reset_btn = Button(text = "Reset", width=5, height=1, bg = "lightgray", command = reset_origin)
delete_btn = Button(text = "Delete", width=5, height=1, bg = "lightgray", font = "10", command = delete_item)
update_btn = Button(text = "Update", width=8, height=1, bg = "lightgray", command = init_money_upgrade)
add_record_btn.place(x = 640, y = 250)
find_category_btn.place(x = 360, y = 2)
reset_btn.place(x = 410, y = 2)
delete_btn.place(x = 370, y = 260)
update_btn.place(x = 720, y = 120)

date_lb = Label(text = "Date", font = " 10")
myID = Label(text = "PYMONEY", font=("Helvetica", 36, "bold"))
category_lb = Label(text = "Category", font = " 10")
description_lb = Label(text = "Description", font = " 10")
amount_lb = Label(text = "Amount", font = " 10")
find_category_lb = Label(text = "Find category", font = " 10")
init_money_lb = Label(text = "Initial money", font = " 10")

date_lb.place(x = 520, y = 160)
category_lb.place(x = 510, y = 180)
description_lb.place(x = 505, y = 200)
amount_lb.place(x = 510, y = 220)
find_category_lb.place(x = 0, y = 0)
init_money_lb.place(x = 490, y = 95)
myID.place(x = 500, y = 15)


default_date = StringVar()
default_date.set(date.today())
date_entry = Entry(textvariable=default_date)
category_entry = Combobox(win)
category_entry['values'] = cates
description_entry = Entry()
amount_entry = Entry()
find_category_entry = Entry()
default_init_money = StringVar()
default_init_money.set(str(records._initial_money))
init_money_entry = Entry(textvariable=default_init_money)
date_entry.place(x = 585, y=162, width = 200)
category_entry.place(x = 585, y=182, width = 200)
description_entry.place(x = 585, y=202, width = 200)
amount_entry.place(x = 585, y=222, width = 200)
find_category_entry.place(x = 100, y=5, width = 250)
init_money_entry.place(x = 585, y=97, width = 200)

my_scrollbar = Scrollbar(win)
my_scrollbar.place(x = 435, y = 35, height=220)
my_listbox = Listbox(win, yscrollcommand=my_scrollbar.set)
for i in records._records:
    tmp_str = i.date + ' '*15
    tmp_str += i.category + " "*(30-len(i.category))
    tmp_str += i.item + " "*(30-len(i.item))
    tmp_str += i.amount + " "*(30-len(i.amount))
    sum += int(i.amount)
    my_listbox.insert("end", tmp_str)
cur_money_lb = Label(text = f"Now you have {sum} money.", font = "20")
cur_money_lb.place(x = 5, y = 265)
my_listbox.place(x = 5, y= 35, width = 430, height = 220)
my_scrollbar.config(command=my_listbox.yview)
win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()