import numpy as np

class sudoku():

    def __init__(self,string):
    
        self.string = string

    def board(self):
    
        global rows
    
        rows = np.array([])
    
        for i in self.string:
    
            rows = np.append(rows,i)
    
        rows = rows.reshape(9,9)
    
        return rows
    
    def get_row(self,k):
    
        return rows[k]
    
    def get_column(self,k):
    
        trans = rows.T
    
        return trans[k]
    
    def get_square(self,pos = [-1]):
    
        squares,squares1 = np.array([]), np.array([])
    
        for i in range(27):
    
            squares= np.append(squares,self.string[3*i:3*(i+1)])
    
        for i in range(3):
    
            squares1 = np.append(squares1,[squares[i],squares[(i+3)],squares[(i+6)]])
    
        for i in range(3):
    
            squares1 = np.append(squares1,[squares[i+9],squares[(i+12)],squares[(i+15)]])
    
        for i in range(3):
    
            squares1 = np.append(squares1,[squares[i+18],squares[(i+21)],squares[(i+24)]])
    
        squares1 = squares1.reshape(9,3)
    
        if len(pos)==1:
    
            return squares1[pos[0]]
    
        else:
    
            n = pos[0]//3
    
            m =pos[1]//3
    
            if n<1:
    
                return squares1[m]
    
            elif n<2:
    
                return squares1[m+3]
    
            else:
    
                return squares1[m+6]

game = sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")

print(game.board()) 
print(game.get_row(0))
print(game.get_column(8))
print(game.get_square([1]))
print(game.get_square([1,8]))
print(game.get_square([8,3]))