class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Approach/techinque to solve this problem is using Matrix DFS similar to number of Island probmel
        # Synopsis on Logic:
        # Create mark function that converts surrounded O's to X's and goes to neighboring O's 
        # First, start by going through the characters on the borders of the board
        # Search the first row, last row, first col, last col to see if there are any O's
        # If so, mark any near O's in same row/col to be 'M'
        # Finally, iterate through entire board, if 'M' character is encountered, convert to 'O'
        # If encountering 'O' characters, convert to 'X's

        # Get length and height of board
        rows, cols = len(board), len(board[0])

        # Create mark function that converts qualifying 'O's to 'M' and its neighbors
        def mark(r, c):
            # See if the current position is not a border and its a 'O' character, return nothing
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            else:
                # If the character is a 'O' on the borders on board,
                # Convert to 'M' to be marked and see if there are adjacent 'O' characters
                board[r][c] = 'M'
                mark(r + 1, c)
                mark(r - 1, c)
                mark(r, c + 1)
                mark(r, c - 1)


        # Iterate through first and last row, 
        # Call mark function on any characters that are 'O's
        for r in range(rows):
            if board[r][0] == 'O':
                mark(r, 0)
            if board[r][cols - 1] == 'O':
                mark(r, cols - 1)

        # Iterate through first and last col
        # Call mark function on any characters that are 'O's 
        for c in range(cols):
            if board[0][c] == 'O':
                mark(0, c)
            if board[rows - 1][c] == 'O':
                mark(rows - 1, c)

        # Iterate through the entire board of characters
        # When encountering a 'O', turn it to a 'X' character
        # If encountering a Marked character, 'M', turn it to the original 'O' character
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == "M":
                    board[row][col] = 'O'

        

        






