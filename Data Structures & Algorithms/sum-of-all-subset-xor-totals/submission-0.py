class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Approach: Use backtracking and recursion to get the XOR sum of all subsets and combine them for total 
        # First, create ans variable to keep track of XOR total of all subsets combined
        # Initialize backtrack function where the parameters are indx and current total of subset
        # Create base case if statement to determine if indx equals len of nums, if so, return the current XOR Total
        # Use recursive call for backtrack to calculate the XOR total for subset including num at indx
        # Do this by making the total parameter have the power of the number at indx position
        # Then, call the same recursive backtrack function to calculate the XOR total without including num at indx
        # Return the totalSum between those two calculations from recursive calls
        # Finally, call the backtrack function, starting at 0 indx and 0 total for parameters and return as final ans

        # First, create ans variable to keep track of XOR total of all subsets combined
        ans = 0

        # Initialize backtrack function where the parameters are indx and current total of subset
        def backtrack(indx, total):
            # Create base case if statement to determine if indx equals len of nums 
            # If so, return the current XOR Total
            if indx == len(nums):
                return total

            # Use recursive call for backtrack to calculate the XOR total for subset including num at indx
            # Do this by making the total parameter have the power of the number at indx position
            sum1 = backtrack(indx + 1, total ^ nums[indx])
            # Then, call the same recursive backtrack function to calculate the XOR total without including num at indx
            sum2 = backtrack(indx + 1, total)

            # Calculate the total XOR sum between those subsets and return it
            totalSum = sum1 + sum2
            return totalSum

        return backtrack(0, 0)
