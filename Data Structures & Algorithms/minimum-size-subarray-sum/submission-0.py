class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Approach: Use a sliding window techinque to find the minimum length subarray that sums up to the target
       
        # First, initialize left pointer for window, currTotal to track current total of subarray
        # and create result variable to store the minimum length of subarray
        left, currTotal = 0, 0
        result = float("inf")

        # Then, create for loop using right pointer to iterate through nums array
        for right in range(len(nums)):
            # Add the number at right pointer to the currTotal
            currTotal += nums[right]

            # Create a while loop that executes while currtotal is greater or equal to target value
            while currTotal >= target:
                # Update result with the minimum between current result length and window
                result = min(right - left + 1, result)
                # Subtract num at left pointer from currTotal and increment left pointer by one
                currTotal -= nums[left]
                left += 1

        return 0 if result == float("inf") else result

