class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach for solving this problem is to use Bottom-Up DP
        # Brute force approach for this problem would be to simply iterate through the string
        # Check if every substring is a palidrome or not. Runtime: O(n^3)
        # The DP approach for solving this problem is by using a 2D DP array to store whether a parition of string is a palidrome
        # Then, Iterate through string backwards while other loop goes forward to compare end letters of string
        # See if the letters at each end index are equal.

        # Initialize 2D DP array that stores whether part of string is a palindrome
        # Also, create variables for keeping track of the length and index of longest palidrome
        ansIndx, ansLen = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # Create nested for loop where it starts from end of string and goes backward
        # The b loop goes forward to get both ends of string to see if current length is a palidrome
        for i in range(n - 1, -1, -1):
            for b in range(i, n):
                # See the characters at each end are equal,
                # And that the length of word is less or equal to 2 or inner parts are alos a palidrome
                if s[i] == s[b] and (b - i <= 2 or dp[i + 1][b - 1]):
                    dp[i][b] = True

                    # If the current palidrome is longer than previous one,
                    # Update the ans variables to match longest
                    if ansLen < (b - i + 1):
                        ansIndx = i
                        ansLen = b - i + 1 
        
        # Final answer is returning the longest palindrome 
        return s[ansIndx: ansIndx + ansLen]

