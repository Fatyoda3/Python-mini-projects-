# clock using python
from tkinter import *

from time import *

# (a for day name short) | (ims for time in h m s)
# after() can be used to call a function recursively
# %W week number for monday as first day %U for sunday
window = Tk()


def time_update():
    if f%2 ==0:

        time_text = strftime("%I:%M:%S %p")
    else :
        time_text = strftime("%H:%M:%S")


    time_label.configure(text= f"TIME is {time_text}")
    time_label.update()
    time_label.after(1000, time_update)


f = 0
def f_increase():
    global f

    f+=1



def date_update():
    date_text = strftime("%d-%m-%Y\n") # %d gives the date only like 26 %D give in dd/mm/yy %m
    # month %Y full year 2023
    date_label.configure(text=f"DATE is {date_text}")
    # date_label.after(1000, date_update)

def day_update():
    day_text = strftime("%A\n")
    day_label.configure(text = f'DAY is {day_text}')

    # day_label.after(1000, day_update)

counts_day_short_or_long = 0

counts_date = 0

time_format = 0
def day_short():
    global counts_day_short_or_long
    counts_day_short_or_long+=1
    day_text = strftime("%a")
    day_label.configure(text = f'DAY is {day_text}')

    if counts_day_short_or_long%2==0:
        day_update()



def date_short():
    global counts_date
    counts_date+=1
    date_text = strftime("%Y-%m-%d")
    date_label.configure(text = f'DATE is {date_text}',
                        activeforeground="light green",fg = "light green",
                        bg="black",activebackground="black")

    if counts_date%2==0:
        date_update()



window.title("CLOCK IN PYTHON")
window.geometry("450x170")
window.configure(bg = "black",highlightbackground="black")

i = 15
j = 2
k = 1
frame = Frame(window,bg = "black")
frame.grid(row= k+2,column = 5)

time_label = Button(frame,text = "time",font = ("ink free",13,"bold"),
                   fg = "light yellow",bg= "black",padx = i,pady = j,activebackground="black",
                    activeforeground= "light yellow",
                    height=2,width= 16,border=False,command=f_increase)
time_label.grid()

date_label = Button(text = "date",font = ("ink free",14,"bold"),
                   fg = "light green",bg= "black",padx = i,border=False,
                    activebackground="black",activeforeground="light green",
                    pady = j,height=2,command=date_short)
date_label.grid(row= k+ 3,column = 6)
"""zone = strftime("%z")
time_zone = Label(text = f"TIMEZONE {zone}",bg = "black",fg  = "yellow")
time_zone.grid(row = k,column = 2)"""
day_label = Button(text = "day",font = ("ink free",14,"bold"),
                  fg = "turquoise",bg= "black",padx = i,border=False,
                   activeforeground="turquoise",activebackground="black",
                   pady = j,height=2,command=day_short)
day_label.grid(row= k+4,column = 5)

day_update()
date_update()
time_update()
window.mainloop()
