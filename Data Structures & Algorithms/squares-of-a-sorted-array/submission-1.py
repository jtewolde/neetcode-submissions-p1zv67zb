class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Optimal Two Pointers Approach: Create left and right pointers for squaring numbers
        # Compare squared numbers at each pointer and take the less out of two to add to ans array

        # Initialize left and right pointers for comparing squared numbers
        # Create ans array that stores sorted squared numbers
        left, right = 0, len(nums) - 1
        ans = []

        # Traverse through nums array with left and right pointers
        while left <= right:
            # Compare squared numbers from left and right, 
            # Append the greater number into the ans array and increment/decrement appropriate pointer
            if (nums[left] * nums[left]) > (nums[right] * nums[right]):
                ans.append(nums[left] * nums[left])
                left += 1
            else:
                ans.append(nums[right] * nums[right])
                right -= 1

        # Return the reversed ans array to be sorted increasingly
        return ans[::-1]

