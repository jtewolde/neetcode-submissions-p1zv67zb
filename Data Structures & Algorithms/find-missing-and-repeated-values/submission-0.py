class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Approach: Use hashsets to find the duplicate/repeating numbers in grid
        # Then, determine the missing number that was replaced
        # First, initialize empty seen hashset to store visited numbers in grid
        # Also, create N variables to shorten getting the length of grid array
        # and double and missing variables to the number of missing/double numbers
        # Use nested for loop to determine if current number in grid is in seen set, if so assign double to current num
        # Add current num to seen set regardless
        # Then, iterate through every number from 1 to n^2 + 1
        # Find the missing values by determining if current num not in seen,
        # Assign missing variable to current num
        # Return both values of double and missing in array

        N = len(grid)
        double = missing = 0
        seen = set()

        for i in range(N):
            for j in range(N):
                if grid[i][j] in seen:
                    double = grid[i][j]
                seen.add(grid[i][j])

        for num in range(1, N*N + 1):
            if num not in seen:
                missing = num
                break

        return [double, missing]

