class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Approach: Use backtracking/recursion to determine if a square can be formed from matchsticks
        # In the matchsticks array, sticks can be combined to equal for a side of the square
        # Each "side" needs to be equal to each other to make a square

        # First, get the total sum of matchsticks array and use modular division by 4
        # This will determine if the matchsticks can form a square with all 4 sides are equal
        totalSum = sum(matchsticks)
        if totalSum % 4 != 0:
            return False

        # Then, calculate the side length that square has to have by dividing sum by 4
        # Initialize sides array that will store the sides of square with zero as elements for 4 indexes
        # Also, reverse sort the array so that larger sticks are placed first
        sideLength = totalSum // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        # Initialize backtracking function that takes indx as parameter
        def backtrack(indx):
            # Base case: If all sides are created with no issues, return True
            if indx == len(matchsticks):
                return True

            # Iterate through all 4 sides of the square
            for j in range(4):
                # Determine if combining smaller matchsticks is possible 
                # And doesn't exceed expected side length. If true, add current matchstick to current side in array
                if sides[j] + matchsticks[indx] <= sideLength:
                    sides[j] += matchsticks[indx]
                    # Use backtrack to do the same for the next matchstick and return true if no issues
                    if backtrack(indx + 1):
                        return True
                    # Otherwise, backtrack by subtracting from that side of square
                    sides[j] -= matchsticks[indx]
            return False
        # Return the result of backtracking function by starting at index 0
        return backtrack(0)






