##################################
# IMPORTS
##################################

# import pieces, board, movement, player
from tkinter import *

#create tkinter object/window
#has to be created before the image objects below can be created in the Board class
window = Tk()

##################################
# IMPORTS
##################################
class Board(Frame):
    bsimg = PhotoImage(file="checkers-img/black_checker.png")
    rsimg = PhotoImage(file="checkers-img/red_checker.png")
    bkimg = PhotoImage(file="checkers-img/black_checker_double.png")
    rkimg = PhotoImage(file="checkers-img/red_checker_double.png")
    # class variables
    # 8x8 list initializing the board and initial location of pieces on
    # the board
    # the preceding letters B and R represent the colors black and red for
    # players 1 and 2, respectively
    # the letters S and D represent single and double pieces, respectively
    checkersBoard = [["BS", " ", "BS", " ", "BS", " ", "BS", " "],
                     [" ", "BS", " ", "BS", " ", "BS", " ", "BS"],
                     ["BS", " ", "BK", " ", "BS", " ", "BS", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", "RK", " ", "RS", " ", "RS", " ", "RS"],
                     ["RS", " ", "RS", " ", "RS", " ", "RS", " "],
                     [" ", "RS", " ", "RS", " ", "RS", " ", "RS"]]
    # current row and column of a given piece
    # set to 0 by default
    pieceRow = 0
    pieceCol = 0

    # constructor
    def __init__(self, container):
        Frame.__init__(self, container)
        #instance variables
        self.row = 0
        self.column = 0
        self.selected = (None, None)

        #functions to be ran at the beginnning of instantiation
        self.setupBoard()
        self.pack()
        self.selectPiece()

    #getter for row instance variable
    @property
    def row(self):
        return self._row

    #setter for row instance variable
    @row.setter
    def row(self, value):
        if (value<=7 and value>=0):
            self._row = value

    #getter for column instance variable
    @property
    def column(self):
        return self._column

    #setter for column instance variable
    @column.setter
    def column(self, value):
        if(value<=7 and value>=0):
            self._column = value

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
                        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="#451d1d")
                        self.box.image = self.bsimg
                        self.box.create_image(50, 50, anchor=CENTER, image=self.bsimg)
                        self.box.grid(row=rows, column=col)
                    elif (self.checkersBoard[rows][col] == "RS"):
                        #make a canvas(brown bg), place a red checker img in the canvas if it corresponds with the 2d list
                        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="#451d1d")
                        self.box.image = self.rsimg
                        self.box.create_image(50, 50, anchor=CENTER, image=self.rsimg)
                        self.box.grid(row=rows, column=col)
                    elif (self.checkersBoard[rows][col] == "BK"):
                        #make a canvas(brown bg), place a red checker img in the canvas if it corresponds with the 2d list
                        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="#451d1d")
                        self.box.image = self.bkimg
                        self.box.create_image(50, 50, anchor=CENTER, image=self.bkimg)
                        self.box.grid(row=rows, column=col)
                    elif (self.checkersBoard[rows][col] == "RK"):
                        #make a canvas(brown bg), place a red checker img in the canvas if it corresponds with the 2d list
                        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="#451d1d")
                        self.box.image = self.rkimg
                        self.box.create_image(50, 50, anchor=CENTER, image=self.rkimg)
                        self.box.grid(row=rows, column=col)
                    else:
                        # make a canvas(brown bg), these are empty squares
                        self.box = Canvas(self, height=100, width=100,highlightthickness=0, background="#451d1d")
                        self.box.grid(row=rows, column=col)

                #for tan squares although the checkers will never actually land on them....
                else:
                    self.box = Canvas(self, height=100, width=100, highlightthickness=0, background="#a47c48")
                    self.box.grid(row=rows, column=col)
                    #packing was removed so that we can add the selected board before packing later


    def selectPiece(self, selected=False):
        #setting up the board without packing it so that we can replace the selected box
        self.setupBoard()

        if (self.row %2==0 and self.column %2!=0):
            #where rows are even and columns are odd
            #create tan canvas
            currentbg = "#c1a071"
        elif(self.row %2!=0 and self.column %2==0):
            #where rows are odd and columns are even
            #create tan canvas
            currentbg = "#c1a071"
        else:
            #every other block
            #create brown canvas
            currentbg = "#bb5d5d"

        #set a new variable to the piece at current index
        piece = self.checkersBoard[self.row][self.column]

        #image variable set to corresponding image for the piece in the 2d list
        if (piece == "BS"):
            image = self.bsimg
        elif(piece == "BK"):
            image = self.bkimg
        elif(piece == "RS"):
            image = self.rsimg
        elif(piece == "RK"):
            image = self.rkimg
        else:
            image = None

        #replace the box
        self.box = Canvas(self, height=100, width=100, highlightthickness=0, background=currentbg)
        if(image != None):
            self.box.image = image
            self.box.create_image(50, 50, anchor=CENTER, image=image)
        self.box.grid(row=self.row,column=self.column)
        self.pack()
        #if enter is pressed, variable self.selected will be set to the current coordinate
        if (selected==True):
            
            self.selected = (self.row,self.column)
            
            #printing the coordinates
            print(self.selected)

            #printing what is in the 2D list at that coordinate!! (we can later use self.selected for movement algorithms!)
            print(self.checkersBoard[self.row][self.column])
            return self.row, self.column

    # updates and displays board after every move
    def calculateNextMove(self, rowy, coly, pieceType):
        # checks piece type
        if (pieceType == "BS"):
            if (rowy == 7):
                self.checkersBoard[rowy][coly], self.checkersBoard[self.pieceRow][self.pieceCol] = "BK", self.checkersBoard[rowy][coly]
        elif (pieceType == "RS"):
            if (rowy == 0):
                self.checkersBoard[rowy][coly], self.checkersBoard[self.pieceRow][self.pieceCol] = "RK", self.checkersBoard[rowy][coly]
        else:
            self.checkersBoard[rowy][coly], self.checkersBoard[self.pieceRow][self.pieceCol] = self.checkersBoard[self.pieceRow][self.pieceCol], self.checkersBoard[rowy][coly]
        # makes piece a double if it reaches opposite side of board
        self.setupBoard()

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

# movement via keys/GPIO input
def right(event):
    print("right key pressed")
    b1.column+=1
    print(b1.column)
    b1.selectPiece()

def left(event):
    print("left key pressed")
    b1.column-=1
    print(b1.column)
    b1.selectPiece()

def up(event):
    print("up key pressed")
    b1.row-=1
    print(b1.row)
    b1.selectPiece()

def down(event):
    print("down key pressed")
    b1.row+=1
    print(b1.row)
    b1.selectPiece()

# select current piece and store its position
def enter(event):
    print("enter key pressed")
    b1.pieceRow, b1.pieceCol = b1.selectPiece(True)

# select new position for the piece
# only move piece if the space is unoccupied and on red square
# needs range checking
def space(event):
    print("space key pressed")
    # new location of piece
    rowy, coly = b1.selectPiece(True)
    # check if space is unoccupied
    if (b1.checkersBoard[rowy][coly] == " "):
        # variable to make checkboard look
        offset = 1
        # even rows 0-8
        if rowy % 2 == 0:
            offset = 0
        # check if red square
        if ((coly + offset) % 2 == 0):
            # if the original piece is a black single
            if (b1.checkersBoard[b1.pieceRow][b1.pieceCol] == "BS"):
                # if row of new position is one below that of current one
                # and col of new position is to the left or right of current one
                if (((b1.pieceRow + 1) == rowy) and (((b1.pieceCol - 1) == coly) or ((b1.pieceCol + 1) == coly))):
                    # makes piece a double if it reaches opposite side of board
                    if (rowy == 7):
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = "BK", b1.checkersBoard[rowy][coly]
                    else:
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                    b1.setupBoard()   
                # capturing piece down 2 and to the right 2
                elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] == "RS" or "RK"):
                        b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied   
                    else:
                        return
                # capturing piece down 2 and to the left 2
                elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] == "RS" or "RK"):
                        b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied
                    else:
                        return
            elif (b1.checkersBoard[b1.pieceRow][b1.pieceCol] == "BK"):
                # if row of new position is one below or above that of current one
                # and col of new position is to the left or right of current one
                if (((b1.pieceRow - 1) == rowy) or ((b1.pieceRow + 1) == rowy) and (((b1.pieceCol - 1) == coly) or ((b1.pieceCol + 1) == coly))):
                    b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                    b1.setupBoard()
                # capturing piece down 2 and to the right 2
                elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] == "RS" or "RK"):
                        b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied   
                    else:
                        return
                # capturing piece down 2 and to the left 2
                elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] == "RS" or "RK"):
                        b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied
                    else:
                        return
                # capturing piece up 2 and to the right 2
                elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] == "RS" or "RK"):
                        b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied   
                    else:
                        return
                # capturing piece up 2 and to the left 2
                elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] == "RS" or "RK"):
                        b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied
                    else:
                        return
            # if the original piece is a red single
            elif (b1.checkersBoard[b1.pieceRow][b1.pieceCol] == "RS"):
                # if row of new position is one above that of current one
                # and col of new position is to the left or right of current one
                if (((b1.pieceRow - 1) == rowy) and (((b1.pieceCol - 1) == coly) or ((b1.pieceCol + 1) == coly))):
                    # makes piece a double if it reaches opposite side of board
                    if (rowy == 0):
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = "RK", b1.checkersBoard[rowy][coly]
                    else:
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                    b1.setupBoard()
                # capturing piece up 2 and to the right 2
                elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] == "BS" or "BK"):
                        b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied   
                    else:
                        return
                # capturing piece up 2 and to the left 2
                elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] == "BS" or "BK"):
                        b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied
                    else:
                        return
            elif (b1.checkersBoard[b1.pieceRow][b1.pieceCol] == "RK"):
                # if row of new position is one below or above that of current one
                # and col of new position is to the left or right of current one
                if (((b1.pieceRow - 1) == rowy) or ((b1.pieceRow + 1) == rowy) and (((b1.pieceCol - 1) == coly) or ((b1.pieceCol + 1) == coly))):
                    b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                    b1.setupBoard()
                # capturing piece down 2 and to the right 2
                elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] == "BS" or "BK"):
                        b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied   
                    else:
                        return
                # capturing piece down 2 and to the left 2
                elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] == "BS" or "BK"):
                        b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied
                    else:
                        return
                # capturing piece up 2 and to the right 2
                elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] == "BS" or "BK"):
                        b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied   
                    else:
                        return
                # capturing piece up 2 and to the left 2
                elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                    # if space between is occupied
                    if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] == "BS" or "BK"):
                        b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] = " "
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                    # if space between is unoccupied
                    else:
                        return
    else:
        print("Dumbass")

##################################
# MAIN
##################################
# dimensions of board for pi screen
# WIDTH =
# HEIGHT =

# binding the window to the functions for keyboard input above
window.bind("<Right>",right)
window.bind("<Left>",left)
window.bind("<Up>",up)
window.bind("<Down>",down)
window.bind("<Return>",enter)
window.bind("<space>",space)

# window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("CHECKERS")

# create an instance of board
b1 = Board(window)

# render the GUI in the mainloop
window.mainloop()

# create players 1 and 2
p1 = Player(0)
p2 = Player(1)
