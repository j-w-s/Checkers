###########################
# IMPORTS
###########################

# import


##################################
# CLASS
##################################
class Movement(self):
    # constructor
    def __init__(self):

    #calculate all the legal moves 
    def possibleMoves(self, piece):
    # **CHANGE THIS VARIABLE TO PLAYER PIECE***********
    # self.piece = piece
    # list containing all legal moves
    legalMoves = []
    # iterates over all the tiles on the board
    for i in range(64):
        # at position,

        # check whether there's a white rook or not
        if (self.chessBoard[int(i/8)][i%8] == "WR" and self.piece == "WR"):
        movesList += self.RookMove(i)

        # check whether there's a black rook or not
        elif (self.chessBoard[int(i/8)][i%8] == "BR" and self.piece == "BR"):
        movesList += self.RookMove(i)

        # check whether there's a white knight or not
        elif (self.chessBoard[int(i/8)][i%8] == "WKN" and self.piece == "WKN"):
        movesList += self.KnightMove(i)

        # check whether there's a black knight or not
        elif (self.chessBoard[int(i/8)][i%8] == "BKN" and self.piece == "BKN"):
        movesList += self.KnightMove(i)

        # check whether there's a white bishop or not
        elif (self.chessBoard[int(i/8)][i%8] == "WB" and self.piece == "WB"):
        movesList += self.BishopMove(i)

        # check whether there's a black bishop or not
        elif (self.chessBoard[int(i/8)][i%8] == "BB" and self.piece == "BB"):
        movesList += self.BishopMove(i)

        # check whether there's a white queen or not
        elif (self.chessBoard[int(i/8)][i%8] == "WQ" and self.piece == "WQ"):
        movesList += self.QueenMove(i)

        # check whether there's a black queen or not
        elif (self.chessBoard[int(i/8)][i%8] == "BQ" and self.piece == "BQ"):
        movesList += self.QueenMove(i)

        # check whether there's a white king or not
        elif (self.chessBoard[int(i/8)][i%8] == "WK" and self.piece == "WK"):
        movesList += self.KingMove(i)

        # check whether there's a black king or not
        elif (self.chessBoard[int(i/8)][i%8] == "BK" and self.piece == "BK"):
        movesList += self.KingMove(i)

        # check whether there's a white pawn or not
        elif (self.chessBoard[int(i/8)][i%8] == "WP" and self.piece == "WP"):
        movesList += self.WhitePawnMove(i)

        # check whether there's a black pawn or not
        elif (self.chessBoard[int(i/8)][i%8] == "BP" and self.piece == "BP"):
        legalMoves += self.BlackPawnMove(i)

    #returns the list of appended movement lists
    return legalMoves

    def isCheck(self):
        # **** UPDATE THIS TO MAKE IT WORK WITH OUR CODE ******
        # ascertain where the kings are, check all pieces of opposing color against those kings, then if either get hit, check if its checkmate
        # king = King
        # kingDict = {}
        # pieceDict = {BLACK : [], WHITE : []}
        # for position, piece in self.gameboard.items():
            if type(piece) == King:
                kingDict[piece.Color] = position
            print(piece)
            pieceDict[piece.Color].append((piece,position))
        #white
        if self.canSeeKing(kingDict[WHITE],pieceDict[BLACK]):
            self.message = "White player is in check"
        if self.canSeeKing(kingDict[BLACK],pieceDict[WHITE]):
            self.message = "Black player is in check"
        
        
    def canSeeKing(self,kingpos,piecelist):
        # **** UPDATE THIS TO MAKE IT WORK WITH OUR CODE ******
        #checks if any pieces in piece list (which is an array of (piece,position) tuples) can see the king in kingpos
        for piece,position in piecelist:
            if piece.isValid(position,kingpos,piece.Color,self.gameboard):
                return True
