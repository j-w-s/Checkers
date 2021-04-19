##################################
# IMPORTS
##################################

# import pieces, board, movement, player
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
    checkersBoard = [["BS", " ", "BS", " ", "BS", " ", "BS", " "],
                     [" ", "BS", " ", "BS", " ", "BS", " ", "BS"],
                     ["BS", " ", "BS", " ", "BS", " ", "BS", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", "RS", " ", "RS", " ", "RS", " ", "RS"],
                     ["RS", " ", "RS", " ", "RS", " ", "RS", " "],
                     [" ", "RS", " ", "RS", " ", "RS", " ", "RS"]]

    # constructor
    def __init__(self, container):
        Frame.__init__(self, container)
        self.setupBoard()
        #self.setupPieces()

    def setupBoard(self):
        for rows in range(len(self.checkersBoard)):
            # inner loop for columns
            for col in range(len(self.checkersBoard[0])):
                # variable to make checkboard look
                offset = 1

                # even rows 0-8
                if rows % 2 == 0:
                    offset = 0

                #if the column is 1,3,5,7 and row is 0,2,4,6,8
                #make the box brown


                #for brown squares
                if ((col + offset) % 2 == 0):
                    if (self.checkersBoard[rows][col] == "BS"):
                        # make a canvas(brown bg), place a black checker img in the canvas if it corresponds with the 2d list
                        self.bsimg = PhotoImage(file="checkers-img/black_checker.png")
                        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="#451d1d")
                        self.box.image = self.bsimg
                        self.box.create_image(50, 50, anchor=CENTER, image=self.bsimg)
                        self.box.grid(row=rows, column=col)

                    elif (self.checkersBoard[rows][col] == "RS"):
                        #make a canvas(brown bg), place a red checker img in the canvas if it corresponds with the 2d list
                        self.rsimg = PhotoImage(file="checkers-img/red_checker.png")
                        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="#451d1d")
                        self.box.image = self.rsimg
                        self.box.create_image(50, 50, anchor=CENTER, image=self.rsimg)
                        self.box.grid(row=rows, column=col)
                    else:
                        # make a canvas(brown bg), these are empty squares
                        self.box = Canvas(self, height=100, width=100,highlightthickness=0, background="#451d1d")
                        self.box.grid(row=rows, column=col)

                #for tan squares although the checkers will never actually land on them....
                else:
                    if (self.checkersBoard[rows][col] == "BS"):
                        # make a canvas(tan bg), place a black checker img in the canvas if it corresponds with the 2d list
                        img = PhotoImage(file="checkers-img/black_checker.png")
                        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="black")
                        self.box.grid(row=rows, column=col)
                    elif (self.checkersBoard[rows][col] == "WS"):
                        # make a canvas(tan bg), place a red checker img in the canvas if it corresponds with the 2d list
                        img = PhotoImage(file="checkers-img/red_checker.png")
                        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="red")
                        self.box.grid(row=rows, column=col)
                    else:
                        # make a canvas(tan bg), these are empty squares
                        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="#a47c48")
                        self.box.grid(row=rows, column=col)
        self.pack()


    def setupPieces(self):
        # create a loop for rows
        for row in range(len(self.checkersBoard)):
            # inner loop for columns
            for col in range(len(self.checkersBoard[row])):

                #set piece images based on checkerboard 2d list
                if (self.checkersBoard[row][col] == "BS"):
                    img = PhotoImage(file="checkers-img/black_checker.png")
                    self.box = Label(self, text="", height=50, width=50, background="#451d1d",image=img)
                    self.box.grid(row=row,column=col)
                elif (self.checkersBoard[row][col] == "WS"):
                    img = PhotoImage(file="checkers-img/red_checker.png")
                    self.box = Label(self, text="", height=50, width=50, background="#451d1d",image=img)
                    self.box.grid(row=row, column=col)
                else:
                    img = PhotoImage(file="checkers-img/unoccupied_square.png")
                    self.box = Label(self, text="", height=50, width=50, background="#451d1d", image=img)
                    self.box.grid(row=row, column=col)

        self.pack()
        # self.pack()

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
    def __init__(self, number, pieceCount=12):
        self.number = number
        self.pieceCount = pieceCount

    # accessor for number
    @property  # says that an accessor/a getter follows
    def number(self):
        return self._number

    # mutator for number
    @number.setter  # says that a mutator/setter follows
    def number(self, number):
        self._number = number

    # accessor for pieceCount
    @property  # says that an accessor/a getter follows
    def pieceCount(self):
        return self._pieceCount

    # mutator for pieceCount
    @pieceCount.setter  # says that a mutator/setter follows
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
# WIDTH =
# HEIGHT =

# create the window
window = Tk()

# window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("CHECKERS")

# create an instance of board
b1 = Board(window)


# render the GUI in the mainloop
window.mainloop()

# create players 1 and 2
p1 = Player(0)
p2 = Player(1)
