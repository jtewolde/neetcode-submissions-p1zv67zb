class Solution:
    def countSubstrings(self, s: str) -> int:
        # Approach: Use a 2D Dynamic Programming to determine if the substring between index i and j is a palindrome
        # With DP, it reuses the previous results to build solutions for longer strings by using the shorter ones
        
        # Initialize ans as counter for amount of palindrome substrings and N for length of the given string
        # Also, initlaize 2-D DP array with all initial results as false for every index in N
        N, ans = len(s), 0
        dp = [[False] * N for _ in range(N)]

        # Use a nested for loop to traverse the string bottom-top where one pointer goes through it reversed
        # And the other pointer goes through the string, starting from the i pointer
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                # For each (i, j) where j >= j, determine if the characters at both pointers are equal
                # Also, if the difference between the two pointers are less or equal to 2 or the palindrome of the previous result is true
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1] == True):
                    # Mark the current dp result as True and increment ans by 1
                    dp[i][j] = True
                    ans += 1

        return ans

        