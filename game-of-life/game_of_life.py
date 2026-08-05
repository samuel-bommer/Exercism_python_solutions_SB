"""
Game of life
"""


def determine_neighboors(matrix: tuple[list], pos_r: int, pos_c: int) -> list:
    """
    Determine neighboor for one cell
    """

    amount_rows = len(matrix)
    amount_col = len(matrix[0])
    
    neighboors_coord = []
    
    for dir_row in range(-1, 2):
        for dir_col in range(-1, 2):
            if dir_row == dir_col == 0:
                continue
            
            neighboor_r = dir_row + pos_r
            neighboor_c = dir_col + pos_c
            
            if 0 <= neighboor_r < amount_rows and 0 <= neighboor_c < amount_col:
                neighboors_coord.append((neighboor_r, neighboor_c))
                
    return neighboors_coord
                
    

def tick(matrix: tuple[list]) -> tuple[list]:
    """ 
    Conway's game of life.
    The following rules are applied:
    - Any live cell with two or three live neighboors lives on
    - Any dead cell with exactly three live neighboors becomes a live cell
    - All other cells die or stay dead    
    """
    
    if not matrix:
        return []
    amount_rows = len(matrix)
    amount_col = len(matrix[0])   
    
    conways_matrix = [[0] * amount_col for _ in range(amount_rows)]
    
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            neighboors_coord = determine_neighboors(matrix, row, column)
            
            alive_neighboors = 0
            for neig in neighboors_coord:
                if matrix[neig[0]][neig[1]] == 1:
                    alive_neighboors += 1
            
            if matrix[row][column] == 1:
                if alive_neighboors == 2 or alive_neighboors == 3:
                    conways_matrix[row][column] = 1
                else:
                    conways_matrix[row][column] = 0
                
            else:
                if alive_neighboors == 3:
                    conways_matrix[row][column] = 1
                
            print(alive_neighboors)
                
    return conways_matrix
            
