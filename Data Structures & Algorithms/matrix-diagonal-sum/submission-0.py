class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # Approach: Use iteration to compute both diagonal sums in a single pass
        # Primary diagonal goes from top left to bottom right and each position in diagonal has the coordinaes with same number
        # Secondary diagonal goes from top right to bottom left and each pos in diagonal will be mat[i][n - i - 1]
        
        # First, initialize ans varialbe that will store the final sum of diagonal sums
        # Also, create n variable for storing length of matrix
        ans, n = 0, len(mat)

        # Then, use for loop to iterate through each row index in the matrix from 0 to len(mat)
        for i in range(n):
            # Get the sum of primary diagonal elements with mat[i][i] and add to ans
            # Get the sum of secondary diagonal elements with mat[i][n - i - 1] and add to ans
            ans += mat[i][i]
            ans += mat[i][n - i - 1]

        # Create centerElement variable that stores the shared center element in diagonal sums when matrix row is odd
        # If the number of rows in mat is odd, then set the variable to the center element in mat
        centerElement = 0
        if n % 2 == 1:
            centerElement = mat[n // 2][n // 2]

        # Return ans subtracted from center element if it is odd or not
        return ans - centerElement

