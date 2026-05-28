class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Approach: Use DFS and backtracking to explore the adjacent cells in image graph

        # First, initialize originalCol to store the original color of the starting pixel
        # Check if the originalCol === color, if true, return immediately as no work is needed
        originalCol = image[sr][sc]
        if originalCol == color:
            return image

        # Initialize variables for getting length of rows and cols in image 
        m, n = len(image), len(image[0])

        # Create a DFS function that takes row and col as parameters
        def dfs(row, col):
            # Inside of DFS, check if row and col are out of bounds or don't match originalCol
            # Return nothing if any above is true
            if row < 0 or row >= m or col < 0 or col >= n or image[row][col] != originalCol:
                return 
            
            # Recursively call DFS on adjacent neighbors from up, down, left, and right
            # Outside of DFS, call DFS from initial coords and return result as final answer
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Outside of DFS, call DFS from initial coords and return image after modification
        dfs(sr, sc)
        return image
            
