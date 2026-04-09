class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Using Binary search approach
        # Perform binary search twice, one for searching for which row the target is in
        # Second for searching for the target in the correct row

        # Create rows and cols variables
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # Pointers for performing Binary Search on which row target is in
        top = 0
        bottom = ROWS - 1 

        # Fist binary search for finding row where target is
        while top <= bottom:
            midRow = (top + bottom) // 2 # variable for middle row

            # If target value is greater than the last value of current row
            # Move top pointer down, eliminating lesser value row
            if target > matrix[midRow][-1]:
                top = midRow + 1
            # If target is less than first number in current row, move bottom pointer down,
            # Eliminate higher number rows
            elif target < matrix[midRow][0]:
                bottom = midRow - 1
            # break out of loop if current row is where targt is
            else:
                break 

        # If neither rows contain target, return false
        if not (top <= bottom):
            return False

        row = (top + bottom) // 2 # variable for row where target is in
        
        left, right = 0, COLS - 1 # Pointers for second binary search

        # Second binary search for finding target in midRow
        while left <= right:
            middle = (left + right) // 2
            
            # Eliminate lower half of row
            if target > matrix[row][middle]:
                left = middle + 1
            # Eliminate upper half of row
            elif target < matrix[row][middle]:
                right = middle - 1
            # Found target in matrix
            else:
                return True

        return False







