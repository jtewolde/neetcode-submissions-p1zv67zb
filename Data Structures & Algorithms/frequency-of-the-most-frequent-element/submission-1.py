class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # The goal of this problem is to use k operations on elements in nums array 
        # to return the maximum possible freq of an element.
        # Essentially, using k number of operations, increment elements in the array to match value of an element to increase frequency
        # Approach: Use sliding window approach that uses a window that goes through nums array
        # First, sort the nums array and initialize left and right pointers for window and totalSum of 
        # Use right pointer to iterate thorugh nums array for sliding window
        # Add the current number at right to totalSum
        # Then, see if the window size multipled by right pointer number is greater than the sum between totalSum and k value
        # If true, subtract the number at left pointer from total and shrink window by moving left pointer forward
        # Return the difference between length of nums and left pointer for maximum frequency

        # First, initialize left and right pointers for window and totalSum
        left, right = 0, 0
        nums.sort()
        totalSum = 0

        # Use right pointer to iterate thorugh nums array for sliding window
        for right in range(len(nums)):
            # Add the current number at right to totalSum
            totalSum += nums[right]
            
            # Then, see if the window size multipled by right pointer number is greater than the sum between totalSum and k value
            # If true, subtract the number at left pointer from total and shrink window by moving left pointer forward
            if (right - left + 1) * nums[right] > totalSum + k:
                totalSum -= nums[left]
                left += 1

         # Return the difference between length of nums and left pointer for maximum frequency
        return len(nums) - left