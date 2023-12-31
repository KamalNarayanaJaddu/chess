from const import *
from square import Square
from piece import *
class Board:
    def __init__(self):
        self.squares=[[0,0,0,0,0,0,0,0] for col in range(cols)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
    def _create(self):
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col]= Square(row,col)
    def _add_pieces(self, color):
        row_pawn, row_other =(6, 7) if color=='white' else (1,0)

        #pawns
        for col in range(cols):
            self.squares[row_pawn][col]= Square(row_pawn, col, pawn(color))

        #knights
        self.squares[row_other][1]=Square(row_other, 1, knight(color))
        self.squares[row_other][6]=Square(row_other, 6, knight(color))

        #bishops
        self.squares[row_other][2]=Square(row_other, 2, bishop(color))
        self.squares[row_other][5]=Square(row_other, 5, bishop(color))

        #rook
        self.squares[row_other][0]=Square(row_other, 0, rook(color))
        self.squares[row_other][7]=Square(row_other, 7, rook(color))

        #queen
        self.squares[row_other][3]=Square(row_other, 3, queen(color))

        #king
        self.squares[row_other][4]=Square(row_other, 4, king(color))
    