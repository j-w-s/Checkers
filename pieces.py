class Piece:
    # constructor
    def __init__(self, image):
        self.image = image

    # accessor for image
    @property # says that an accessor/a getter follows
    def image(self):
        return self._image

    # mutator for image
    @image.setter # says that a mutator/setter follows
    def image(self, image):
        self._image = image

class Knight(Piece):
    # class variables
    # list containing black, white pieces of piece type
    knightImage = ["CHESS PIECES\Chess_ndt60.png",\
                 "CHESS PIECES\Chess_nlt60.png"]
    # constructor
    def __init__(self, number):
        # inherits from the Piece superclass
        Piece.__init__(self, knightImage[number])

class Rook(Piece):
    # class variables
    # list containing black, white pieces of piece type
    rookImage = ["CHESS PIECES\Chess_rdt60.png",\
                 "CHESS PIECES\Chess_rlt60.png"]
    #constructor
    def __init__(self, number):
        # inherits from the Piece superclass
        Piece.__init__(self, rookImage[number])

class Bishop(Piece):
    # class variables
    # list containing black, white pieces of piece type
    bishopImage = ["CHESS PIECES\Chess_bdt60.png",\
                   "CHESS PIECES\Chess_blt60.png"]
    # constructor
    def __init__(self, number):
        # inherits from the Piece superclass
        Piece.__init__(self, bishopImage[number])

class Queen(Piece):
    # class variables
    # list containing black, white pieces of piece type
    queenImage = ["CHESS PIECES\Chess_qdt60.png",\
                   "CHESS PIECES\Chess_qlt60.png"]
    # constructor
    def __init__(self, number):
        # inherits from the Piece superclass
        Piece.__init__(self, queenImage[number])

class King(Piece):
    # class variables
    # list containing black, white pieces of piece type
    kingImage = ["CHESS PIECES\Chess_kdt60.png",\
                 "CHESS PIECES\Chess_klt60.png"]
    # constructor
    def __init__(self, number):
        # inherits from the Piece superclass
        Piece.__init__(self, kingImage[number])
        
class Pawn(Piece):
    # class variables
    # list containing black, white pieces of piece type
    pawnImage = ["CHESS PIECES\Chess_pdt60.png",\
                 "CHESS PIECES\Chess_plt60.png"]
    # constructor
    def __init__(self, number):
        # inherits from the Piece superclass
        Piece.__init__(self, pawnImage[number])
