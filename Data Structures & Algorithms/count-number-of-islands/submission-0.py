class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approaach os solving this problem is with a matrix DFS/BFS
        
        # Initialize row/col variables for the dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Create dfs function where it takes position of rows and cols
        # If the position is out of bounds or current position isn't a 1, return nothing
        # Else, set current position on grid to zero
        # Run DFS on surorunding areas from all four directions
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            else:
                grid[r][c] = '0'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        # Variable to keep track of number of islands(final answer to return)
        num_islands = 0

        # Iterate through grid, if current position is a island,
        # Increment num_islands by one and run dfs to locate other ones around it
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r,c)

        return num_islands