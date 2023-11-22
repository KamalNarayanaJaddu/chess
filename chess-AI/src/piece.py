import os;
class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name= name
        self.color=color
        value_sign=1 if color=='white' else -1
        self.value=value * value_sign
        self.moves=[]
        self.moved= False
        self.texture=texture
        self.set_texture()
        self.texture_rect= texture_rect

    def set_texture(self, size=80):
        self.texture =os.path.join(
            f'../assets/images/imgs-{size}px/{self.color}_{self.name}.png')
    def add_moves(self, move):
        self.moves.append(move)
        
    
    def clear_moves(self):
        self.moves = []


class pawn(Piece):

    def __init__(self,color):
        super().__init__(self,color,1.0)
    
class knight(Piece):

    def __init__(self,color):
        super().__init__(self,color,3.0)

class bishop(Piece):

    def __init__(self,color):
        super().__init__(self,color,3.0001)
    
class rook(Piece):

    def __init__(self,color):
        super().__init__(self,color,5.0)
    
class queen(Piece):

    def __init__(self,color):
        super().__init__(self,color,9.0)
    
class king(Piece):

    def __init__(self,color):
        super().__init__(self,color,100000.0)
       