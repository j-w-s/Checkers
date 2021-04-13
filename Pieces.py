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
    blackKnight = "CHESS PIECES\Chess_ndt60.png"
    whiteKnight = "CHESS PIECES\Chess_nlt60.png"
    # class variables
    def __init__(self):
        # inherits from the Piece superclass
        Pieces.__init__(self)

class Rook(Piece):
    # class variables
    blackRook = "CHESS PIECES\Chess_rdt60.png"
    whiteRook = "CHESS PIECES\Chess_rlt60.png"
    rookColor = ["CHESS PIECES\Chess_rdt60.png", "CHESS PIECES\Chess_rlt60.png"] # such that black, white pieces
    # could call i=1 or i=2 in p1 = Piece(1) or p2 = Piece(2) and
    # use:
    # def __init__(self, i):
    # Pieces.__init__(self, rookColor[i]
    # for EVERY piece type
    # class variables
    def __init__(self):
        # inherits from the Piece superclass
        Pieces.__init__(self)

class Bishop(Piece):
    # class variables
    blackBishop = "CHESS PIECES\Chess_bdt60.png"
    whiteBishop = "CHESS PIECES\Chess_blt60.png"
    # class variables
    def __init__(self):
        # inherits from the Piece superclass
        Pieces.__init__(self)

class Queen(Piece):
    # class variables
    blackQueen = "CHESS PIECES\Chess_qdt60.png"
    whiteQueen = "CHESS PIECES\Chess_qlt60.png"
    # class variables
    def __init__(self):
        # inherits from the Piece superclass
        Pieces.__init__(self)

class King(Piece):
    # class variables
    blackKing = "CHESS PIECES\Chess_kdt60.png"
    whiteKing = "CHESS PIECES\Chess_klt60.png"
    # class variables
    def __init__(self):
        # inherits from the Piece superclass
        Pieces.__init__(self)
        
class Pawn(Piece):
    # class variables
    blackPawn = "CHESS PIECES\Chess_pdt60.png"
    whitePawn = "CHESS PIECES\Chess_plt60.png"
    # class variables
    def __init__(self):
        # inherits from the Piece superclass
        Pieces.__init__(self)
