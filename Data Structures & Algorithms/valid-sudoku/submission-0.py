class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Approach for solving this problem is with the use of Hash Sets and iterating through board

        # First, Initialize 3 hash sets for keeping track on numbers on each row, col, and square
        # Use DefaultDict(set) for those hash sets
        # Iterate through entire board by creating nested for loop to view every position on board
        # If current position on board (board[row][col]) is a '.', then continue as it doesn't make sudoku invalid
        # Else, if board[row][col] is already in either hashset for row, col, or squares, return false
        # Otherwise, add current position to each hashset of rows, cols, and squares
        # When adding current position to squares set, make index to be [row // 3][col // 3]
        # Return true by default

        # Initialize 3 hash sets for keeping track of numbers on each row, col, and square
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # Iterate through entire 9x9 sudoku board with nested for loops 
        for row in range(9):
            for col in range(9):
                # Skip current position on board if it is a period
                if board[row][col] == '.':
                    continue
                # Check if current position is already any hashset, return false
                elif (board[row][col] in rows[row] 
                or board[row][col] in cols[col]
                or board[row][col] in squares[(row // 3, col // 3)]):
                    return False

                # Add current position of board to each hash set
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])

        return True
                




                