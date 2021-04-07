##################################
# IMPORTS
##################################
from tkinter import *

##################################
# VARIABLES
##################################

##################################
# CLASSES
##################################
class Board(Frame):
    # class variables

    # constructor
    def __init__(self, container):
        Frame.__init__(self, container)
        self.setupGUI()

    def setupGUI(self):
        # player display at top
        self.player1 = Label(self, text = "Player 1", font = ("@Malgun Gothic", 8), height = 5, width = 100, anchor = N, background = "white")
        self.player1.grid(row = 0, columnspan = 9)

        # border between player and board
        self.border1 = Label(self, height = 0, width = 86, anchor = N, background = "black")
        self.border1.grid(row = 1, columnspan = 9)

        # VERY ROUGH IMPLEMENTATION
        # change background color dep. on
        # ((col + offset)%2 == 0)
        # ex:
        # if ((col + offset)%2 == 0):
        #   background = "#451d1d"
        #   self.piece = Label(self, bg = background, ...)
        #   some code
        # display piece on board
        img = PhotoImage(file = "CHESS-PIECES/Chess_bdt60.png")
        self.piece = Label(self, image = img, height = 70, width = 70, bg = "#451d1d")
        self.piece.image = img
        self.piece.grid(row = 12, column = 4, rowspan = 1, columnspan = 1)

        # border between player and board
        self.border1 = Label(self, height = 0, width = 86, anchor = N, background = "black")
        self.border1.grid(row = 9, columnspan = 9)
        
        # player display at bottom
        self.player2 = Label(self, text = "Player 1", font = ("@Malgun Gothic", 8), height = 5, width = 100, anchor = S, background = "white")
        self.player2.grid(row = 10, columnspan = 9)

        # create a loop for rows
        for rows in range(1,9):
            # inner loop for columns
            for col in range(1,9):
                # variable to make checkboard look
                offset = 1

                # even rows 0-8
                if rows%2 == 0:
                    offset = 0

                # if the column is 1,3,5,7 and row is 0,2,4,6,8
                #m ake the box brown
                try:
                    if ((col + offset)%2 == 0):
                        self.box1 = Label(self,text="", height = 5, width = 10, background = "#451d1d")
                        self.box1.grid(row=rows,column=col)
                    else:
                        self.box1 = Label(self,text="", height = 5, width = 10, background = "#a47c48")
                        self.box1.grid(row=rows,column=col)
                except:
                    pass

        # packs into display
        self.pack()
##################################
# MAIN
##################################
# dimensions of board for pi screen
#WIDTH = 
#HEIGHT = 

# create the window
window = Tk()
#window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("CHESS")

# create an instance of board
b1 = Board(window)

# render the GUI in the mainloop
window.mainloop()
