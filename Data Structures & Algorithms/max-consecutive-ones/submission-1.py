class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Brute force: Create max_streak variable that keeps track of max # of 1's consecutively
        # Iterate through entire nums array, if current num is a 1, increment streak by one
        # If encountering a zero, trest streak back to zero.
        # Return streak variable as final answer

        # Create max and curr streak variables to keep track of current streak of 1's
        # And keep track of max streak of 1's
        max_streak = 0
        curr_streak = 0

        # Iterate through all numbers in nums array,
        # If current num is 1, increment curr streak by one and update max streak
        # Else, reset curr streak back to zero
        for num in nums:
            if num == 1:
                curr_streak += 1
                max_streak = max(max_streak, curr_streak)
            else:
                curr_streak = 0
            print(curr_streak, max_streak)

        return max_streak