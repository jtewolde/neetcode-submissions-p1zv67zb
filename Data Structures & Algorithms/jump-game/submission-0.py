class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Approach to solving this problem using Greedy Techinque
        # Goal is to find out if the end of nums array can be reached with each index acting as a jump
        # Initialize two variables, n for the length of nums, and target for the end of the array
        # Create for loop that starts at the end of the array and goes backwards one
        # Declare an If statement saying that if nums[index] + index >= target, then set target to the current index.
        # Return the boolean value of if the target == 0, or if target is at start of array,

        n = len(nums)
        target = n - 1
        
        for index in range(n - 1, -1, -1):
            if index + nums[index] >= target:
                target = index

        return target == 0