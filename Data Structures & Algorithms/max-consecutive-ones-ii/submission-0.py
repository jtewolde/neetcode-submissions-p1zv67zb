class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Intution: Using sliding window method to get the window of max consective one's
        # Create a count/streak variable to keep track of number of zeros in current window
        # As long as there is only one zero in the window, the window is valid
        # If current element is a zero on left pointer, change element to one and increment numZero
        # If the current window has more than one zero, then remove leftmost element from window
        # Change leftmost element back to one 
        # Return length of current window as final answer

        # Initialize left pointer for creating sliding window
        # numZeros to keep track of zeros inside of current window
        left = 0
        numZeros = 0

        # Iterate through each number inside of nums
        for num in nums:

            # If current element is zero, then covert to 1 and increment numZeros by one
            if num == 0:
                num = 1
                numZeros += 1
            
            # If there is more than one zero in current window,
            # Convert leftmost element back to zero and increase numZeros by 1
            # Move left pointer forward for window
            if numZeros > 1:
                nums[left] = 0
                numZeros += 1
                left += 1

        # Get the current window size by getting difference between length of nums and left pointer
        return len(nums) - left



        