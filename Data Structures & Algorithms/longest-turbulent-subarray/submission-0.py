class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Approach: Use a sliding window to find the maximum turbulent subarray in arr
        # A Turbulent array is when the comparison sign between two adjacent elememts alterates
        # Example: [9, 5, 3, 10, 4, 8] => (>, <, >, <. >) = 5 as answer

        # Initialize left and right pointer variables to iterate through arr.
        # and create ans to store length of maximum turbulent subarray and prevSign for storing comparison sign
        left, right = 0, 1
        ans, prevSign = 1, ""

        # Iterate through arr elements using right for sliding window
        while right < len(arr):
            # Case 1: Compare adjacent elements where prev element is greater than curr element
            # Check if previous comparison sign between two elements isn't ">" to determine if window is turbulent
            if arr[right - 1] > arr[right] and prevSign != '>':
                # Update ans to take max length of valid turbulent window, 
                # Move right pointer up one and change prev to ">"
                ans = max(ans, right - left + 1)
                right += 1
                prevSign = ">"
            # Case 2: If current element is greater than prev element and prev sign wasn't "<"
            elif arr[right - 1] < arr[right] and prevSign != "<":
                ans = max(ans, right - left + 1)
                right += 1
                prevSign = "<"
            # Case 3: If the comparison between two elements in arr are equal to each other and use equality sign
            else:
                # Skip elements in arr that are equal to each other by moving right past them
                # Update sliding window by moving left pointer to index of right pointer - 1
                # Set prevSign
                right = right + 1 if arr[right - 1] == arr[right] else right
                left = right - 1
                prevSign = ""
        return ans

