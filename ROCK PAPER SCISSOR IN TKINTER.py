import time
from tkinter import *
from random import *
choices = ["rock","paper","scissor"]


def rock():
    computer = choice(choices)
    x = "rock"
    if computer == x:# 1 rock and 0  rock
        time.sleep(0.1)
        win_lose.after(10)
        win_lose.configure(text = f"tie\n||computer = {computer}|| PLAYER = {x}||".capitalize(),fg="light yellow")


    elif computer == "scissor":# 1 scissor and 0 rock
        time.sleep(0.1)
        win_lose.after(10)
        win_lose.configure(text = f"you win\n||computer = {computer}|| PLAYER = {x}||".capitalize(),fg="green")

    elif computer == "paper":
        time.sleep(0.1)
        win_lose.after(10)
        win_lose.configure(text = f"You lose\n||computer = {computer}|| PLAYER = {x}||".capitalize(),fg="red")


    pass
def paper():
    computer = choice(choices)
    x = "paper"
    if computer == x:# 1 paper and 0 paper
        time.sleep(0.1)
        win_lose.after(10)
        win_lose.configure(text = f"Tie\n||computer = {computer}|| PLAYER = {x}||".capitalize(),fg="light yellow")
    elif computer == "scissor":# 1 scissor and 0 paper

        time.sleep(0.1)
        win_lose.after(10)
        win_lose.configure(
            text=f"You lose\n||computer = {computer}|| PLAYER = {x}||".capitalize(), fg="red"
        )

    elif computer == "rock":
        time.sleep(0.1)
        win_lose.after(10)
        win_lose.configure(text = f"You lose\n||computer = {computer}|| PLAYER = {x}||".capitalize(),fg="green")

    pass

def scissor():

    computer = choice(choices)
    x = "scissor"
    if computer == x:  # 1 scissor and 0  scissor
        time.sleep(0.1)
        win_lose.after(10)
        win_lose.configure(text = f"Tie\n||computer = {computer}|| PLAYER = {x}||".capitalize(),fg="light yellow")
    elif computer == "rock":  # 1 scissor and 0 rock
        time.sleep(0.1)
        win_lose.after(10)
        win_lose.configure(text = f"You lose\n||computer = {computer}|| PLAYER = {x}||".capitalize(),fg="red")
    
    elif computer == "paper":
        time.sleep(0.1)
        win_lose.after(10)
        win_lose.configure(text = f"You Win\n||computer = {computer}|| PLAYER = {x}||".capitalize(),fg="green")
    pass


window = Tk()



window.geometry("450x400")
window.configure(background="black")
window.title("ROCK PAPER SCISSOR")
label_frame = Frame(window,bg = "black")
label_frame.grid(row = 0,column = 0)
label = Label(label_frame,text = "rps game".upper(),
              width= 16,font = ("ink free",13,"bold"),
              foreground="green",background="black")
label.grid(row = 0,column = 1,columnspan = 1)

i = 0

frame = Frame(window,bg = "black")
frame.grid(row = 1,column = 0)
button = Button(frame,text = choices[i],width= 5,height=2,
                background="grey",foreground="orange",
                    activeforeground="orange",activebackground="grey",command=rock)
button_2 = Button(frame,text = choices[i+1],width= 5,height=2,
                    background="grey",foreground="orange",
                    activeforeground="orange",activebackground="grey",command=paper)

button_3 = Button(frame,text = choices[i+2],width= 5,height=2,
                    background="grey",foreground="orange",
                    activeforeground="orange",activebackground="grey",command=scissor)


button.grid(row = 2,column = i)

button_2.grid(row = 2,column = i+1)

button_3.grid(row = 2, column = i+2)

win_lose = Label(frame,text = "WIN OR LOSE 😁",width = 30,font = ("ink free",12,"bold"),background="black",
              activebackground="black",foreground="cyan",activeforeground="cyan")
win_lose.grid(row = 4,column = 1)




window.mainloop()


