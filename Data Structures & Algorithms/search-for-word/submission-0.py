class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Use recursive backtracking to solve this problem
        # First, create two variables to get the length of rows and columns in the word table
        # Also, create a data structure, path, that is a set to keep track of paths taken to create word
        # Initialize DFS function whre the parameters are the curr row and col and char for current character on

        # Create two base/edges cases to return boolean value
        # First case: If char is equal to len(word), then we have found the solution, return True

        # Second case: If the following conditions are met, return false:
        # If current val of row or col are out of bounds (< 0 or > ROWS, COLS),
        # Current char in word is not equal to char on the board[row][col],
        # or if current position(row, col) tuple is in path, already been visited.
        
        # Add the current coordinate(row, col) to the path set
        # Create a res variable that recursively calls DFS on each four directions to finding the path of the word,
        # Call DFS whrne going Left, right, up, and down
        # Then, remove current postion from path because we already visited that path

        # Create nested for loop to iterate through entire board
        # Call recursive dfs function, if it returns true, Return true
        # Else, return False by default


        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, col, char):
            if char == len(word):
                return True

            if (row < 0 or col < 0 or row >= ROWS or col >= COLS 
                or word[char] != board[row][col] or (row, col) in path):
                return False
            
            path.add((row, col))
            ans = (dfs(row + 1, col, char + 1) or
                    dfs(row - 1, col, char + 1) or
                    dfs(row, col + 1, char + 1) or
                    dfs(row, col - 1, char + 1))
            path.remove((row, col))
            return ans

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False










