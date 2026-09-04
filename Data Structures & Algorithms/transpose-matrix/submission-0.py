class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Approach: Use iteration to go through each number in the given matrix and put into the new tranposed martix
        # Transposing the given matrix means swapping the values of the cols and rows of original matrix with transposed matrix

        # Initialize the values of the rows and cols of the original matrix
        # Create transposed matrix that makes the cols of transposed be the rows of the original and vice versa
        ROWS, COLS = len(matrix), len(matrix[0])
        transposedMatrix = [[0] * ROWS for _ in range(COLS)]

        # Iterate through each element with its current position (row, col) in the original matrix
        # Place the element in the transposed matrix with position (col, row)
        for row in range(ROWS):
            for col in range(COLS):
                transposedMatrix[col][row] = matrix[row][col]
        return transposedMatrix