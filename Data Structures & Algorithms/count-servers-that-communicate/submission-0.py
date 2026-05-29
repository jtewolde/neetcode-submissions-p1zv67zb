class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Approach: Use iteration to count the number of servers in each row and col
        # Initialize variables for getting length of ROWS and COLS in grid
        # Also, create arrays for counting num of servers in every row and col
        # Do some preprocessing for grid by iterating through entire grid
        # If current position in grid is a server(1), then increment count for row and col
        # Then, create nested for loop to iterate through grid again,
        # Determine if current pos is a server and if the max count of servers on current row and col > 1,
        # Then, increment ans variable by one and return as final answer

        # Initialize variables for getting length of ROWS and COLS in grid
        # Also, create arrays for counting num of servers in every row and col
        # As well as ans for storing final count of valid servers in grid
        ROWS, COLS = len(grid), len(grid[0])
        rowCount = [0] * ROWS
        colCount = [0] * COLS
        ans = 0

        # Do some preprocessing for grid by iterating through entire grid
        # If current position in grid is a server(1), then increment count for row and col
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1

        # Then, create nested for loop to iterate through grid again,
        # Determine if current pos is a server 
        # and if the max count of servers on current row and col > 1,
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and max(rowCount[r], colCount[c]) > 1:
                    ans += 1
        return ans

