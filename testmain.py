##################################
# IMPORTS
##################################

#import pieces, board, movement, player
from tkinter import *

##################################
# IMPORTS
##################################

class Board(Frame):
    # class variables
    # 8x8 list initializing the board and initial location of pieces on
    # the board
    # the preceding letters B and R represent the colors black and red for
    # players 1 and 2, respectively
    # the letters S and D represent single and double pieces, respectively
    checkersBoard = [["BS", " " , "BS", " ", "BS", "", "BS", ""], 
                [" ", "BS", " ", "BS", " ", "BS", " ", "BS"],
                ["BS", " ", "BS", " ", "BS", " ", "BS", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                ["RS", " " , "RS", " ", "RS", "", "RS", ""], 
                [" ", "RS", " ", "RS", " ", "RS", " ", "RS"],
                ["RS", " ", "RS", " ", "RS", " ", "RS", " "]]

    # constructor
    def __init__(self, container):
        Frame.__init__(self, container)
        self.setupGUI()

    def setupGUI(self):
    # create a loop for rows
        for rows in range(len(self.checkersBoard)):
            # inner loop for columns
            for col in range(len(self.checkersBoard[0])):
                # variable to make checkboard look
                offset = 0

                # even rows 0-8
                if rows%2 == 0:
                    offset = 1

                # if the column is 1, 3, 5, or 7 and row is 0, 2, 4, 6, or 8,
                # make the box brown
                    # chooses picture for occupation by piece -- or not -- on square on board
                    # ********************CHANGE "BOARD" TO THE UPADTED BOARD -- MAKE THIS RUN EVERY TURN********************                    if (board[row][col] == "BR"):

                    if (self.checkersBoard[rows][col] == "BS"):
                        img = PhotoImage(file = "checkers-images/black_checker.png")
                    elif (self.checkersBoard[rows][col] == "WS"):
                        img = PhotoImage(file = "checkers-images/red_checker.png")
                    else:
                        img = PhotoImage(file = "checkers-images/unoccupied_square.png")
                    # determines background color of square on board   
                    if ((col + offset)%2 == 0):
                        # self.square = Label(self, text = "", image = img, height = 70, width = 70, background = "#451d1d")
                        # self.square.grid(row = rows, column = col)
                        bkg = "#451d1d"
                    else:
                        # self.square = Label(self, text = "", image = img, height = 70, width = 70, background = "#a47c48")
                        # self.square.grid(row = rows, column = col)
                        bkg = "#a47c48"
                    # creates square
                    self.square = Label(self, text = "", image = img, height = 70, width = 70, background = bkg)
                    self.square.image = img
                    self.square.grid(row = rows, column = col, rowspan = 1, columnspan = 1)
        self.pack()
        #self.pack()

    # updates board after every move
    def calculateNextMove(chessBoard):
        # maintain the original board
        nextBoard = copy.deepcopy(board)
        for row in range(len(board)):
            for col in range(len(board[0])):
                # ********************SOME CODE THAT UPDATES COPY OF BOARD
                # TO THE BOARD WITH THE UPDATED MOVE OF PLAYER 1 OR 2********************
        return nextBoard
    
class Player():
    # constructor
    def __init__(self, number, pieceCount = 12):
        self.number = number
        self.pieceCount = pieceCount

    # accessor for number
    @property # says that an accessor/a getter follows
    def number(self):
        return self._number

    # mutator for number
    @number.setter # says that a mutator/setter follows
    def number(self, number):
        self._number = number

    # accessor for pieceCount
    @property # says that an accessor/a getter follows
    def pieceCount(self):
        return self._pieceCount

    # mutator for pieceCount
    @pieceCount.setter # says that a mutator/setter follows
    def pieceCount(self, pieceCount):
        if (pieceCount > 0):
            self._pieceCount = pieceCount

    # whenever a player loses a piece,
    # decrement counter for pieces
    def decrementPieceCount(self):
        self._pieceCount -= 1

##################################
# MAIN
##################################
# dimensions of board for pi screen
#WIDTH = 
#HEIGHT = 

# create the window
window = Tk()
#window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("CHECKERS")

# create an instance of board
b1 = Board(window)

# render the GUI in the mainloop
window.mainloop()

# create players 1 and 2
p1 = Player(0)
p2 = Player(1)
