import enum

class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2
    
    
class Grid:
    def __init__(self, n_rows, n_columns):
        self.grid = [
            [GridPosition.EMPTY for _ in range(n_columns)] for _ in range(n_rows)
            ]
        self.n_rows = n_rows
        self.n_columns= n_columns
        
    def place_piece(self, column, piece):
        if column < 0 or column>=self.ncolumns:
            raise ValueError('Invalid column')
        
        for _ in self.grid.reverse():
            if _[column] == GridPosition.EMPTY:
                _[column] = piece
                return
            
    def print_grid(self):
        print(self.grid)
    
    # def print_grid(self):
    #     for row in self.grid:
    #         print([cell.value for cell in row])
            
g = Grid(3,3)
g.print_grid()

            
            
            
        
    
        
    