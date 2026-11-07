class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Approach: Use the sliding window approach to manage the current cost and difference between chars in s ans t strings
        # Calculate the currCost by getting difference between the ASCII chars at right pointer in both strings and take abs value
        # If the currCost of window exceeds maxCost, shrink window by moving left pointer forward and decrement difference from currCost
        # Keep track of the window ize aht doesn't exceed the maxCost and return as final answer
        
        # Initialize needed variables, currCost for tracking the currCost of the window size by getting the difference between the two chars at right pointer
        # Left pointer starts at zero
        # Ans variable will track the max window size while not exceeding currCost
        currCost = 0
        left = 0
        ans = 0

        # Iterate through the length of s as both strings have the same length
        for right in range(len(s)):
            # Get the currCost of window by getting difference of ASCII values on both chars
            currCost += abs(ord(s[right]) - ord(t[right]))
            
            # IF the currCost exceeds the maxCost, decrement the currCost with the difference of the ASCII Chars at left pointer on both strings
            # Then, increment left pointer to move forward with window
            while currCost > maxCost:
                currCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans