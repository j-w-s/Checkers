##################################
# IMPORTS
##################################

# import Pieces, Board, Movement
from tkinter import *

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
