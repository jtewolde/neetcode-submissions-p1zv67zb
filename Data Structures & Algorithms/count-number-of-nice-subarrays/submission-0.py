class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Approach: Use a sliding window that uses three pointers like left, mid, and right to find windows that are nice subarrays
        # A nice subarray is when a subarray has exactly k odd elements in the window
        
        # Initialize left and mid pointer for the sliding window iteration through nums array
        # Also, create ans and odd variables to keep track of num of nice subarrays and odd nums in current window
        ans, odd = 0, 0
        left, mid = 0, 0
        
        # Iterate through the nums array using right pointer, 
        # Check if the num at right pointer is odd, then increment odd variable
        for right in range(len(nums)):
            if nums[right] % 2:
                odd += 1
            
            # Check if the num of odd elements exceeds value of k, then shrink window by moving left pointer and mid pointer up
            # Check if number at left pointer is odd, if true then decrement odd variable
            while odd > k:
                if nums[left] % 2:
                    odd -= 1
                left += 1
                mid = left

            # Check if num of odd elements in curr window equals value of k
            if odd == k:
                # While the number at mid pointer isn't odd, increment mid pointer
                while not nums[mid] % 2:
                    mid += 1
                ans += (mid - left) + 1
        return ans
