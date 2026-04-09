class Solution:
    def numDecodings(self, s: str) -> int:
        # Approach for solving this problem is by using Top-Bottom DP with Memoization
        # Base cases: If current index out of bounds: return 1
        # If current digit is '0', return 0 as there isn't any char that maps to '0'
        # The recurrence relation/decision is whether to decode one or two digits combined, dfs[i] = dfs[i + 1] + dfs[i + 2]
        # Any two digit combination can't be more than the len of s(26)

        # First, create memo hashmap with len of string, initialized with digit '1'
        # Create DFS function that takes index as argument
        # Establish base cases where current digit = '0', return 0 and return dp[i] if i in dp
        # Create ans variable that calls dfs[i + 1] for only taking one digit
        # See if valid double digit can be formed and added to ans
        # Conditions to be met: If current char is a '1' or '2' and if char + 1 is in '0123456'
        # This is to make sure that double digit number is less than 26 and is valid

        # Initialize memo hashmap where val is '1' for length of stirng
        memo = {len(s): 1}

        # Create DFS function that takes index as argument
        def dfs(indx):
            # Establish base cases where current indx is already in memo, return it from memo,
            # If current char in s at indx == 0, return 0
            if indx in memo:
                return memo[indx]
            elif s[indx] == '0':
                return 0

            # Take in one digit to the ans variable
            ans = dfs(indx + 1)

            # See if conditions are met for a valid double digit number to be created, add to ans
            if indx + 1 < len(s) and (s[indx] == '1' or s[indx] == '2' and s[indx + 1] in '0123456'):
                ans += dfs(indx + 2)

            # Cache the result into memo
            memo[indx] = ans
            return ans

        return dfs(0)

        

