class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Logic: Find the k number of integers in array that are closet to integer b
        # Synposis: Use the sliding window/two pointers to iterate through array,
        # Compare current num to see if num is close to integer x than other num
        # Two Pointers approach runtime: O(N)
        
        # Initialize left and right pointers for window size
        left, right = 0, len(arr) - 1

        # Perform while the window size is bigger than k
        while right - left >= k: 
            # Check if num at left is further to k than num at right
            # If so, increment left by one to shrink window
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                # Shrink window by decrementing right by one
                right -= 1
        # Return window between left and right pointers in arr
        return arr[left : right+1]

