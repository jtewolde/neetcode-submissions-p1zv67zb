class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # To build the Pascal's Triangle, each row is built upon the previous row
        # The triangle always start with [1] and each row in the triangle incremently in length
        # Approach: Initialize/create the first row in the triangle with [[1]]
        # Create nested for loops to create next rows in Pascal triangle and building the numbers in row
        # To build new row, take last row and pad it with zeros in temp array to sum adjacent elements with edges 
        # After creating new row, append it to the triangle array

        # Initialize triangle array that will store Pascal's Triangle rows
        triangle = [[1]]

        # Create first for loop for creating number of rows in Pascal's Triangle
        for row in range(numRows - 1):
            # Pad the previous row with zeros on the end for easier creation of next rows
            temp = [0] + triangle[-1] + [0]
            currRow = []
            # Second for loop is for creating elements/numbers in each row by adding the two adjacent numbers
            for element in range(len(triangle[-1]) + 1):
                currRow.append(temp[element] + temp[element + 1])
            # Append the newly created row to triangle 
            triangle.append(currRow)

        return triangle
