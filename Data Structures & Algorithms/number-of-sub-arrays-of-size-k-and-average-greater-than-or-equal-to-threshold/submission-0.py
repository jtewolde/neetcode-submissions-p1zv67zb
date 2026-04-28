class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Approach: Use sliding window method to get the target sum of current window of arr elemetns
        # Once subarray reaches size of k, then see if the sum of windows equals/exceeds targetSum
        # If it exceeds, increment ans variable that stores nubmer of valid subarrays
        # Then, shrink window from left by removing oldest elements from curSum

        # Initialize variables needed for problem like ans, curSum
        # Multiply threshold with k to get the targetSum to avoid repeated division
        ans = curSum = 0
        threshold *= k

        # Iterate through elements in arr until k window size is reached
        for right in range(len(arr)):
            curSum += arr[right] # Add element into curSum
            # See if window size exceeds/equals k window size for subarray
            if right >= k - 1:
                # If the sum of window exceeds threshold, then add curSum for window to ans variable
                ans += curSum >= threshold
                # Take out oldest element from sum of current window
                curSum -= arr[right - k + 1]

        return ans