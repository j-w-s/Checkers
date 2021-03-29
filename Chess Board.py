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
    def __init__(self,container):
        Frame.__init__(self,container)
        self.setupGUI()

    # ??
    def setupGUI(self):
        # create a loop for rows
        self.Name = Label(self, height =1, width = 5, font = ("Arial",10), background = "grey93")
        self.Name.grid(row=0,column=0)
        
        for rows in range(1,8):
            # create row names
            self.rowname = Label(self,text=(rows), height = 5, width =5, background = "gray93")
            self.rowname.grid(row=rows,column=0, sticky = E)

            topLabels = ['A','B','C','D','E','F','G','H']
            # inner loop for columns
            for col in range(1,9):
                # create column names
                self.letter = Label(self,text=topLabels[col-1], height =2, width = 10, background="gray93")
                self.letter.grid(row = 0, column=col, sticky = S)
                
                # variable to make checkboard look
                offset = 0

                # even rows 0-8
                if rows%2 == 0:
                    offset = 1

                # if the column is 1,3,5,7 and row is 0,2,4,6,8
                #m ake the box brown
                if (col + offset)%2 == 0:
                    self.box1 = Label(self,text="", height = 5, width = 10, background = "#451d1d")
                    self.box1.grid(row=rows,column=col)
                else:
                    self.box1 = Label(self,text="", height = 5, width = 10, background = "#a47c48")
                    self.box1.grid(row=rows,column=col)
                
        self.pack()

##################################
# MAIN
##################################
window = Tk()
window.title("Board")

# create an instance of board
b1 = Board(window)

# render the GUI in the mainloop
window.mainloop()
