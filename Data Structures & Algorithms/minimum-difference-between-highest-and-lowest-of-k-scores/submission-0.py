class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Approach: Sort the entire nums array increasingly from min to max to get smallest range of k elements
        # Use sliding window techinque to find the minimum difference between k scores
        # Create two pointers, left and right, starting from 0 and k -1 to represent window of k size

        # Initialize left and right pointers that has window size of K scores
        # Sort nums array to make adjacent elements be similar in range
        # Create ans variable to keep track of minimum difference 
        left, right = 0, k - 1
        nums.sort()
        ans = float('inf')

        # Iterate through nums array through right pointer while being in bounds
        while right < len(nums):
            # Get current difference between numbers in high and low values in window with left/right pointers
            diff = nums[right] - nums[left]
            # Update ans by taking minimum value between current ans and diff
            ans = min(ans, diff)
            # Increment both pointers by one to get new window
            left += 1
            right += 1

        return ans

