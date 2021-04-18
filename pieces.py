###########################
# IMPORTS
###########################

from tkinter import *

##################################
# CLASS
##################################
class Piece:
    # constructor
    def __init__(self, image):
        self.image = image

    # accessor for image
    @property  # says that an accessor/a getter follows
    def image(self):
        return self._image

    # mutator for image
    @image.setter  # says that a mutator/setter follows
    def image(self, image):
        self._image = image


class Single(Piece):
    # class variables
    # list containing black, white pieces of piece type
    knightImage = [PhotoImage(file="checkers-img\black_checker.png"), \
                   PhotoImage(file="checkers-img\red_checker.png")]

    # constructor
    def __init__(self, number):
        # inherits from the Piece superclass
        Piece.__init__(self, knightImage[number])


class Double(Piece):
    # class variables
    # list containing black, white pieces of piece type
    rookImage = [PhotoImage(file="checkers-img\black_checker_double.png"), \
                 PhotoImage(file="checkers-img\red_checker_double.png")]

    # constructor
    def __init__(self, number):
        # inherits from the Piece superclass
        Piece.__init__(self, rookImage[number])
