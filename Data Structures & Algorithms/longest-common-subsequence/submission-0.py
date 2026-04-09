class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Goal: Compare the two text strings, see if either of the texts are a subsequence of each other
        # Return the max length of the subsequence
        # Approach: Use a 2D array to kep track of length of subsequences for each decision
        # The cell dp[i][j] represents the length of LCS at indexes for text1 and text2
        # Logic: Iterate through both texts, compare the characters at both texts at current index
        # If chars are the same, increment dp[i - 1][j - 1] by one to increase LCS
        # If not, take the max between two options of changing index on text1 or text2
        # Note: Indexes have +1 or -1 because DP array are zero-indexed

        # Create variables for length of each text string
        len1, len2 = len(text1), len(text2)

        # Initialize 2D array that has dimensions of len1 and len2
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # Iterate through the entire 2D array
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # If characters match, increment LCS by one from previous diagonal cell
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                # If not, take the max between left or top cell 
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        # Return entire LCS length for complete strings
        return dp[len1][len2]
