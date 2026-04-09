class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Approach for solving this problem is with matrix DFS,
        # Only difference from number of islands problem is that instead of tracking # of islands
        # Answer is looking for max area of each island on grid

        # Inititalize variables for the dimensions of grid 
        rows, cols = len(grid), len(grid[0])

        # Create dfs function where its arguments are the position inside of grid
        # Base case is if the position is out of bounds or it isn't a '1', return area as zero
        # Else, set current position to be zero
        # Then, calculate maxArea of island by adding 1 for current position with running DFS on other directions
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            else:
                grid[r][c] = '0'
                return 1 + (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r , c + 1) + dfs(r, c - 1))

        # Iterate through entire grid, if encounter a '1', then set maxArea to be the maximum between itself and area of island
        # Create variable to keep track of maxArea of 1's. Return at the end
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea

