###########################
# IMPORTS
###########################

# import
import copy
from tkinter import *

##################################
# CLASS
##################################
class Board(Frame):
    # class variables
    # 8x8 list initializing the board and initial location of pieces on
    # the board
    # the preceding letters B and W represent the colors lack and white for
    # players 1 and 2, respectively
    # R, KN, B, Q, K, and P represent the pieces rook, knight, bishop,
    # queen, king, and pawn, respectively
    chessBoard = [["BR", "BKN" , "BB", "BQ", "BK", "BB", "BKN", "BR"], 
                ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
                ["WR", "WKN", "WB", "WQ", "WK", "WB", "WKN", "WR"]]

    # constructor
    def __init__(self, container):
        Frame.__init__(self, container)
        self.setupGUI()

    # updates board after every move
    def calculateNextMove(chessBoard):
        # maintain the original board
        nextBoard = copy.deepcopy(board)
        for row in range(len(board)):
            for col in range(len(board[0])):
                # ********************SOME CODE THAT UPDATES COPY OF BOARD
                # TO THE BOARD WITH THE UPDATED MOVE OF PLAYER 1 OR 2********************
        return nextBoard

    def setupGUI(self):
    # create a loop for rows
        for rows in range(len(chessBoard)):
            # inner loop for columns
            for col in range(len(chessBoard[0])):
                # variable to make checkboard look
                offset = 0

                # even rows 0-8
                if rows%2 == 0:
                    offset = 1

                # if the column is 1, 3, 5, or 7 and row is 0, 2, 4, 6, or 8,
                # make the box brown
                try:
                    # chooses picture for occupation by piece -- or not -- on square on board
                    # ********************CHANGE "BOARD" TO THE UPADTED BOARD -- MAKE THIS RUN EVERY TURN********************                    if (board[row][col] == "BR"):

                    elif (board[row][col] == "BKN"):

                    elif (board[row][col] == "BB"):

                    elif (board[row][col] == "BQ"):

                    elif (board[row][col] == "BK"):

                    elif (board[row][col] == "BP"):

                    elif (board[row][col] == "WR"):

                    elif (board[row][col] == "WKN"):

                    elif (board[row][col] == "WB"):

                    elif (board[row][col] == "WQ"):

                    elif (board[row][col] == "WK"):

                    elif (board[row][col] == "WP"):

                    else:
                        img = PhotoImage(file = "CHESS-PIECES/onoccupied_square)
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
                    self.square.grid(row = rows+2, column = col, rowspawn = 1, columnspan = 1)
                except:
                    pass
      
