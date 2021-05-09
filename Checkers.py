##################################
# IMPORTS AND MISC. VARIABLES
##################################

# imports
from tkinter import *
import RPi.GPIO as GPIO
from time import sleep
import copy
import sys

GPIO.setwarnings(False)

# create tkinter object/window
window = Tk()

##################################
# CLASSES
##################################
# class for Checkers board and misc. class functions
class Board(Frame):
    # class variables
    # images for black and red singles and doubles
    bsimg = PhotoImage(file="checkers-img/black_checker.png")
    rsimg = PhotoImage(file="checkers-img/red_checker.png")
    bkimg = PhotoImage(file="checkers-img/black_checker_double.png")
    rkimg = PhotoImage(file="checkers-img/red_checker_double.png")
    
    # 8x8 list initializing the board and initial location of pieces on
    # the board
    # the preceding letters B and R represent the colors black and red for
    # players 1 and 2, respectively
    # the letters S and K represent single and double (king) pieces, respectively
    checkersBoard = [["BS", " ", "BS", " ", "BS", " ", "BS", " "],
                     [" ", "BS", " ", "BS", " ", "BS", " ", "BS"],
                     ["BS", " ", "BS", " ", "BS", " ", "BS", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", "RS", " ", "RS", " ", "RS", " ", "RS"],
                     ["RS", " ", "RS", " ", "RS", " ", "RS", " "],
                     [" ", "RS", " ", "RS", " ", "RS", " ", "RS"]]
    
    # current row and column of a given piece
    # set to 0 by default
    pieceRow = 0
    pieceCol = 0

    # constructor
    def __init__(self, container):
        Frame.__init__(self, container)
        # instance variables
        self.row = 0
        self.column = 0
        self.selected = (0, 0)
        self.setupBoard()

    # accessor for row
    @property # says that an accessor/a getter follows
    def row(self):
        return self._row

    # mutator for row instance variable
    @row.setter # says that a mutator/setter follows
    def row(self, value):
        if (value<=7 and value>=0): # range checking
            self._row = value

    # accessor for column
    @property # says that an accessor/a getter follows
    def column(self):
        return self._column

    # mutator for column
    @column.setter # says that a mutator/setter follows
    def column(self, value):
        if(value<=7 and value>=0):# range checking
            self._column = value
            
    # class method creating visual display of checkers board
    def setupBoard(self):
        # deletes leftover widgets/canvases
        for widget in Frame.winfo_children(self):
            widget.destroy()
        # loop for rows of checkers board
        for rows in range(len(self.checkersBoard)):
            
            # inner loop for columns of checkers board
            for col in range(len(self.checkersBoard[0])):
            
                # variable to make checkboard look
                offset = 1

                # even rows 0-8
                if (rows % 2 == 0):
                    offset = 0

                # if the column is 1,3,5,7 and row is 0,2,4,6,8,
                # make the square brown

                # for brown squares
                if ((col + offset) % 2 == 0):
                    if (self.checkersBoard[rows][col] == "BS"):
                        # make a canvas (brown bg) and place a black checker img in the canvas
                        self.box = Canvas(self, height=60, width=60, highlightthickness=0, background="#451d1d")
                        self.box.image = self.bsimg
                        self.box.create_image(30, 30, anchor=CENTER, image=self.bsimg)
                        self.box.grid(row=rows, column=col)
                    elif (self.checkersBoard[rows][col] == "RS"):
                        # make a canvas (brown bg) and place a red checker img in the canvas
                        self.box = Canvas(self, height=60, width=60, highlightthickness=0, background="#451d1d")
                        self.box.image = self.rsimg
                        self.box.create_image(30, 30, anchor=CENTER, image=self.rsimg)
                        self.box.grid(row=rows, column=col)
                    elif (self.checkersBoard[rows][col] == "BK"):
                        # make a canvas (brown bg) and place a black checker img in the canvas
                        self.box = Canvas(self, height=60, width=60, highlightthickness=0, background="#451d1d")
                        self.box.image = self.bkimg
                        self.box.create_image(30, 30, anchor=CENTER, image=self.bkimg)
                        self.box.grid(row=rows, column=col)
                    elif (self.checkersBoard[rows][col] == "RK"):
                        # make a canvas (brown bg) and place a red checker img in the canvas
                        self.box = Canvas(self, height=60, width=60, highlightthickness=0, background="#451d1d")
                        self.box.image = self.rkimg
                        self.box.create_image(30, 30, anchor=CENTER, image=self.rkimg)
                        self.box.grid(row=rows, column=col)
                    else:
                        # make a canvas (brown bg); these are empty squares
                        self.box = Canvas(self, height=60, width=60,highlightthickness=0, background="#451d1d")
                        self.box.grid(row=rows, column=col)

                # for tan, unoccupied squares on the board
                else:
                    self.box = Canvas(self, height=60, width=60, highlightthickness=0, background="#a47c48")
                    self.box.grid(row=rows, column=col)

        #adds a black bar at the bottom
        for i in range(1,6):
            for j in range(8):
                self.border = Canvas(self, height=60,width=60,highlightthickness = 0, background="black")
                self.border.grid(row=rows+i,column=col-j)

        self.pack()

    # class method that resets the board and restores players' pieces to 12
    def resetBoard(self):
        self.checkersBoard = originalBoard
        p1.pieceCount = 12
        p2.pieceCount = 12
        # cursor is moved to (0, 0) on board
        self.row, self.column = 0, 0
        # resets player turn to 0 in case red wins
        Player.playerTurn = 0

    # class method selecting pieces on the board
    def selectPiece(self, selected = False):
        # sets board up without packing it
        self.setupBoard()

        if (self.row %2==0 and self.column %2!=0):
            # where rows are even and columns are odd,
            # create tan canvas
            currentbg = "#c1a071"

        elif(self.row %2!=0 and self.column %2==0):
            # where rows are odd and columns are even,
            # create tan canvas
            currentbg = "#c1a071"
            
        else:
            # everywhere else,
            # create brown canvas
            currentbg = "#bb5d5d"

        # instantiates a piece variable storing the piece stored at location (self.row, self.column) on board
        piece = self.checkersBoard[self.row][self.column]

        # sets image variable to image corresponding to piece (above)
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

        # replaces the square
        self.box = Canvas(self, height=60, width=60, highlightthickness=0, background=currentbg)
        if (image != None):
            self.box.image = image
            self.box.create_image(30, 30, anchor=CENTER, image=image)
        self.box.grid(row=self.row,column=self.column)
        
        # if enter is pressed, variable self.selected will be set to the current coordinates of selected piece
        if (selected == True):
            self.selected = (self.row, self.column)
            return self.row, self.column

# class for players of game (Checkers)
class Player():
    # class variables
    # when playerTurn == 0, player 1's turn
    # when playerTurn == 1, player 2's turn
    playerTurn = 0
    
    # constructor
    def __init__(self, number, pieceCount=12):
        # instance variables
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
        if (pieceCount > 0): # range checking
            self._pieceCount = pieceCount

    # whenever a player loses a piece,
    # decrements counter for pieces
    def decrementPieceCount(self):
        if (self.pieceCount-1 > 0):
            self.pieceCount -= 1
        else:
            b1.resetBoard()

# create player instances 1 and 2 (black and red)
p1 = Player(0)
p2 = Player(1)

##################################
# FUNCTIONS
##################################
# function for capture piece as a black single
def capturePieceBlackSingle(rowy, coly):
    b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
    # makes piece a double if it reaches opposite side of board
    if (rowy == 7):
        b1.checkersBoard[rowy][coly] = "BK"
    b1.setupBoard()
    p2.decrementPieceCount()

# function for capture piece as a black double
def capturePieceBlackKing(rowy, coly):
    b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] = " "
    b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
    b1.setupBoard()
    p2.decrementPieceCount()
    
# function for capture piece as a red single        
def capturePieceRedSingle(rowy, coly):
    b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
    # makes piece a double if it reaches opposite side of board
    if (rowy == 0):
        b1.checkersBoard[rowy][coly] = "RK"
    b1.setupBoard()
    p1.decrementPieceCount()

# function for capture piece as a red double
def capturePieceRedKing(rowy, coly):
    b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] = " "
    b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
    b1.setupBoard()
    p1.decrementPieceCount()

##################################
# movement via keys/GPIO input
##################################
#creates events to bind buttons and joystick to window
def joystickEvent(window, joystick):
    window.event_generate('<<joystick{}>>'.format(joystick))
        
def button1Event(window,button):
    window.event_generate('<<button{}>>'.format(button))

#when called quits the window
def quits(event):
    window.destroy()

#when called resets the board
def reset(event):
    b1.resetBoard()

# function for handling input of right joystick
def right(event):
    b1.column+=1
    b1.selectPiece()

# function for handling input of left joystick
def left(event):
    b1.column-=1
    b1.selectPiece()

# function for handling input of up joystick
def up(event):
    b1.row-=1
    b1.selectPiece()

# function for handling input of down joystick
def down(event):
    b1.row+=1
    b1.selectPiece()

# function for handling input of return/enter key
# selects current piece and stores its position
def button1(event):
    GPIO.output(leds[0],1)
    b1.pieceRow, b1.pieceCol = b1.selectPiece(True)
    sleep(.1)
    GPIO.output(leds[0],0)

# function for handling input of space key
# selects new position for the piece selected by return/enter key
# only moves piece if the space is unoccupied and on red square
# includes range checking and allows pieces to be captured/doubled
def button2(event):
    GPIO.output(leds[1],1)
    # new location of piece
    rowy, coly = b1.selectPiece(True)
    
    # checks if space is unoccupied
    if (b1.checkersBoard[rowy][coly] == " "):
        
        # variable to make checkboard look
        offset = 1
        
        # even rows 0-8
        if rowy % 2 == 0:
            offset = 0
            
        # check if red square
        if ((coly + offset) % 2 == 0):

            # if player 1's turn
            if (Player.playerTurn == 0):
                
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
                        Player.playerTurn += 1
                        
                    # capturing piece down 2 and to the right 2
                    elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                        
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] == "RS" or "RK"):
                            b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] = " "
                            capturePieceBlackSingle(rowy, coly)
                            
                        # if space between is unoccupied   
                        else:
                            return
                        
                    # capturing piece down 2 and to the left 2
                    elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                        
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] == "RS" or "RK"):
                            b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] = " "
                            capturePieceBlackSingle(rowy, coly)
                            
                        # if space between is unoccupied
                        else:
                            return
                        
                elif (b1.checkersBoard[b1.pieceRow][b1.pieceCol] == "BK"):
                    
                    # if row of new position is one below or above that of current one
                    # and col of new position is to the left or right of current one
                    if (((b1.pieceRow - 1) == rowy) or ((b1.pieceRow + 1) == rowy) and (((b1.pieceCol - 1) == coly) or ((b1.pieceCol + 1) == coly))):
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                        Player.playerTurn += 1
                        
                    # capturing piece down 2 and to the right 2
                    elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                        
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] == "RS" or "RK"):
                            b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] = " "
                            capturePieceBlackKing(rowy, coly)
                            
                        # if space between is unoccupied   
                        else:
                            return

                    # capturing piece down 2 and to the left 2
                    elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol - 2) == coly))):

                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] == "RS" or "RK"):
                            b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] = " "
                            capturePieceBlackKing(rowy, coly)

                        # if space between is unoccupied
                        else:
                            return

                    # capturing piece up 2 and to the right 2
                    elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                        
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] == "RS" or "RK"):
                            b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] = " "
                            capturePieceBlackKing(rowy, coly)

                        # if space between is unoccupied   
                        else:
                            return

                    # capturing piece up 2 and to the left 2
                    elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                        
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] == "RS" or "RK"):
                            b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] = " "
                            capturePieceBlackKing(rowy, coly)
    
                        # if space between is unoccupied
                        else:
                            return
                else:
                    pass

            # if player 2's turn
            if (Player.playerTurn == 1):
                
                # if the original piece is a red single
                if (b1.checkersBoard[b1.pieceRow][b1.pieceCol] == "RS"):
                    
                    # if row of new position is one above that of current one
                    # and col of new position is to the left or right of current one
                    if (((b1.pieceRow - 1) == rowy) and (((b1.pieceCol - 1) == coly) or ((b1.pieceCol + 1) == coly))):

                        # makes piece a double if it reaches opposite side of board
                        if (rowy == 0):
                            b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = "RK", b1.checkersBoard[rowy][coly]

                        else:
                            b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                        Player.playerTurn -= 1

                    # capturing piece up 2 and to the right 2
                    elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                        
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] == "BS" or "BK"):
                            b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] = " "
                            capturePieceRedSingle(rowy, coly)
            
                        # if space between is unoccupied   
                        else:
                            return
                        
                    # capturing piece up 2 and to the left 2
                    elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol - 2) == coly))):

                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] == "BS" or "BK"):
                            b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] = " "
                            capturePieceRedSingle(rowy, coly)
                            
                        # if space between is unoccupied
                        else:
                            return
                
                elif (b1.checkersBoard[b1.pieceRow][b1.pieceCol] == "RK"):
                    
                    # if row of new position is one below or above that of current one
                    # and col of new position is to the left or right of current one
                    if (((b1.pieceRow - 1) == rowy) or ((b1.pieceRow + 1) == rowy) and (((b1.pieceCol - 1) == coly) or ((b1.pieceCol + 1) == coly))):
                        b1.checkersBoard[rowy][coly], b1.checkersBoard[b1.pieceRow][b1.pieceCol] = b1.checkersBoard[b1.pieceRow][b1.pieceCol], b1.checkersBoard[rowy][coly]
                        b1.setupBoard()
                        Player.playerTurn -= 1
                    # capturing piece down 2 and to the right 2
                    
                    elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol + 2) == coly))):
                        
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] == "BS" or "BK"):
                            b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol + 1] = " "
                            capturePieceRedKing(rowy, coly)
                            
                        # if space between is unoccupied   
                        else:
                            return
                        
                    # capturing piece down 2 and to the left 2
                    elif (((b1.pieceRow + 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                        
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] == "BS" or "BK"):
                            b1.checkersBoard[b1.pieceRow + 1][b1.pieceCol - 1] = " "
                            capturePieceRedKing(rowy, coly)
                            
                        # if space between is unoccupied
                        else:
                            return
        
                    # capturing piece up 2 and to the right 2
                    elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol + 2) == coly))):
            
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] == "BS" or "BK"):
                            b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol + 1] = " "
                            capturePieceRedKing(rowy, coly)
                            
                        # if space between is unoccupied   
                        else:
                            return
                
                    # capturing piece up 2 and to the left 2
                    elif (((b1.pieceRow - 2) == rowy) and (((b1.pieceCol - 2) == coly))):
                        
                        # if space between is occupied
                        if (b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] == "BS" or "BK"):
                            b1.checkersBoard[b1.pieceRow - 1][b1.pieceCol - 1] = " "
                            capturePieceRedKing(rowy, coly)
                            
                        # if space between is unoccupied
                        else:
                            return
                else:
                    pass
    sleep(.1)
    GPIO.output(leds[1],0)

##################################
# MAIN
##################################
# dimensions of board for pi screen
#WIDTH, HEIGHT = window.winfo_screenwidth(), window.winfo_screenheight()
##################################

#variables for GPIO input/output
buttons= [6,17]
leds= [5,16]
joystick = [18,19,20,21]
GPIO.setmode(GPIO.BCM)

#setup for joystick
for i in range(len(joystick)):
    GPIO.setup(joystick[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#adds the event for the bind() function for the joysticks
GPIO.add_event_detect(joystick[0], GPIO.BOTH, callback=lambda x:joystickEvent(window,joystick[0]),bouncetime=800)
GPIO.add_event_detect(joystick[1], GPIO.BOTH, callback=lambda x:joystickEvent(window,joystick[1]),bouncetime=800)
GPIO.add_event_detect(joystick[2], GPIO.BOTH, callback=lambda x:joystickEvent(window,joystick[2]),bouncetime=800)
GPIO.add_event_detect(joystick[3], GPIO.BOTH, callback=lambda x:joystickEvent(window,joystick[3]),bouncetime=800)

#setup for buttons and their leds
for i in range(len(buttons)):
    GPIO.setup(buttons[i],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(leds[i],GPIO.OUT)

#adds event for the bind() funciton for the buttons
GPIO.add_event_detect(buttons[0], GPIO.FALLING, callback= lambda x:button1Event(window,buttons[0]),bouncetime=800)
GPIO.add_event_detect(buttons[1], GPIO.FALLING, callback= lambda x:button1Event(window,buttons[1]),bouncetime=800)

#binding joysticks and buttons to probper functions
window.bind("<<joystick18>>",up)
window.bind("<<joystick19>>",down)
window.bind("<<joystick20>>",right)
window.bind("<<joystick21>>",left)
window.bind("<<button6>>",button1)
window.bind("<<button17>>",button2)

#uses the mouse to reset and quit game if desired
#can be used to put in buttons at a later date.
window.bind("<Double-Button-1>", quits)
window.bind("<Button-1>", reset)

window.attributes("-fullscreen", True)
# changes geometry of window
#window.geometry("%dx%d+0+0"%(WIDTH,HEIGHT))

# changes title of window
window.title("CHECKERS")

# creates an instance of board
b1 = Board(window)

# creates copy of original board for resets
originalBoard = copy.deepcopy(b1.checkersBoard)

# renders the GUI in the mainloop
window.mainloop()
