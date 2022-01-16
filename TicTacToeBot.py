# Will Sheehan Tic tac toe bot
#Jan 9th 2022

#grid holding nine buttons, when clicked their text is changed to x
# after a button is clicked, another button's text is changed to o 

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import choice

root = Tk()
root.title('Tic Tac Toe Bot')
#root.geometry('1200x700')

#counts how many turns fro computer's sake
turn = 0

to_play = TRUE #makes sure computer only plays one move

clickedboxes = [] 

def notAvailableIndicies(clickedboxes):
    notAvailableSpots = []
    for box in clickedboxes:
        cell = 0
        row=(box.grid_info()['row']) #row can be 0-2
        col=(box.grid_info()['column']) #col can be 0-2
        if row==0:
            cell = 1 + col
        elif row==1:
            cell = 4 + col
        else:
            cell = 7 + col
        notAvailableSpots.append(cell-1)
    print(notAvailableSpots)
    return notAvailableSpots


#button clicked function
def b_click(b):
    global turn
    global to_play
    #b["text"] refers to text parameter of the button object
    if b["text"] == " ":
        b["text"] = "X"
        b["state"] = tk.DISABLED #buttons are disabled if an x or o is there
        turn += 1
        to_play = FALSE
        clickedboxes.append(b)
        computer_turn(turn, to_play)

def checkForWin(clickedboxes):



    messagebox.showinfo("Winner!", "You won the game" )

def lose():
    messagebox.showinfo("Loser", "You have been defeated")

def tie():
    messagebox.showinfo("Tie", "This game is a draw")




#build buttons that perform anonymous functions upon click (lambda)
b1 = Button(root, text=" ", font =('Helvetica', 20), height = 3, width = 6, bg = 'white', command = lambda: b_click(b1), state = tk.NORMAL) 
b2 = Button(root, text=" ", font =('Helvetica', 20), height = 3, width = 6, bg = 'white', command = lambda: b_click(b2), state = tk.NORMAL) 
b3 = Button(root, text=" ", font =('Helvetica', 20), height = 3, width = 6, bg = 'white', command = lambda: b_click(b3), state = tk.NORMAL) 

b4 = Button(root, text=" ", font =('Helvetica', 20), height = 3, width = 6, bg = 'white', command = lambda: b_click(b4), state = tk.NORMAL) 
b5 = Button(root, text=" ", font =('Helvetica', 20), height = 3, width = 6, bg = 'white', command = lambda: b_click(b5), state = tk.NORMAL) 
b6 = Button(root, text=" ", font =('Helvetica', 20), height = 3, width = 6, bg = 'white', command = lambda: b_click(b6), state = tk.NORMAL) 

b7 = Button(root, text=" ", font =('Helvetica', 20), height = 3, width = 6, bg = 'white', command = lambda: b_click(b7), state = tk.NORMAL) 
b8 = Button(root, text=" ", font =('Helvetica', 20), height = 3, width = 6, bg = 'white', command = lambda: b_click(b8), state = tk.NORMAL) 
b9 = Button(root, text=" ", font =('Helvetica', 20), height = 3, width = 6, bg = 'white', command = lambda: b_click(b9), state = tk.NORMAL) 


def computer_turn(turn, to_play):
    board = root.grid_slaves() #grid slaves gives me a list of the slaves of the grid [1]
    board.reverse() #to align indicies
    while to_play==FALSE:
#first move plays middle square else random
        if (b5["text"] == " " and turn == 1):
            board[4].configure(text = "O")
            board[4]["state"] = tk.DISABLED
            clickedboxes.append(b5)
            to_play = TRUE
        elif turn == 1:
            selects = choice([i for i in range(0,8) if i not in [4]])
            board[selects].configure(text = "O")
            board[selects]["state"] = tk.DISABLED
            clickedboxes.append((board[selects]))
            to_play = TRUE
        elif turn > 1: 
            # indicies of buttons in board array are 0-8, teherefore need random number 0-8
            notAvailableIndexs = notAvailableIndicies(clickedboxes)
            selects2 = choice([i for i in range(0,8) if i not in notAvailableIndexs])
            board[selects2].configure(text = "O")
            board[selects2]["state"] = tk.DISABLED
            clickedboxes.append((board[selects2]))
            to_play = TRUE

#grid button to the screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


root.mainloop()