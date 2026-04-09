class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Logic for this problem, finding a subsequence of numbers in numa array that increase
        # That subsequence can have different numbers in it
        # Example: [0, 9, 5, 1, 2, 3, 6] -> [0, 1, 2, 3, 6] = 5
        # For each num in nums, we have a choice to include/exclude in subsequence
        # Approach for solving this problem is with Bottom-Up DP, starting at end of nums array
        # Iterate through nums array in reverse from end to zero index
        # Create another nested for loop for comparing num next to index 

        # Initialize DP array where each index has val of 1
        LTS = [1] * len(nums)

        # Go through indexes of nums array in reverse, going towards zero
        for a in range(len(nums) - 1, -1, -1):
            # Nested for loop taht get next number after index a from reverse for loop
            for b in range(a + 1, len(nums)):
                # See if number at a is less than number at b,
                # If True: that means this is inside the LTS(longest increasing subsequence)
                if nums[a] < nums[b]:
                    # Update LTS at index a with max between itself currently and LTS at index b + 1 
                    LTS[a] = max(LTS[a], 1 + LTS[b])

        # Return the max of LTS
        return max(LTS)
